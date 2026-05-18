@echo off
title USSU Ultra Algorithm Analyzer v4.0 - Windows Installer
chcp 65001 >nul
color 0B

:: ============================================================
::  USSU'S ULTRA PRO MAX ALGORITHM ANALYZER v4.0
::  Windows 11 Installation Script
::  Author: Ussu | github.com/issu321
:: ============================================================

setlocal enabledelayedexpansion

:: Cyberpunk Colors
set "CYAN=[36m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "RED=[91m"
set "MAGENTA=[95m"
set "BLUE=[94m"
set "WHITE=[97m"
set "BOLD=[1m"
set "DIM=[2m"
set "END=[0m"

echo.
echo  %BOLD%%CYAN%    ██╗   ██╗███████╗███████╗██╗   ██╗%END%
echo  %BOLD%%CYAN%    ██║   ██║██╔════╝██╔════╝██║   ██║%END%
echo  %BOLD%%CYAN%    ██║   ██║███████╗███████╗██║   ██║%END%
echo  %BOLD%%CYAN%    ██║   ██║╚════██║╚════██║██║   ██║%END%
echo  %BOLD%%CYAN%    ╚██████╔╝███████║███████║╚██████╔╝%END%
echo  %BOLD%%CYAN%     ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ %END%
echo.
echo  %BOLD%%MAGENTA%         ╔═══════════════════════════════════════════════════════╗%END%
echo  %BOLD%%MAGENTA%         ║     ULTRA PRO MAX ALGORITHM ANALYZER v4.0            ║%END%
echo  %BOLD%%MAGENTA%         ║     Windows 11 Installation Wizard                    ║%END%
echo  %BOLD%%MAGENTA%         ║     github.com/issu321                                ║%END%
echo  %BOLD%%MAGENTA%         ╚═══════════════════════════════════════════════════════╝%END%
echo.

:: Check Python
echo  %BOLD%%CYAN%[SYSTEM CHECK]%END% Verifying Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo  %RED%[✗ ERROR]%END% Python is not installed or not in PATH.
    echo  %YELLOW%[!] Please install Python 3.10+ from https://python.org%END%
    pause
    exit /b 1
)
for /f "tokens=*" %%a in ('python --version') do set PYVER=%%a
echo  %GREEN%[✓ FOUND]%END% %PYVER%

:: Check pip
echo.
echo  %BOLD%%CYAN%[SYSTEM CHECK]%END% Verifying pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo  %RED%[✗ ERROR]%END% pip is not available.
    pause
    exit /b 1
)
echo  %GREEN%[✓ FOUND]%END% pip is ready.

:: Create directories
echo.
echo  %BOLD%%CYAN%[SETUP]%END% Creating workspace directories...
if not exist "graphs" mkdir graphs
if not exist "reports" mkdir reports
if not exist "data" mkdir data
echo  %GREEN%[✓]%END% graphs/  %GREEN%[✓]%END% reports/  %GREEN%[✓]%END% data/

:: Install dependencies
echo.
echo  %BOLD%%CYAN%[INSTALL]%END% Installing Python dependencies...
echo  %DIM%This may take a moment...%END%
echo.

pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo  %RED%[✗ FAILED]%END% Dependency installation failed.
    echo  %YELLOW%[!] Try running as Administrator%END%
    pause
    exit /b 1
)

:: Success
echo.
echo  %BOLD%%GREEN%╔═══════════════════════════════════════════════════════════════╗%END%
echo  %BOLD%%GREEN%║                    INSTALLATION COMPLETE                       ║%END%
echo  %BOLD%%GREEN%╠═══════════════════════════════════════════════════════════════╣%END%
echo  %BOLD%%GREEN%║  ✓ Python Environment Verified                                 ║%END%
echo  %BOLD%%GREEN%║  ✓ All Dependencies Installed                                  ║%END%
echo  %BOLD%%GREEN%║  ✓ Workspace Directories Ready                                 ║%END%
echo  %BOLD%%GREEN%╚═══════════════════════════════════════════════════════════════╝%END%
echo.
echo  %BOLD%%CYAN%[LAUNCH]%END% Run the analyzer with:
echo  %WHITE%    python app.py%END%
echo.
echo  %DIM%Made with 💙 by Ussu | github.com/issu321%END%
echo.
pause