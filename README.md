# NEXUS: Zero Day

**A cybersecurity education simulation — learn real attack and defence techniques through an immersive story.**

![Build Status](https://github.com/HawaiizFynest/nexus_zero_day/actions/workflows/build.yml/badge.svg)
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
| **Techniques** | 18 cybersecurity topics — offensive and defensive |
| **Minigames** | Port Mapper · Cipher Decoder · Firewall Bypass |
| **Codex** | 18 in-depth education entries with real-world breach case studies |
| **Help system** | Tabbed in-game guide — Getting Started, Interface, Walkthrough, Commands, Tips |
| **Save / Load** | 3 save slots stored in `~/Documents/NEXUS_ZeroDay/saves/` |
| **Fullscreen** | F11 to toggle, fully responsive layout |
| **No dependencies** | Pure Python standard library + tkinter — nothing to install |

---

## Download & Run

### Easiest — grab the executable

Go to [**Releases**](https://github.com/HawaiizFynest/nexus_zero_day/releases/latest):

| Platform | File |
|----------|------|
| **Windows** | `NEXUS_ZeroDay.exe` — double-click, no install needed |
| **macOS** | `NEXUS_ZeroDay_macOS.zip` — unzip and run |

### Run from source

Requires **Python 3.8+** with tkinter (included in standard Python installers).

```bash
git clone https://github.com/HawaiizFynest/nexus_zero_day.git
cd nexus_zero_day
python3 nexus.py
```

**Linux:** `sudo apt install python3-tk && python3 nexus.py`

**macOS (if tkinter missing):** `brew install python-tk && python3 nexus.py`

---

## How to Play

1. **Accept a contract** — click a mission card in the right panel, or type `missions` → `accept 1`
2. **Scan your target** — type `scan` or click PORT SCAN in the left toolkit
3. **Complete the minigame** — your performance boosts exploit success rate
4. **Execute the exploit** — click EXECUTE EXPLOIT in the exploit window
5. **Watch your trace** — type `bounce` to reduce trace generation by 70%
6. **Read the Codex** — after each mission, learn the real technique behind what you did (+2 REP)
7. **Save often** — SAVE button in the top bar, or type `save`

**F11** = fullscreen · **HELP** button = full in-game guide · **↑/↓** = command history · **Tab** = autocomplete

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

## Glossary

Quick reference for cybersecurity terms used in the game. The full in-game **Codex** covers each topic in depth with real-world case studies.

| Term | Definition |
|------|-----------|
| **0-Day / Zero-Day** | A vulnerability unknown to the vendor — no patch exists. Named because defenders have had zero days to prepare. |
| **Air Gap** | A system physically isolated from all networks. Fails most often through human behaviour — someone connecting a USB drive or backup cable. |
| **ARP Spoofing** | Sending fake ARP messages on a local network to redirect traffic through the attacker, enabling man-in-the-middle attacks. |
| **ASLR** | Address Space Layout Randomisation — randomises memory locations each run, making buffer overflow exploitation much harder. |
| **BGP** | Border Gateway Protocol — routes internet traffic between networks worldwide. Compromising it can redirect or kill traffic for entire countries. |
| **Buffer Overflow** | Writing more data into a memory buffer than it can hold, overwriting adjacent memory. Used to redirect program execution to malicious code. |
| **C2 / C&C** | Command and Control — the infrastructure attackers use to communicate with deployed malware. Malware periodically "beacons" home for instructions. |
| **CDN** | Content Delivery Network — distributed servers delivering web content. LAZARUS hides its shadow network inside legitimate CDN infrastructure. |
| **Certificate Authority (CA)** | Issues digital certificates that verify server identity. One compromised CA can undermine trust in every certificate it has ever signed. |
| **Chain of Custody** | The documented, unbroken record of who has had possession of evidence from collection to court. A gap allows defence lawyers to challenge admissibility. |
| **Credential Harvesting** | Stealing usernames and passwords via phishing, malware, or database breaches. Often enables access to many other systems if passwords are reused. |
| **CVE** | Common Vulnerabilities and Exposures — a public database of known vulnerabilities each given a unique identifier (e.g. CVE-2021-3156). |
| **DNS** | Domain Name System — the internet's address book. Corrupting DNS responses can redirect users or make services appear unreachable. |
| **Dynamic Analysis** | Running malware in an isolated sandbox and observing its real-time behaviour — files created, network connections, registry changes. |
| **EDR** | Endpoint Detection and Response — security software monitoring individual computers for suspicious behaviour. Kernel rootkits operate below its visibility. |
| **Exploit** | Code or technique that takes advantage of a vulnerability to gain unauthorised access or execute malicious code. |
| **FTP** | File Transfer Protocol. Anonymous FTP allows connections without a password — a security risk that should be disabled on production systems. |
| **HSM** | Hardware Security Module — a tamper-resistant device storing cryptographic keys. The keys cannot be extracted even if the device is physically seized. |
| **Incident Response (IR)** | The structured process for handling a breach: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned. |
| **IOC** | Indicator of Compromise — evidence of a breach (IP addresses, file hashes, registry keys). Shared between organisations to detect the same threat. |
| **Kernel** | The core of an operating system with the highest system privileges. Kernel-level rootkits can hide anything from tools that run at lower privilege levels. |
| **Lateral Movement** | Moving from one compromised system to others on the same network to reach more valuable targets. |
| **LKM** | Loadable Kernel Module — code loaded into a running Linux kernel. Legitimate uses include device drivers; malicious uses include rootkits. |
| **Man-in-the-Middle (MITM)** | Intercepting communications between two parties who believe they are talking directly to each other. |
| **MITRE ATT&CK** | A framework cataloguing real-world attacker tactics and techniques, organised by attack phase. Used to map incidents and predict attacker behaviour. |
| **Mutex** | A programming mechanism preventing a program running twice simultaneously. Malware uses mutex names as a fingerprint — lazarus_active_v4 identified the implant's origin. |
| **NDA** | Non-Disclosure Agreement — a legal contract requiring confidentiality. Used in the story to silence a whistleblower through legal threat. |
| **Network Forensics** | Extracting legal-grade evidence from network traffic captures. Requires SHA-256 hashing every PCAP file and verifying timestamps against NTP logs for court admissibility. |
| **OPSEC** | Operational Security — protecting information that could be used against you. Failures are almost always small and mundane: a timestamp, a reused username, a consistent timezone. |
| **OSINT** | Open Source Intelligence — building intelligence from publicly available information. No hacking required; social media, filings, and domain records can be devastating. |
| **PCAP** | Packet Capture — a file storing raw network traffic. The primary data source for network forensics. Analysed with tools like Wireshark. |
| **PE Header** | The metadata structure of Windows executables. Reveals imported API functions, section entropy (packed = likely malware), and compilation timestamps. |
| **Penetration Testing** | An authorised simulated attack to evaluate security. The difference between a pen tester and a criminal is the signed permission document. |
| **Phishing / Spear Phishing** | Deceptive emails stealing credentials or delivering malware. Spear phishing is targeted using personal details — far more effective than generic phishing. |
| **Port Scanning** | Probing a target to discover open ports and running services. Every open port is a potential entry point; version banners reveal patchable vulnerabilities. |
| **Race Condition** | A flaw where an attacker can insert a malicious action in the gap between a security check and the system acting on it. 187 nanoseconds was enough. |
| **Reconnaissance** | The first phase of any operation — gathering intelligence before engaging. Vera's rule: reconnaissance is eighty percent of the work. |
| **Rootkit** | Malware that hides itself from the OS and security tools. A kernel-level rootkit intercepts system calls, making its presence invisible. |
| **Sandbox** | An isolated environment for safely executing and observing malware. Sophisticated malware checks for sandbox indicators and may refuse to run. |
| **SQL Injection** | Inserting SQL syntax into an input field to manipulate database queries. Preventable with two lines of code. On the OWASP Top Ten since 2003. |
| **SSO** | Single Sign-On — one login granting access to many systems. A stolen SSO credential opens every door the victim was authorised to use. |
| **Static Analysis** | Examining a binary without executing it — strings, PE headers, import tables. Safe, but reveals less than dynamic analysis. |
| **TLS** | Transport Layer Security — encrypts internet traffic. Only as secure as the certificate validation; a node accepting any certificate is trivially intercepted. |
| **Vulnerability** | A weakness in software, hardware, or human behaviour that can be exploited. Ranges from coding errors to configuration mistakes to design flaws. |
| **YARA** | A pattern-matching language for identifying malware families by unique byte sequences or strings. Rules are widely shared between security organisations. |

---

## Project Structure

```
nexus_zero_day/
├── nexus.py                    Entry point
├── nexus.spec                  PyInstaller build configuration
├── LAUNCH_NEXUS.bat            Windows launcher
├── launch_nexus.sh             macOS / Linux launcher
├── .github/
│   └── workflows/
│       └── build.yml           Auto-build Windows + macOS exe on tag push
└── game/
    ├── engine.py               Game state, save/load, exploit logic
    ├── story.py                All narrative, missions, characters, Codex
    └── ui/
        ├── main_window.py      Main layout, terminal, commands
        ├── terminal.py         Terminal widget
        ├── mission_panel.py    Contracts panel
        ├── network_map.py      Target network map
        ├── dialogue.py         Character transmission popups
        ├── edu_panel.py        Single-topic Codex popup
        ├── codex_window.py     Full Codex browser
        ├── exploit_window.py   Exploit sequence + minigames
        ├── minigame.py         Minigame routing
        └── help_window.py      In-game help system
```

---

## Changelog

### v3.0
- **New chapter** — Chapter 5: The Reckoning. Voss comes back. NEXUS becomes the target.
- **4 new missions** — Packet Archaeology (Ch2), Ghost Signal, The Tallinn Connection, Cover Your Tracks (Ch5)
- **4 new Codex entries** — Network Forensics · Incident Response · Digital Forensics & Evidence · OPSEC
- **3 new targets** — Traffic archive, compromised NEXUS relay, Voss's personal server in Tallinn
- **Updated epilogue** — Voss arrested at Tallinn Airport; caught by his own evidence

### v2.0
- 2 new missions — Ghost in the Binary · Running the Specimen (malware reverse engineering)
- 2 new Codex entries — Malware Static Analysis · Malware Dynamic Analysis

### v1.0
- Initial release — 12 missions, 12 Codex entries, 3 minigames, save/load, fullscreen, in-game help

---

## Building the Executable

```bash
pip install pyinstaller
cd nexus_zero_day
python -m PyInstaller nexus.spec
```

---

## Disclaimer

NEXUS: Zero Day is an **educational simulation**. All targets, organisations, and individuals are fictional. The cybersecurity techniques described are real — always apply them legally and ethically, only on systems you own or have explicit written permission to test.

---

## Licence

MIT — see [LICENSE](LICENSE)

*"Before you ever touch a target, you understand it completely." — 0xVERA*
