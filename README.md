# NEXUS: Zero Day

**A cybersecurity education simulation — learn real attack and defense techniques through an immersive story.**

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

Ebook coming soon!

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
| Malware Dynamic Analysis — sandboxing, IOC extraction, behavioral logging | Running the Specimen |

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
        ├── terminal.py         Terminal widget with color tags
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

## License

MIT — see [LICENSE](LICENSE)

---

### GLOSSARY:
### Key terms for readers new to cybersecurity

## 0-Day / Zero-Day
A software vulnerability that is unknown to the vendor and therefore has
no patch. Named because defenders have had zero days to prepare a fix.
Zero-days are among the most valuable and dangerous tools in offensive
security.

## Air Gap
A security measure where a computer or network is physically isolated
from the internet and all other networks. Considered one of the most
secure forms of data storage. Air gaps fail most often through human
behavior — someone connecting a USB drive or a backup cable
between the isolated system and a connected one.

## ARP Spoofing
A technique where an attacker sends fake ARP (Address Resolution
Protocol) messages on a local network, associating their own MAC
address with the IP address of another device. This causes traffic meant
for that device to be sent to the attacker instead, enabling a
man-in-the-middle attack.

## ASLR (Address Space Layout Randomization)
A security feature built into modern operating systems that randomizes
the memory locations of key data areas each time a program runs. This
makes it much harder for attackers to exploit buffer overflow
vulnerabilities, because they cannot predict where in memory their
malicious code needs to jump.

## BGP (Border Gateway Protocol)
The routing protocol that directs internet traffic between large networks
worldwide. BGP essentially tells internet traffic which path to take
across the globe. Compromising BGP allows an attacker to redirect
national or international traffic to null routes (making it disappear) or to
attacker-controlled infrastructure.

## Buffer Overflow
A vulnerability where a program writes more data into a memory buffer
than it was designed to hold, overflowing into adjacent memory.
Attackers exploit this to overwrite the program's return address and
redirect execution to malicious code. One of the oldest and most studied
vulnerability classes in computing.

## C2 / C&C; (Command and Control)
The server or infrastructure an attacker uses to communicate with
malware they have deployed on compromised systems. The malware
periodically 'beacons' — checks in with the C2 server for instructions.
Identifying and disrupting C2 infrastructure is a key goal in incident
response.

## CDN (Content Delivery Network)
A geographically distributed network of servers that delivers internet
content (websites, video, software updates) to users from locations
physically close to them, making delivery faster. In the story, OmniCorp
hides the LAZARUS shadow network inside legitimate CDN
infrastructure.

## Certificate Authority (CA)
An organization that issues digital certificates, which are used to verify
that a website or server is who it claims to be. Your browser comes
pre-loaded with a list of trusted CAs. If a CA is compromised, attackers
can issue fraudulent certificates for any website, enabling
man-in-the-middle attacks on encrypted traffic.

## Credential Harvesting
The process of stealing usernames and passwords, either through
phishing, malware that captures keystrokes or saved passwords, or by
extracting credentials from compromised databases. Harvested
credentials are often used to access other systems, especially if the
victim reuses passwords.

## CVE (Common Vulnerabilities and Exposures)
A publicly maintained database of known security vulnerabilities, each
given a unique identifier (e.g. CVE-2021-3156). When a vulnerability is
discovered and disclosed responsibly, it receives a CVE number,
allowing security teams worldwide to track and patch it.

## DNS (Domain Name System)
The internet's address book. DNS translates human-readable domain
names (like google.com) into IP addresses that computers use to find
each other. Corrupting DNS responses allows an attacker to redirect
users to fake websites or, as with LAZARUS, make websites appear not
to exist at all.

## Dynamic Analysis
A method of analyzing malware by actually running it in a controlled,
isolated environment (a sandbox) and observing what it does — what
files it creates, what network connections it makes, what registry keys it
writes. Contrasted with static analysis, which examines the code without
running it.

