@echo off
title NEXUS: Zero Day — Launcher
color 0A
cls

echo.
echo  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
echo  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
echo  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
echo  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
echo  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
echo  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
echo.
echo                  Z E R O   D A Y
echo         Cybersecurity Education Simulation
echo.

:: Check Python
python --version > nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found. Installing...
    echo  Downloading Python 3.11 installer...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile '%TEMP%\python_installer.exe'"
    echo  Running installer (check 'Add to PATH')...
    start /wait %TEMP%\python_installer.exe /quiet InstallAllUsers=0 PrependPath=1 Include_tcltk=1
    echo  Python installed. Relaunch this file.
    pause
    exit
)

:: Check tkinter
python -c "import tkinter" > nul 2>&1
if errorlevel 1 (
    echo  [ERROR] tkinter not available.
    echo  Please reinstall Python with the tcl/tk option checked.
    pause
    exit
)

echo  [OK] Python found.
echo  [*]  Launching NEXUS: Zero Day...
echo.

:: Launch from game directory
cd /d "%~dp0"
python nexus.py

if errorlevel 1 (
    echo.
    echo  [ERROR] Game crashed. Check error above.
    pause
)
