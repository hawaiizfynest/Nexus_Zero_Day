# -*- mode: python ; coding: utf-8 -*-
# NEXUS: Zero Day — PyInstaller build spec
# Produces a single-file Windows executable.
#
# Usage (run on Windows or via GitHub Actions):
#   pip install pyinstaller
#   pyinstaller nexus.spec

import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['nexus.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # Include the entire game package
        ('game', 'game'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.font',
        'tkinter.messagebox',
        'tkinter.simpledialog',
        'tkinter.scrolledtext',
        'game.story',
        'game.engine',
        'game.ui',
        'game.ui.main_window',
        'game.ui.terminal',
        'game.ui.mission_panel',
        'game.ui.network_map',
        'game.ui.dialogue',
        'game.ui.edu_panel',
        'game.ui.codex_window',
        'game.ui.exploit_window',
        'game.ui.minigame',
        'game.ui.help_window',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'numpy', 'pandas', 'scipy',
        'PIL', 'cv2', 'PyQt5', 'wx',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NEXUS_ZeroDay',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    # Single file — no install needed, just run the .exe
    onefile=True,
    console=False,           # No console window (GUI only)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # Window icon (add assets/icon.ico to enable)
    # icon='assets/icon.ico',
    version_file=None,
)
