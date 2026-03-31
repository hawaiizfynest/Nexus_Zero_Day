#!/usr/bin/env python3
"""
NEXUS: Zero Day
A cybersecurity education simulation game.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Ensure local imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.engine import GameEngine
from game.ui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.withdraw()  # Hide until fully loaded

    try:
        engine = GameEngine()
        app = MainWindow(root, engine)
        root.deiconify()
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal Error", f"Failed to start NEXUS:\n{e}")
        raise

if __name__ == "__main__":
    main()
