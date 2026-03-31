Created by HawaiizFynest

# NEXUS: Zero Day

> A cybersecurity education simulation — learn real attack techniques through immersive gameplay.

![Build Status](https://github.com/hawaiizfynest/nexus-zero-day/actions/workflows/build.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## About

You are **Alex Ryder** — handle: `gh0st`. Former network engineer, now hacktivist.

Vera Kaine (ex-NSA) has recruited you to expose **PROJECT LAZARUS** — a hidden internet
kill-switch buried inside global CDN infrastructure, built by the defence contractor that
destroyed your career.

NEXUS: Zero Day is a desktop hacking simulation inspired by *Uplink*, built to teach real
cybersecurity concepts through an immersive story with characters, missions, and interactive
minigames.

---

## Features

- **Full story** — 4 chapters, 12 missions, 6 characters with typewriter dialogue
- **Real techniques** — port scanning, SQL injection, buffer overflows, rootkits, zero-days, MITM, and more
- **Interactive minigames** — Port Mapper, Cipher Decoder, Firewall Bypass
- **Codex** — 12 in-depth cybersecurity education entries with real-world breach case studies
- **In-game help** — tabbed getting-started guide built into the game
- **Save/load** — 3 save slots, stored in `~/Documents/NEXUS_ZeroDay/saves/`
- **Fullscreen** — F11 to toggle, fully responsive layout
- **No dependencies** — pure Python standard library + tkinter

---

## Installation

### Option 1 — Download the executable (easiest)

Go to [**Releases**](https://github.com/hawaiizfynest/nexus-zero-day/releases) and download:

| Platform | File |
|----------|------|
| Windows  | `NEXUS_ZeroDay.exe` — double-click to run, no install needed |
| macOS    | `NEXUS_ZeroDay_macOS.zip` — unzip and run |

### Option 2 — Run from source

Requires **Python 3.8+** with tkinter (included in standard Python installers).

```bash
git clone https://github.com/hawaiizfynest/nexus-zero-day.git
cd nexus-zero-day
python3 nexus.py
```

**Windows:**
```
LAUNCH_NEXUS.bat
```

**macOS (if tkinter missing):**
```bash
brew install python-tk
./launch_nexus.sh
```

**Linux:**
```bash
sudo apt install python3-tk
./launch_nexus.sh
```

---

## Building the executable yourself

```bash
pip install pyinstaller
pyinstaller nexus.spec
# Output: dist/NEXUS_ZeroDay.exe
```

Or push a version tag to trigger the GitHub Actions build automatically:

```bash
git tag v1.0
git push origin v1.0
# GitHub builds Windows + macOS executables and creates a release
```

---

## How to Play

1. **Accept a contract** — click a mission card in the right panel, or type `missions` → `accept 1`
2. **Scan your target** — type `scan` or click PORT SCAN in the left toolkit
3. **Run the minigame** — your performance boosts exploit success probability
4. **Execute the exploit** — click EXECUTE EXPLOIT in the exploit window
5. **Manage your trace** — type `bounce` early, use LOG WIPE to reduce trace
6. **Read the Codex** — after each mission, learn the real cybersecurity concept (+2 REP)
7. **Save often** — SAVE button in the top bar, or type `save`

Press **F11** for fullscreen. Click **HELP** in the top bar for the full in-game guide.

---

## Story

| Chapter | Title | Techniques |
|---------|-------|------------|
| 1 | First Contact | Port scanning, default credentials, SQL injection |
| 2 | The Network Beneath | MITM/TLS, buffer overflow, spear phishing |
| 3 | Ghost Protocol | Rootkits, C2 infrastructure, lateral movement / air gaps |
| 4 | Zero Day | Zero-day exploits, race conditions, certificate trust |

---

## Cybersecurity Topics (Codex)

| # | Topic | Unlocked by |
|---|-------|-------------|
| 1 | Port Scanning & Reconnaissance | Ghost in the Wire |
| 2 | Default & Weak Credentials | Default Sins |
| 3 | SQL Injection | Injection Season |
| 4 | Man-in-the-Middle & TLS | Man in the Middle |
| 5 | Buffer Overflow | Buffer Overflow Blues |
| 6 | Phishing & Social Engineering | Phishing Season |
| 7 | Rootkits & Persistence | Rootkit |
| 8 | Command & Control Infrastructure | The Counter-Hunt |
| 9 | Lateral Movement & Air Gaps | The Architecture |
| 10 | Zero-Day Vulnerabilities | Zero Day |
| 11 | Race Conditions & Timing Attacks | The Kill Switch |
| 12 | PKI & Certificate Trust | Dead Man's Switch |

---

## Project Structure

```
nexus-zero-day/
├── nexus.py                  # Entry point
├── nexus.spec                # PyInstaller build spec
├── LAUNCH_NEXUS.bat          # Windows launcher
├── launch_nexus.sh           # macOS/Linux launcher
├── .github/
│   └── workflows/
│       └── build.yml         # Auto-build Windows + macOS executables on tag push
└── game/
    ├── engine.py             # Game state, save/load, exploit logic
    ├── story.py              # All narrative, missions, characters, Codex content
    └── ui/
        ├── main_window.py    # Main UI — layout, terminal, commands
        ├── terminal.py       # Terminal widget
        ├── mission_panel.py  # Contracts panel
        ├── network_map.py    # Target network map
        ├── dialogue.py       # Character transmission popups
        ├── edu_panel.py      # Single-topic Codex popup
        ├── codex_window.py   # Full Codex browser
        ├── exploit_window.py # Exploit sequence + minigames
        ├── minigame.py       # Minigame routing
        └── help_window.py    # In-game help system
```

---

## Contributing

Pull requests are welcome. Please open an issue first for significant changes.

Areas that would benefit from contribution:
- Additional missions and story chapters
- New minigame types
- Linux `.AppImage` packaging
- Accessibility improvements (font scaling, high-contrast mode)

---

## Disclaimer

NEXUS: Zero Day is an **educational simulation**. All targets, organisations, and individuals
are entirely fictional. No real systems are accessed or harmed. The cybersecurity techniques
described are real — always apply them legally and ethically, only on systems you own or
have explicit written permission to test.

---

## License

MIT — see [LICENSE](LICENSE)

---

*"Before you ever touch a target, you understand it completely." — 0xVERA*
