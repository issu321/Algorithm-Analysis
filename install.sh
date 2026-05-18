#!/usr/bin/env bash
# ============================================================
#  USSU'S ULTRA PRO MAX ALGORITHM ANALYZER v4.0
#  Kali Linux / Unix Installation Script
#  Author: Ussu | github.com/issu321
# ============================================================

set -e

# Cyberpunk Colors
CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
MAGENTA='\033[95m'
BLUE='\033[94m'
WHITE='\033[97m'
BOLD='\033[1m'
DIM='\033[2m'
END='\033[0m'

clear

echo ""
echo -e "${BOLD}${CYAN}    ██╗   ██╗███████╗███████╗██╗   ██╗${END}"
echo -e "${BOLD}${CYAN}    ██║   ██║██╔════╝██╔════╝██║   ██║${END}"
echo -e "${BOLD}${CYAN}    ██║   ██║███████╗███████╗██║   ██║${END}"
echo -e "${BOLD}${CYAN}    ██║   ██║╚════██║╚════██║██║   ██║${END}"
echo -e "${BOLD}${CYAN}    ╚██████╔╝███████║███████║╚██████╔╝${END}"
echo -e "${BOLD}${CYAN}     ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ${END}"
echo ""
echo -e "${BOLD}${MAGENTA}         ╔═══════════════════════════════════════════════════════╗${END}"
echo -e "${BOLD}${MAGENTA}         ║     ULTRA PRO MAX ALGORITHM ANALYZER v4.0            ║${END}"
echo -e "${BOLD}${MAGENTA}         ║     Kali Linux / Unix Installation Wizard             ║${END}"
echo -e "${BOLD}${MAGENTA}         ║     github.com/issu321                                ║${END}"
echo -e "${BOLD}${MAGENTA}         ╚═══════════════════════════════════════════════════════╝${END}"
echo ""

# Check Python
echo -e "${BOLD}${CYAN}[SYSTEM CHECK]${END} Verifying Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[✗ ERROR]${END} python3 is not installed."
    echo -e "${YELLOW}[!] Run: sudo apt update && sudo apt install python3 python3-pip${END}"
    exit 1
fi

PYVER=$(python3 --version)
echo -e "${GREEN}[✓ FOUND]${END} $PYVER"

# Check pip
echo ""
echo -e "${BOLD}${CYAN}[SYSTEM CHECK]${END} Verifying pip..."
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}[✗ ERROR]${END} pip3 is not installed."
    echo -e "${YELLOW}[!] Run: sudo apt install python3-pip${END}"
    exit 1
fi
echo -e "${GREEN}[✓ FOUND]${END} pip3 is ready."

# Create directories
echo ""
echo -e "${BOLD}${CYAN}[SETUP]${END} Creating workspace directories..."
mkdir -p graphs reports data
echo -e "${GREEN}[✓]${END} graphs/  ${GREEN}[✓]${END} reports/  ${GREEN}[✓]${END} data/"

# Install dependencies
echo ""
echo -e "${BOLD}${CYAN}[INSTALL]${END} Installing Python dependencies..."
echo -e "${DIM}This may take a moment...${END}"
echo ""

pip3 install -r requirements.txt

# Make app.py executable
chmod +x app.py

# Success banner
echo ""
echo -e "${BOLD}${GREEN}╔═══════════════════════════════════════════════════════════════╗${END}"
echo -e "${BOLD}${GREEN}║                    INSTALLATION COMPLETE                       ║${END}"
echo -e "${BOLD}${GREEN}╠═══════════════════════════════════════════════════════════════╣${END}"
echo -e "${BOLD}${GREEN}║  ✓ Python Environment Verified                                 ║${END}"
echo -e "${BOLD}${GREEN}║  ✓ All Dependencies Installed                                  ║${END}"
echo -e "${BOLD}${GREEN}║  ✓ Workspace Directories Ready                                 ║${END}"
echo -e "${BOLD}${GREEN}║  ✓ Execution Permissions Set                                   ║${END}"
echo -e "${BOLD}${GREEN}╚═══════════════════════════════════════════════════════════════╝${END}"
echo ""
echo -e "${BOLD}${CYAN}[LAUNCH]${END} Run the analyzer with:"
echo -e "${WHITE}    python3 app.py${END}"
echo -e "${WHITE}    ./app.py${END}"
echo ""
echo -e "${DIM}Made with 💙 by Ussu | github.com/issu321${END}"
echo ""