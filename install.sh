#!/usr/bin/env bash
# Cross-platform setup for macOS, Debian/Ubuntu, and Arch.
# Creates a .venv in the project root and installs requirements.txt into it.
#
# Usage:
#   ./install.sh
# Then to play:
#   source .venv/bin/activate
#   python main.py

set -euo pipefail

PY_MIN_MAJOR=3
PY_MIN_MINOR=8

# ---------- platform detection ----------
detect_platform() {
    case "$(uname -s)" in
        Darwin) echo "mac" ;;
        Linux)
            if [ -r /etc/os-release ]; then
                # shellcheck disable=SC1091
                . /etc/os-release
                case "${ID:-}${ID_LIKE:-}" in
                    *arch*)            echo "arch" ;;
                    *debian*|*ubuntu*) echo "debian" ;;
                    *)                 echo "linux-unknown" ;;
                esac
            else
                echo "linux-unknown"
            fi
            ;;
        *) echo "unknown" ;;
    esac
}

PLATFORM=$(detect_platform)
echo "Detected platform: $PLATFORM"

# ---------- python install hint ----------
install_python_hint() {
    case "$PLATFORM" in
        mac)    echo "  brew install python" ;;
        debian) echo "  sudo apt update && sudo apt install -y python3 python3-venv python3-pip" ;;
        arch)   echo "  sudo pacman -S --needed python python-pip" ;;
        *)      echo "  (install Python 3.${PY_MIN_MINOR}+ from https://www.python.org/downloads/)" ;;
    esac
}

# ---------- find a usable python ----------
PYTHON=""
for candidate in python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then
        if "$candidate" -c "import sys; sys.exit(0 if sys.version_info >= ($PY_MIN_MAJOR, $PY_MIN_MINOR) else 1)" 2>/dev/null; then
            PYTHON="$candidate"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python ${PY_MIN_MAJOR}.${PY_MIN_MINOR}+ not found." >&2
    echo "Install it with:" >&2
    install_python_hint >&2
    exit 1
fi

echo "Using $PYTHON ($($PYTHON --version 2>&1))"

# ---------- ensure venv module is available (Debian splits it out) ----------
if ! "$PYTHON" -c "import venv" 2>/dev/null; then
    echo "ERROR: 'venv' module not available for $PYTHON." >&2
    echo "Install it with:" >&2
    install_python_hint >&2
    exit 1
fi

# ---------- create venv ----------
if [ ! -d .venv ]; then
    echo "Creating virtual environment in .venv ..."
    "$PYTHON" -m venv .venv
else
    echo ".venv already exists, reusing it."
fi

# ---------- install deps ----------
# shellcheck disable=SC1091
. .venv/bin/activate
echo "Upgrading pip ..."
python -m pip install --upgrade pip >/dev/null
echo "Installing requirements ..."
python -m pip install -r requirements.txt

echo ""
echo "Done. To play:"
echo "    source .venv/bin/activate"
echo "    python main.py"
