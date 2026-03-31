#!/usr/bin/env bash
# NEXUS: Zero Day — macOS / Linux Launcher

cd "$(dirname "$0")"

echo ""
echo "  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗"
echo "  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
echo "           Z E R O   D A Y"
echo ""

# Find python3
if ! command -v python3 &>/dev/null; then
    echo "[ERROR] python3 not found."
    echo "Install via: sudo apt install python3 python3-tk   (Debian/Ubuntu)"
    echo "         or: brew install python-tk                (macOS)"
    exit 1
fi

# Check tkinter
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[ERROR] tkinter not available."
    echo "Install via: sudo apt install python3-tk   (Debian/Ubuntu)"
    echo "         or: brew install python-tk        (macOS Homebrew)"
    exit 1
fi

echo "[OK] Python + tkinter found."
echo "[*]  Launching NEXUS: Zero Day..."
echo ""

python3 nexus.py
