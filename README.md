# NEXUS: Zero Day

**A cybersecurity education simulation — learn real attack and defence techniques through an immersive story.**

![Build Status](https://github.com/hawaiizfynest/nexus_zero_day/actions/workflows/build.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-3.0-brightgreen)

---

## What is this?

You are **Alex Ryder** — handle: `gh0st`. Former network engineer turned hacktivist.

Veteran hacker **Vera Kaine** (ex-NSA) has recruited you to investigate **PROJECT LAZARUS** — a hidden internet kill-switch embedded inside global CDN infrastructure, built by the defence contractor that destroyed your career.

But stopping LAZARUS is only the beginning. When the story goes public, the man behind it doesn't disappear quietly — and suddenly NEXUS is the target.

NEXUS: Zero Day is a desktop hacking simulation inspired by *Uplink*. Every mission teaches a real cybersecurity technique — from port scanning and SQL injection through malware reverse engineering, digital forensics, and operational security.

---

## Features

| | |
|---|---|
| **Story** | 5 chapters + epilogue, 18 missions, 6 characters with typewriter dialogue |
| **Techniques** | Offensive and defensive — see full list below |
| **Minigames** | Port Mapper · Cipher Decoder · Firewall Bypass |
| **Codex** | 18 cybersecurity education entries with real-world breach case studies |
| **Help system** | Tabbed in-game guide — Getting Started, Interface, Walkthrough, Commands, Tips |
| **Save / Load** | 3 save slots stored in `~/Documents/NEXUS_ZeroDay/saves/` |
| **Fullscreen** | F11 to toggle, fully responsive layout |
| **No dependencies** | Pure Python standard library + tkinter |

---

## Download & Run

### Easiest — grab the executable

Go to [**Releases**](https://github.com/hawaiizfynest/nexus_zero_day/releases/latest):

| Platform | File |
|----------|------|
| **Windows** | `NEXUS_ZeroDay.exe` — double-click, no install needed |
| **macOS** | `NEXUS_ZeroDay_macOS.zip` — unzip and run |

### Run from source

```bash
git clone https://github.com/hawaiizfynest/nexus_zero_day.git
cd nexus-zero-day
python3 nexus.py
```

**Linux:** `sudo apt install python3-tk && python3 nexus.py`
**macOS (if tkinter missing):** `brew install python-tk && python3 nexus.py`

---

## Story & Missions

| Chapter | Title | Missions |
|---------|-------|---------|
| **1** | First Contact | Ghost in the Wire · Default Sins · Injection Season |
| **2** | The Network Beneath | Man in the Middle · Buffer Overflow Blues · Phishing Season · Packet Archaeology |
| **3** | Ghost Protocol | Rootkit · The Counter-Hunt · The Architecture · Ghost in the Binary · Running the Specimen |
| **4** | Zero Day | Zero Day · The Kill Switch · Dead Man's Switch |
| **5** | The Reckoning | Ghost Signal · The Tallinn Connection · Cover Your Tracks |

---

## Cybersecurity Techniques

### Offensive
| Technique | Mission |
|-----------|---------|
| Port Scanning & Reconnaissance | Ghost in the Wire |
| Default & Weak Credentials | Default Sins |
| SQL Injection | Injection Season |
| Man-in-the-Middle & TLS | Man in the Middle |
| Buffer Overflow | Buffer Overflow Blues |
| Phishing & Social Engineering | Phishing Season |
| Rootkits & Kernel Persistence | Rootkit |
| Command & Control Infrastructure | The Counter-Hunt |
| Lateral Movement & Air Gaps | The Architecture |
| Zero-Day Exploitation | Zero Day |
| Race Conditions & Timing Attacks | The Kill Switch |
| PKI & Certificate Trust Abuse | Dead Man's Switch |

### Defensive
| Technique | Mission |
|-----------|---------|
| Malware Static Analysis | Ghost in the Binary |
| Malware Dynamic Analysis | Running the Specimen |
| Network Forensics | Packet Archaeology |
| Incident Response | Ghost Signal |
| Digital Forensics & Legal Evidence | The Tallinn Connection |
| Operational Security (OPSEC) | Cover Your Tracks |

---

## Changelog

### v3.0
- **New chapter** — Chapter 5: The Reckoning. Voss didn't disappear. He came back.
- **4 new missions** — Packet Archaeology (Ch2), Ghost Signal, The Tallinn Connection, Cover Your Tracks (Ch5)
- **4 new Codex entries** — Network Forensics · Incident Response · Digital Forensics & Evidence · OPSEC
- **3 new targets** — Traffic archive, compromised NEXUS relay, Voss's personal server
- **4 new items** — Forensic evidence packages, NEXUS infrastructure hardening
- Updated epilogue — Voss is found and arrested through NEXUS's own forensic work

### v2.0
- 2 new missions — Ghost in the Binary, Running the Specimen (malware reverse engineering)
- 2 new Codex entries — Malware Static Analysis · Malware Dynamic Analysis
- 2 new toolkit buttons — STATIC ANALY · DYNAMIC ANALY

### v1.0
- Initial release — 12 missions, 12 Codex entries, 3 minigames, save/load, fullscreen, in-game help

---

## Building the Executable

```bash
pip install pyinstaller
cd nexus_game
python -m PyInstaller nexus.spec
```

---

## Licence

MIT — see [LICENSE](LICENSE)

*"Before you ever touch a target, you understand it completely." — 0xVERA*
