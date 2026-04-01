# NEXUS: Zero Day

**A cybersecurity education simulation — learn real attack and defence techniques through an immersive story.**

![Build Status](https://github.com/hawaiizfynest/nexus_zero_day/actions/workflows/build.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-2.0-brightgreen)

---

## What is this?

You are **Alex Ryder** — handle: `gh0st`. Former network engineer turned hacktivist.

Veteran hacker **Vera Kaine** (ex-NSA, Tailored Access Operations) has recruited you to investigate **PROJECT LAZARUS** — a hidden internet kill-switch embedded inside global CDN infrastructure, built by the defence contractor that destroyed your career.

NEXUS: Zero Day is a desktop hacking simulation inspired by *Uplink*. Every mission teaches a real cybersecurity technique — from port scanning and SQL injection to malware reverse engineering and zero-day exploits. The Codex explains the science behind each attack, how defenders detect it, and a real-world breach case study.

---

## Features

| | |
|---|---|
| **Story** | 4 chapters, 14 missions, 6 characters with typewriter dialogue |
| **Techniques** | Offensive and defensive — see full list below |
| **Minigames** | Port Mapper · Cipher Decoder · Firewall Bypass — affect exploit success |
| **Codex** | 14 in-depth cybersecurity education entries with real breach case studies |
| **Help system** | Tabbed in-game guide — Getting Started, Interface, Walkthrough, Commands, Tips |
| **Save / Load** | 3 save slots stored in `~/Documents/NEXUS_ZeroDay/saves/` |
| **Fullscreen** | F11 to toggle, fully responsive layout at any window size |
| **No dependencies** | Pure Python standard library + tkinter — nothing to pip install |

---

## Download & Run

### Easiest — grab the executable

Go to [**Releases**](https://github.com/hawaiizfynest/nexus_zero_day/releases/latest) and download for your platform:

| Platform | File | Notes |
|----------|------|-------|
| **Windows** | `NEXUS_ZeroDay.exe` | Double-click — no install, no Python needed |
| **macOS** | `NEXUS_ZeroDay_macOS.zip` | Unzip and run. If blocked: right-click → Open |

### Run from source

Requires **Python 3.8+** with tkinter (included in standard Python installers on Windows and macOS).

```bash
git clone https://github.com/hawaiizfynest/nexus_zero_day.git
cd nexus_zero_day
python3 nexus.py
```

**Linux:**
```bash
sudo apt install python3-tk
python3 nexus.py
```

**macOS (if tkinter is missing):**
```bash
brew install python-tk
python3 nexus.py
```

---

## How to Play

1. **Accept a contract** — click a mission card in the right panel, or type `missions` → `accept 1`
2. **Scan your target** — type `scan` or click PORT SCAN in the left toolkit
3. **Complete the minigame** — better performance = higher exploit success rate
4. **Execute the exploit** — click EXECUTE EXPLOIT in the exploit window
5. **Watch your trace** — type `bounce` to activate proxy routing and reduce trace generation by 70%
6. **Read the Codex** — after each mission, learn the real cybersecurity concept behind what you just did (+2 REP)
7. **Save often** — SAVE button in the top bar, or type `save`

**Keyboard:** F11 = fullscreen · ↑/↓ = command history · Tab = autocomplete · Escape = exit fullscreen

Click **HELP** in the top bar for the full in-game getting started guide.

---

## Story & Missions

| Chapter | Title | Missions |
|---------|-------|---------|
| **1** | First Contact | Ghost in the Wire · Default Sins · Injection Season |
| **2** | The Network Beneath | Man in the Middle · Buffer Overflow Blues · Phishing Season |
| **3** | Ghost Protocol | Rootkit · The Counter-Hunt · The Architecture · Ghost in the Binary · Running the Specimen |
| **4** | Zero Day | Zero Day · The Kill Switch · Dead Man's Switch |

---

## Cybersecurity Techniques Covered

### Offensive
| Technique | Mission |
|-----------|---------|
| Port Scanning & Reconnaissance | Ghost in the Wire |
| Default & Weak Credentials | Default Sins |
| SQL Injection | Injection Season |
| Man-in-the-Middle & TLS interception | Man in the Middle |
| Buffer Overflow exploitation | Buffer Overflow Blues |
| Phishing & Social Engineering | Phishing Season |
| Rootkits & Kernel Persistence | Rootkit |
| Command & Control Infrastructure | The Counter-Hunt |
| Lateral Movement & Air Gap bridging | The Architecture |
| Zero-Day Vulnerability exploitation | Zero Day |
| Race Conditions & Timing Attacks | The Kill Switch |
| PKI & Certificate Trust abuse | Dead Man's Switch |

### Defensive (v2.0)
| Technique | Mission |
|-----------|---------|
| Malware Static Analysis — strings, PE headers, YARA rules | Ghost in the Binary |
| Malware Dynamic Analysis — sandboxing, IOC extraction, behavioural logging | Running the Specimen |

---

## Characters

| Handle | Name | Role |
|--------|------|------|
| `gh0st` | Alex Ryder | You — ex-OmniCorp engineer, now hacktivist |
| `0xVERA` | Vera Kaine | Mentor — ex-NSA Tailored Access Operations |
| `byte_kai` | Kai Osei | Ally — malware analyst and reverse engineer |
| `pr1sm` | Priya Nair | Handler — OSINT specialist and investigative journalist |
| — | Director Harlan Voss | Antagonist — OmniCorp Chief of Cyber Operations |
| `ARIA-v2` | ARIA | Your on-board AI companion and guide |

---

## Building the Executable

```bash
pip install pyinstaller
cd nexus_game
python -m PyInstaller nexus.spec
# Output: dist/NEXUS_ZeroDay.exe
```

Or push a version tag and GitHub Actions builds it automatically:

---

## Project Structure

```
nexus-zero-day/
├── nexus.py                    Entry point
├── nexus.spec                  PyInstaller build configuration
├── LAUNCH_NEXUS.bat            Windows launcher (source runs)
├── launch_nexus.sh             macOS / Linux launcher
├── GITHUB_SETUP.txt            Step-by-step GitHub Desktop publish guide
├── .github/
│   └── workflows/
│       └── build.yml           Auto-build Windows + macOS exe on tag push
└── game/
    ├── engine.py               Game state, save/load, exploit logic
    ├── story.py                All narrative, missions, characters, Codex content
    └── ui/
        ├── main_window.py      Main layout, terminal, commands, toolbar
        ├── terminal.py         Terminal widget with colour tags
        ├── mission_panel.py    Contracts panel with scrollable cards
        ├── network_map.py      Target network map
        ├── dialogue.py         Character transmission popups (typewriter effect)
        ├── edu_panel.py        Single-topic Codex popup
        ├── codex_window.py     Full Codex browser — all 14 topics
        ├── exploit_window.py   Exploit sequence, prep animation, minigames
        ├── minigame.py         Minigame routing controller
        └── help_window.py      In-game help system — 5 tabbed sections
```

---

## Changelog

### v2.0
- **2 new missions** — Ghost in the Binary and Running the Specimen (Chapter 3)
- **Malware reverse engineering** — static analysis (strings, PE headers, YARA) and dynamic analysis (sandbox detonation, ProcMon, IOC extraction)
- **2 new Codex entries** — Malware Static Analysis · Malware Dynamic Analysis, each with real-world case studies (SUNBURST, Emotet)
- **2 new toolkit buttons** — STATIC ANALY · DYNAMIC ANALY
- **2 new targets** — OMNICORP-DB-PRIMARY (malware host) · NEXUS-SANDBOX-VM (analysis environment)
- **3 new items** — Malware Sample, IOC Report, Reverse Engineering Toolkit

### v1.0
- Initial release — 12 missions across 4 chapters
- 12 Codex cybersecurity education entries
- 3 interactive minigames
- Save/load system, fullscreen support, in-game help

---

## Contributing

Pull requests are welcome. Please open an issue first for significant changes.

Good areas to contribute:
- New missions and story chapters
- Additional minigame types
- Linux AppImage packaging
- Accessibility improvements (font scaling, high-contrast mode)
- Additional Codex topics

---

## Disclaimer

NEXUS: Zero Day is an **educational simulation**. All targets, organisations, and individuals are entirely fictional. No real systems are accessed or harmed. The cybersecurity techniques described are real — always practise them legally and ethically, only on systems you own or have explicit written permission to test.

---

## Licence

MIT — see [LICENSE](LICENSE)

---

*"Before you ever touch a target, you understand it completely." — 0xVERA*
