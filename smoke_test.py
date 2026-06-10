"""
Headless smoke test for Catch the Falling Items.

Runs the whole game without a display or audio device (SDL "dummy" drivers) so
it can execute in CI. It builds a Game, exercises every registered item type
(draw / update / on_collect / on_missed), and steps the main update loop many
times, asserting the core rules hold:

    * catching a good item raises the score
    * catching a Bomb lowers the score by 5
    * catching a Magnet arms the magnet and pulls items toward the basket
    * missing items raises the miss counter and eventually ends the game

Exit code 0 means everything works; any assertion or exception fails the build.
Run locally with:  python smoke_test.py
"""

import os

# Must be set before pygame is imported anywhere.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from main import Game
from items import ITEMS
from config import HEIGHT, MAX_MISSES


def all_item_classes():
    seen = []
    for bucket in ITEMS.values():
        for cls in bucket:
            if cls not in seen:
                seen.append(cls)
    return seen


def center_on_basket(game, item):
    """Place an item exactly where the basket will catch it."""
    item.x = game.basket.x + game.basket.width // 2
    item.y = game.basket.y


def test_construction():
    game = Game()
    assert game.basket is not None
    assert game.magnet_until == 0, "magnet should start disarmed"
    print("  ok: Game constructs and resets cleanly")
    return game


def test_each_item_renders_and_collects(game):
    surface = pygame.Surface((10, 10))
    for cls in all_item_classes():
        item = cls(pos=(100, 0), weight=1.0)
        item.update()          # one frame of falling
        item.draw(surface)     # must not raise
        item.on_collect(game)  # collect hook
        assert item.alive is False, f"{cls.__name__} should be consumed on collect"
    print(f"  ok: all {len(all_item_classes())} item types draw/update/collect")


def test_score_and_bomb(game):
    game.reset()
    # Good item raises score.
    from items.apple import Apple
    apple = Apple(pos=(0, 0))
    apple.on_collect(game)
    assert game.score == 1, f"apple should give +1, got {game.score}"

    # Bomb lowers score by 5.
    from items.bomb import Bomb
    before = game.score
    Bomb(pos=(0, 0)).on_collect(game)
    assert game.score == before - 5, f"bomb should subtract 5, got {game.score}"
    print("  ok: scoring (apple +1) and bomb penalty (-5) apply")


def test_magnet_pull(game):
    game.reset()
    from items.magnet import Magnet
    Magnet(pos=(0, 0)).on_collect(game)
    assert game.magnet_until > pygame.time.get_ticks(), "magnet should arm a timer"

    # An item to the left of the basket should drift right (toward center).
    basket_center = game.basket.x + game.basket.width // 2
    item = Magnet(pos=(basket_center - 100, 50))
    game.items = [item]
    start_dx = abs(item.x - basket_center)
    game.update()
    end_dx = abs(item.x - basket_center)
    assert end_dx < start_dx, "magnet should pull items toward the basket center"
    print("  ok: magnet arms and pulls items toward the basket")


def test_missing_ends_game(game):
    game.reset()
    # Drop MAX_MISSES items past the bottom edge.
    from items.apple import Apple
    for _ in range(MAX_MISSES):
        item = Apple(pos=(300, HEIGHT + 50))
        game.items = [item]
        game.update()
    assert game.misses >= MAX_MISSES, "misses should accumulate"
    assert game.game_over is True, "game should end after MAX_MISSES"
    print(f"  ok: {MAX_MISSES} misses ends the game")


def test_dash_jump_costs_two_stamina(game):
    from config import MAX_STAMINA, DASH_JUMP_COST
    b = game.basket
    b.stamina = float(MAX_STAMINA)
    b.on_ground = True
    b.facing = 1
    b.dash()   # spends DASH_COST and opens the dash-jump window
    assert b.dash_jump_window > 0, "dash should open the dash-jump window"
    b.jump()   # combo should bring the total spend up to DASH_JUMP_COST
    spent = MAX_STAMINA - b.stamina
    assert abs(spent - DASH_JUMP_COST) < 1e-9, (
        f"dash-jump should cost {DASH_JUMP_COST} stamina, spent {spent}"
    )
    print(f"  ok: dash-jump combo costs {DASH_JUMP_COST} stamina")


def test_main_loop_steps(game):
    game.reset()
    # Spawn and step many frames; nothing should raise.
    for _ in range(300):
        game.spawn_item()
        game.update()
        game.draw()
    print("  ok: 300 spawn/update/draw frames run without error")


def main():
    print("Headless smoke test: Catch the Falling Items")
    game = test_construction()
    test_each_item_renders_and_collects(game)
    test_score_and_bomb(game)
    test_magnet_pull(game)
    test_dash_jump_costs_two_stamina(game)
    test_missing_ends_game(game)
    test_main_loop_steps(game)
    pygame.quit()
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