## EDR (Endpoint Detection and Response)
Security software installed on individual computers (endpoints) that
monitors for suspicious behavior in real time and can respond
automatically. In the story, the NEXUS rootkit operates at kernel level
specifically to be invisible to OmniCorp's EDR, which runs in user
space.

## Exploit
A piece of code or a technique that takes advantage of a vulnerability to
cause unintended behavior in a system — typically gaining
unauthorized access, executing code, or escalating privileges. An exploit
is the practical weapon; the vulnerability is the weakness it targets.

## FTP (File Transfer Protocol)
An older protocol for transferring files between computers over a
network. Anonymous FTP allows anyone to connect and download files
without a username or password. Once a common feature, it is now
considered a security risk and should be disabled on any system that
doesn't specifically need it.

## HSM (Hardware Security Module)
A dedicated physical device that stores and manages cryptographic keys
and performs encryption operations. HSMs are designed to be
tamper-resistant — the keys inside cannot be extracted even if the
device is physically seized. In the story, the HSM itself is unbreakable,
but the software around it has a race condition.

## IOC (Indicator of Compromise)
Evidence that a system has been compromised. IOCs include things like
the IP addresses a piece of malware connects to, file hashes, registry
keys it creates, or unusual process names. Sharing IOCs between
organizations allows defenders to detect the same threat across many
different networks.

## Kernel
The core of an operating system — the software that manages
everything else, including hardware, memory, and running programs.
Code running at the kernel level has the highest possible privileges and
can control or hide anything on the system. A kernel-level rootkit is
extremely difficult to detect from within the operating system.

## Lateral Movement
The process of moving from one compromised system to other systems
on the same network, expanding access. An attacker who gains a
foothold on one server will use lateral movement techniques to reach
other, more valuable systems — like moving from a public-facing web
server to an internal database.

## LKM (Loadable Kernel Module)
A piece of code that can be dynamically loaded into and unloaded from
a running Linux kernel without rebooting. Legitimate uses include
device drivers. Malicious uses include rootkits that hook system calls to
hide attacker activity, as in the story's Chapter Nine.

## Man-in-the-Middle (MITM)
An attack where the attacker secretly intercepts and potentially alters
communications between two parties who believe they are
communicating directly with each other. In the story, NEXUS positions
itself between OmniCorp's CDN node and its clients, reading encrypted
traffic because the node doesn't properly validate certificates.

## Mutex (Mutual Exclusion)
A programming mechanism that prevents the same program from
running more than one instance simultaneously. Malware often creates a
mutex with a unique name on startup — if the mutex already exists, it
knows it's already running and exits. This also serves as an IOC: the
mutex name lazarus_active_v4 in the story immediately reveals the
malware's origin.

## NDA (Non-Disclosure Agreement)
A legal contract requiring one or more parties to keep specified
information confidential. In the story, OmniCorp uses a broadly-written
NDA to silence Alex after he files a whistleblower report, preventing
him from going to the press with what he knows.

## OSINT (Open Source Intelligence)
Intelligence gathered entirely from publicly available sources — social
media, news articles, company websites, corporate filings, domain
registration records, public databases, and more. Priya's specialty. No
hacking required; OSINT can build a surprisingly complete picture of a
target from information they have already made public.

## PE Header (Portable Executable)
The standard file format for executable programs on Windows (.exe and
.dll files). The PE header contains metadata about the file — including
its import table (which Windows API functions it uses), section names
and their entropy levels, and a compilation timestamp. Analyzing the PE
header is an early step in malware reverse engineering.

## Penetration Testing (Pen Test)
An authorized simulated attack on a computer system, performed to
evaluate its security. Ethical hackers (pen testers) use the same
techniques as malicious attackers but with explicit permission. The
difference between a pen tester and a criminal is entirely the piece of
paper that authorizes the engagement.

## Phishing / Spear Phishing
Phishing is sending deceptive emails designed to trick recipients into
revealing credentials or clicking malicious links. Spear phishing is
targeted phishing — the email is tailored to a specific individual using
personal details gathered through OSINT, making it far more
convincing and far more likely to succeed.

## Port Scanning
Sending network probes to a target to discover which ports are open and
what services are running on them. Every open port is a potential entry
point. Service banners — the responses servers send when contacted —
reveal software versions that can be matched against known vulnerabilities.

## Privilege Escalation
The process of gaining higher-level access than originally obtained. An
attacker who initially accesses a system as a low-privilege user will
attempt to escalate to administrator or root, gaining full control. Many
exploits specifically target privilege escalation vulnerabilities.

## Race Condition
A flaw where the outcome of a program depends on the timing or
sequence of events, and an attacker can manipulate that timing to cause
unintended behavior. The classic example: a program checks a
condition is safe, then uses it — but an attacker changes it in the gap
between the check and the use. In the story, this gap is 187 nanoseconds
in the LAZARUS authentication server.

## Reconnaissance (Recon)
The first phase of any operation — gathering information about a target
before engaging it. Reconnaissance can be passive (using OSINT,
observing without interacting) or active (port scanning, banner
grabbing). Vera's rule: reconnaissance is 80% of the work.

## Rootkit
Malware designed to hide itself and other malicious software from the
operating system and security tools. A kernel-level rootkit loads into the
kernel itself and can intercept and modify the results of system calls —
making its files, processes, and network connections invisible to any
tool that queries the OS through normal channels.

## Sandbox
An isolated environment where potentially malicious code can be safely
executed and observed without risk to the surrounding system. In
dynamic malware analysis, the sandbox records everything the malware
does. Sophisticated malware may check whether it's running in a
sandbox and behave differently — or not run at all — to avoid analysis.

## SEC (Securities and Exchange Commission)
The United States federal agency responsible for regulating financial
markets and protecting investors. The SEC operates a whistleblower
program that allows people to confidentially report corporate fraud
and securities violations. In the story, Alex submits his report to the
SEC, which acknowledges it and never follows up.

## Shellcode
Small, self-contained machine code designed to be injected into a
vulnerable process and executed. The term comes from the early goal of
shellcode: spawning a command shell on the target. Modern shellcode
can do far more — download payloads, add users, establish backdoors.

## SQL Injection
A vulnerability where user-supplied input is inserted directly into a
database query without sanitization. By including SQL syntax in the
input, an attacker can manipulate the query to return all data, bypass
authentication, or delete records. Preventable with parameterized queries
— two lines of code that separate data from instructions. Has been on
the OWASP Top Ten since 2003.

## SSO (Single Sign-On)
An authentication system that allows a user to log in once and gain
access to multiple applications without logging in again for each one.
Widely used in corporate environments. If an SSO credential is stolen
through phishing, the attacker gains access to every system the victim is
authorized to use.

## Static Analysis
Examining a file — typically malware — without executing it.
Techniques include strings extraction (finding readable text embedded
in the binary), PE header analysis, import table review, and entropy
measurement. Static analysis is safe — the malware cannot run or phone
home — but reveals less than dynamic analysis, which actually executes
the code.

## TLS (Transport Layer Security)
The protocol that encrypts internet traffic. When you see HTTPS in your
browser, TLS is what's making it secure. TLS works by establishing an
encrypted connection verified by digital certificates. TLS is only as
secure as the certificate validation — if a system accepts any certificate
without checking the chain of trust, a man-in-the-middle attack becomes
straightforward.

## Vulnerability
A weakness in software, hardware, or human behavior that can be
exploited by an attacker to cause unintended behavior. Vulnerabilities
range from coding errors (buffer overflows, SQL injection) to
configuration mistakes (default credentials, anonymous FTP) to design
flaws (race conditions, missing certificate validation).

## YARA
A pattern-matching language used in malware analysis and threat
hunting. Security researchers write YARA rules to describe
characteristics of a piece of malware — specific byte sequences, strings,
or combinations of features. These rules can then scan millions of files
to identify the same malware family, even after modifications. YARA
rules are widely shared between security organizations.

*"Before you ever touch a target, you understand it completely." — 0xVERA*
