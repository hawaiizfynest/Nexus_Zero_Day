"""
NEXUS: Zero Day — In-Game Help System
A tabbed help window covering getting started, the interface,
mission walkthrough, command reference, and tips.
"""

import tkinter as tk
from tkinter import font as tkfont

C = {
    "bg":        "#080c0a",
    "bg2":       "#0d1410",
    "bg3":       "#111a16",
    "green":     "#00ff88",
    "green_dim": "#00aa55",
    "green_dk":  "#003322",
    "amber":     "#ffaa00",
    "red":       "#ff3344",
    "cyan":      "#00ccff",
    "purple":    "#cc44ff",
    "text":      "#c0e8d0",
    "text_dim":  "#4a7a5a",
    "border":    "#1a3328",
}

# ── Content for every tab ──────────────────────────────────────────────────

SECTIONS = {
    "GETTING STARTED": [
        ("WELCOME TO NEXUS", "cyan", None),
        ("", None, None),
        ("You are Alex Ryder — handle: gh0st. Former network engineer, now hacktivist.", None, None),
        ("Vera Kaine (0xVERA), ex-NSA operative, has recruited you to expose PROJECT LAZARUS —", None, None),
        ("a corporate internet kill-switch hidden inside global CDN infrastructure.", None, None),
        ("", None, None),
        ("Your first target is a low-security MediaBridge relay node. Prove you can", None, None),
        ("operate cleanly, and the real work begins.", None, None),
        ("", None, None),
        ("── STEP 1 — Accept a Contract ─────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Three contracts are waiting in the RIGHT PANEL →", None, None),
        ("Click any mission card to accept it, or type in the terminal:", None, None),
        ("", None, None),
        ("    missions", "green", None),
        ("    accept 1", "green", None),
        ("", None, None),
        ("── STEP 2 — Scan Your Target ──────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Always recon before you attack. A port scan reveals open services and", None, None),
        ("version numbers that map directly to known vulnerabilities.", None, None),
        ("", None, None),
        ("    scan          (or click PORT SCAN in the left toolkit)", "green", None),
        ("", None, None),
        ("── STEP 3 — Run the Minigame ──────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Every exploit launches a minigame. Your performance gives a success bonus.", None, None),
        ("Complete it for the best odds, or click SKIP MINIGAME for base probability.", None, None),
        ("", None, None),
        ("── STEP 4 — Execute & Exfiltrate ──────────────────────────────────────", "green", None),
        ("", None, None),
        ("After the minigame, click EXECUTE EXPLOIT. If successful, you gain shell", None, None),
        ("access (whoami → root). Run the remaining mission steps — the mission panel", None, None),
        ("tracks your progress. Complete all steps to finish the contract.", None, None),
        ("", None, None),
        ("── STEP 5 — Manage Your Trace ─────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Every action raises your TRACE %. Hit 100% and you are BUSTED.", None, None),
        ("    bounce       — activates proxy routing, cuts trace generation 70%", "amber", None),
        ("    LOG WIPE     — shreds logs on a compromised host, -20% trace", "amber", None),
        ("", None, None),
        ("── STEP 6 — Save Often ─────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Progress is not automatic. Click SAVE in the top bar or type:  save", None, None),
    ],

    "THE INTERFACE": [
        ("INTERFACE OVERVIEW", "cyan", None),
        ("", None, None),
        ("The game window is divided into five areas:", None, None),
        ("", None, None),
        ("── LEFT PANEL ──────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("NETWORK MAP   Lists every target you have discovered.", None, None),
        ("              Click a target to select it — it highlights green.", None, None),
        ("              The TARGET INTEL panel updates to show its details.", None, None),
        ("", None, None),
        ("TOOLKIT       12 exploit buttons below the map.", None, None),
        ("              Clicking one runs that exploit against the selected target", None, None),
        ("              and launches the minigame.", None, None),
        ("", None, None),
        ("── CENTRE PANEL ────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("TERMINAL      Your primary interface. Type commands here.", None, None),
        ("              Full command list: type  help  in the terminal.", None, None),
        ("", None, None),
        ("TAB BAR       Switch the centre panel between views:", None, None),
        ("  TERMINAL    Live terminal and command input", None, None),
        ("  STORY       Current chapter narrative and progress", None, None),
        ("  INTEL       Full intelligence report on the active target", None, None),
        ("  FILES       File system of a compromised target (needs shell)", None, None),
        ("  LOGS        Full operation log for the session", None, None),
        ("", None, None),
        ("── RIGHT PANEL ─────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("ACTIVE CONTRACTS   Shows available and active missions.", None, None),
        ("                   Click a card to accept. Active mission glows green.", None, None),
        ("", None, None),
        ("TARGET INTEL       IP, OS, ports, security level, and known", None, None),
        ("                   vulnerabilities for the currently selected target.", None, None),
        ("                   Shows ROOT ACCESS badge when you own a shell.", None, None),
        ("", None, None),
        ("── TOP BAR ─────────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("TIME       How long you have been playing this session", None, None),
        ("CREDITS    In-game currency earned from missions", None, None),
        ("REP        Reputation — increases with missions and Codex entries", None, None),
        ("SHELLS     Number of targets where you have root access", None, None),
        ("TRACE      Risk meter — keep this below 50%. Red at 70%, BUST at 100%.", None, None),
        ("", None, None),
        ("Buttons:   SAVE · LOAD · CODEX · HELP · F11 (fullscreen) · QUIT", None, None),
        ("", None, None),
        ("── KEYBOARD SHORTCUTS ──────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("F11          Toggle fullscreen", None, None),
        ("Escape       Exit fullscreen", None, None),
        ("↑ / ↓        Scroll through terminal command history", None, None),
        ("Tab          Autocomplete a command", None, None),
        ("Enter        Execute current command", None, None),
    ],

    "MISSION WALKTHROUGH": [
        ("GHOST IN THE WIRE  —  Opening Mission", "cyan", None),
        ("Target: MEDIABRIDGE-RELAY-01  [10.44.12.8]  Security: LOW", "text_dim", None),
        ("Objective: Reconnaissance and config exfiltration", "text_dim", None),
        ("Reward: +10 REP  •  Proxy Chain v1 item", "amber", None),
        ("", None, None),
        ("Vera: \"If you can't do the boring work cleanly,", "text_dim", None),
        ("you'll die on the exciting work.\"", "text_dim", None),
        ("", None, None),
        ("── STEP 1  Accept the contract ─────────────────────────────────────────", "green", None),
        ("Click the Ghost in the Wire card in the right contracts panel,", None, None),
        ("or type:   missions   then   accept 1", None, None),
        ("The terminal confirms acceptance and sets the target automatically.", None, None),
        ("", None, None),
        ("── STEP 2  Port scan ───────────────────────────────────────────────────", "green", None),
        ("Type:  scan   or click PORT SCAN in the toolkit.", None, None),
        ("", None, None),
        ("MINIGAME — Port Mapper:", None, None),
        ("A grid of port numbers appears. Five are OPEN (SYN/ACK response),", None, None),
        ("the rest are CLOSED (RST). Click all five open ports before time runs out.", None, None),
        ("Common open ports on this target: 21 (FTP), 22 (SSH), 80 (HTTP), 8080.", None, None),
        ("", None, None),
        ("Result: 4 open ports confirmed, OS fingerprinted, service banners grabbed.", None, None),
        ("", None, None),
        ("── STEP 3  Review intel ────────────────────────────────────────────────", "green", None),
        ("Click the INTEL tab or type:  intel", None, None),
        ("Key findings: Anonymous FTP enabled (no credentials needed on port 21),", None, None),
        ("outdated Apache Tomcat on 8080, sudo heap overflow (CVE-2021-3156).", None, None),
        ("", None, None),
        ("── STEP 4  Connect to the target ───────────────────────────────────────", "green", None),
        ("    connect 10.44.12.8", "green", None),
        ("Your prompt changes to  gh0st@10:~$  confirming the connection.", None, None),
        ("Explore with:  whoami  •  ps  •  netstat  •  ls", None, None),
        ("", None, None),
        ("── STEP 5  Gain shell access ────────────────────────────────────────────", "green", None),
        ("Click BRUTE FORCE in the toolkit (exploits the anonymous FTP credential).", None, None),
        ("", None, None),
        ("MINIGAME — Cipher Decoder:", None, None),
        ("Four rounds. Each shows a Caesar-shifted encoded word.", None, None),
        ("Click the correctly decoded option from four choices.", None, None),
        ("Example: shift +3 turns  admin  into  dgplq.", None, None),
        ("", None, None),
        ("Success: prompt changes to  gh0st@10:~#  (# = root). ROOT ACCESS badge", None, None),
        ("appears in the Target Intel panel.", None, None),
        ("", None, None),
        ("── STEP 6  Exfiltrate the config ───────────────────────────────────────", "green", None),
        ("    exploit exfil", "green", None),
        ("Or click the EXFIL step in the active mission panel.", None, None),
        ("The server config and routing table are pulled to the NEXUS drop server.", None, None),
        ("", None, None),
        ("── MISSION COMPLETE ────────────────────────────────────────────────────", "cyan", None),
        ("The terminal prints the completion banner and Vera delivers the debrief.", None, None),
        ("ARIA will then offer to open the Codex for Port Scanning (+2 REP).", None, None),
        ("", None, None),
        ("── WHAT COMES NEXT ─────────────────────────────────────────────────────", "green", None),
        ("Default Sins     — exploit admin/admin123 credentials, plant implant", None, None),
        ("Injection Season — extract LAZARUS routing data via SQL injection", None, None),
        ("Complete all three to advance to Chapter 2: The Network Beneath.", None, None),
    ],

    "COMMANDS": [
        ("TERMINAL COMMAND REFERENCE", "cyan", None),
        ("", None, None),
        ("── NAVIGATION ──────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("help              Show this command list in the terminal", None, None),
        ("connect <ip>      Connect to a target by IP address", None, None),
        ("disconnect        Return to localhost", None, None),
        ("clear  /  cls     Clear the terminal output", None, None),
        ("history           Show your last 20 commands", None, None),
        ("", None, None),
        ("── RECONNAISSANCE ──────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("scan  /  nmap     Port scan the current target", None, None),
        ("recon             OSINT reconnaissance — low trace, high info", None, None),
        ("intel             Switch to target intelligence tab", None, None),
        ("whoami            Current user on target (nobody / root)", None, None),
        ("ps                List running processes", None, None),
        ("netstat           Show active network connections", None, None),
        ("ls  /  dir        List files on the target (requires shell)", None, None),
        ("cat <file>        Read a file on the target (requires shell)", None, None),
        ("ifconfig          Show network interfaces and bounce status", None, None),
        ("", None, None),
        ("── MISSIONS ────────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("missions          List available contracts in the current chapter", None, None),
        ("accept <N>        Accept mission number N from the list", None, None),
        ("status            Full player stats — credits, rep, trace, shells", None, None),
        ("inventory         List items you have collected", None, None),
        ("credits           Show current credit balance", None, None),
        ("", None, None),
        ("── EXPLOITS ────────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("exploit <tool>    Run a named exploit, e.g:  exploit bruteforce", None, None),
        ("hack              Alias for bruteforce", None, None),
        ("recon             OSINT on current target", None, None),
        ("", None, None),
        ("  Available exploit names:", "text_dim", None),
        ("  portscan  •  bruteforce  •  sqlinject  •  overflow  •  sshcrack", "text_dim", None),
        ("  mitm  •  implant  •  lkm_compile  •  craft_phish  •  exfil", "text_dim", None),
        ("  zeroday_prep  •  ipc_corrupt  •  race_exploit  •  forge_cert", "text_dim", None),
        ("", None, None),
        ("── TRACE & STEALTH ─────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("trace             Show trace level with contextual advice", None, None),
        ("bounce            Activate 3-hop proxy routing (trace gen -70%)", None, None),
        ("                  Also activates via the BOUNCE toolkit button", None, None),
        ("", None, None),
        ("  LOG WIPE button — shreds event logs on the target (-20% trace)", "amber", None),
        ("                    Requires active shell access first", "amber", None),
        ("", None, None),
        ("── VIEWS & INFORMATION ─────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("story             Switch to chapter narrative and progress view", None, None),
        ("logs              Switch to operation log view", None, None),
        ("intel             Switch to target intelligence view", None, None),
        ("codex             Open the cybersecurity knowledge base", None, None),
        ("", None, None),
        ("── GAME MANAGEMENT ─────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("save              Open save menu (3 slots)", None, None),
        ("load              Open load menu", None, None),
        ("restart           Reset current run (after being BUSTED)", None, None),
    ],

    "TIPS & CODEX": [
        ("TIPS FOR EFFECTIVE OPERATIONS", "cyan", None),
        ("", None, None),
        ("── GENERAL ─────────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Always scan before you attack. The intel tab shows exact vulnerability", None, None),
        ("names — these hint at which exploit to use.", None, None),
        ("", None, None),
        ("Activate BOUNCE early. It costs nothing and passively decays trace", None, None),
        ("over time while active. Run it at the start of every session.", None, None),
        ("", None, None),
        ("Higher minigame scores = higher exploit success rates. A perfect Port", None, None),
        ("Mapper run can push a 50% base chance up to near 80%.", None, None),
        ("", None, None),
        ("Failed exploits generate double trace. If a target feels too hard,", None, None),
        ("check your inventory — you may have an item that boosts that exploit.", None, None),
        ("", None, None),
        ("── TRACE MANAGEMENT ────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("  0–30%    Safe. Operate normally.", "green", None),
        ("  30–60%   Elevated. Activate bounce if you haven't already.", "amber", None),
        ("  60–80%   Danger. Run LOG WIPE on any shell you own.", "amber", None),
        ("  80–99%   Critical. Stop exploiting. Wipe logs, wait for decay.", "red", None),
        ("  100%     BUSTED. Type  restart  to reset.", "red", None),
        ("", None, None),
        ("── THE CODEX ───────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("After each mission, ARIA offers to open the Codex for the technique", None, None),
        ("you just used. Reading it earns +2 REP and unlocks the entry.", None, None),
        ("", None, None),
        ("Open the Codex any time via the CODEX button in the top bar.", None, None),
        ("12 topics are available across the full game:", None, None),
        ("", None, None),
        ("  Ch1  Port Scanning & Reconnaissance", "text_dim", None),
        ("  Ch1  Default & Weak Credentials", "text_dim", None),
        ("  Ch1  SQL Injection", "text_dim", None),
        ("  Ch2  Man-in-the-Middle & TLS Security", "text_dim", None),
        ("  Ch2  Buffer Overflow Vulnerabilities", "text_dim", None),
        ("  Ch2  Phishing & Social Engineering", "text_dim", None),
        ("  Ch3  Rootkits & Persistence", "text_dim", None),
        ("  Ch3  Command & Control Infrastructure", "text_dim", None),
        ("  Ch3  Lateral Movement & Air Gap Attacks", "text_dim", None),
        ("  Ch4  Zero-Day Vulnerabilities", "text_dim", None),
        ("  Ch4  Race Conditions & Timing Attacks", "text_dim", None),
        ("  Ch4  PKI & Certificate Trust", "text_dim", None),
        ("  Ch3  Malware RE — Static Analysis", "text_dim", None),
        ("  Ch3  Malware RE — Dynamic Analysis", "text_dim", None),
        ("  Ch2  Network Forensics", "text_dim", None),
        ("  Ch5  Incident Response", "text_dim", None),
        ("  Ch5  Digital Forensics & Evidence", "text_dim", None),
        ("  Ch5  Operational Security (OPSEC)", "text_dim", None),
        ("", None, None),
        ("── THE STORY ───────────────────────────────────────────────────────────", "green", None),
        ("", None, None),
        ("Ch1  First Contact      — Learn to move. MediaBridge subsidiary.", None, None),
        ("Ch2  The Network Beneath — Follow the data. CDN infrastructure.", None, None),
        ("Ch3  Ghost Protocol     — OmniCorp knows you exist. Go deeper.", None, None),
        ("Ch4  Zero Day           — 72 hours to stop PROJECT LAZARUS.", None, None),
        ("Ch5  The Reckoning      — Voss comes back. NEXUS becomes the target.", None, None),
        ("", None, None),
        ("Type  story  in the terminal to read the current chapter narrative.", None, None),
        ("Character transmissions appear automatically as you complete missions.", None, None),
    ],
}


class HelpWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("NEXUS — Help & Getting Started")
        self.win.configure(bg=C["bg"])
        self.win.geometry("860x640")
        self.win.transient(parent)
        self.win.resizable(True, True)
        self.win.minsize(700, 500)

        font_title = tkfont.Font(family="Courier New", size=13, weight="bold")
        font_tab   = tkfont.Font(family="Courier New", size=10, weight="bold")
        font_mono  = tkfont.Font(family="Courier New", size=10)
        font_small = tkfont.Font(family="Courier New", size=9)
        self.font_mono  = font_mono
        self.font_small = font_small

        # ── Header ──
        hdr = tk.Frame(self.win, bg=C["bg2"])
        hdr.pack(fill="x")
        tk.Label(hdr, text="◈ NEXUS: ZERO DAY — HELP & GETTING STARTED",
                 bg=C["bg2"], fg=C["green"], font=font_title, pady=8).pack(side="left", padx=12)
        tk.Button(hdr, text="✕ CLOSE", bg=C["bg3"], fg=C["text_dim"],
                  font=font_small, relief="flat", cursor="hand2",
                  activebackground=C["green_dk"], activeforeground=C["green"],
                  command=self.win.destroy).pack(side="right", padx=12, pady=6)

        tk.Frame(self.win, bg=C["border"], height=1).pack(fill="x")

        # ── Tab bar ──
        tab_bar = tk.Frame(self.win, bg=C["bg2"])
        tab_bar.pack(fill="x")
        self._tab_btns = {}
        self._active_tab = tk.StringVar(value="")

        for name in SECTIONS:
            btn = tk.Button(tab_bar, text=name, bg=C["bg2"], fg=C["text_dim"],
                            font=font_tab, relief="flat", bd=0, padx=14, pady=8,
                            cursor="hand2",
                            activebackground=C["green_dk"], activeforeground=C["green"],
                            command=lambda n=name: self._show_tab(n))
            btn.pack(side="left")
            self._tab_btns[name] = btn

        tk.Frame(self.win, bg=C["border"], height=1).pack(fill="x")

        # ── Content area ──
        content_frame = tk.Frame(self.win, bg=C["bg"])
        content_frame.pack(fill="both", expand=True)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        self._canvas = tk.Canvas(content_frame, bg=C["bg"], highlightthickness=0)
        sb = tk.Scrollbar(content_frame, orient="vertical", command=self._canvas.yview,
                          bg=C["bg"], troughcolor=C["bg2"], width=8)
        self._canvas.configure(yscrollcommand=sb.set)
        self._canvas.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")

        self._inner = tk.Frame(self._canvas, bg=C["bg"])
        self._cw = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")

        self._inner.bind("<Configure>",
            lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))
        self._canvas.bind("<Configure>",
            lambda e: self._canvas.itemconfig(self._cw, width=e.width))
        self._canvas.bind("<MouseWheel>",
            lambda e: self._canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self._canvas.bind("<Button-4>",
            lambda e: self._canvas.yview_scroll(-1, "units"))
        self._canvas.bind("<Button-5>",
            lambda e: self._canvas.yview_scroll(1, "units"))

        # Show first tab
        self._show_tab(list(SECTIONS.keys())[0])

    def _show_tab(self, name):
        # Update button highlight
        for n, btn in self._tab_btns.items():
            if n == name:
                btn.configure(bg=C["green_dk"], fg=C["green"])
            else:
                btn.configure(bg=C["bg2"], fg=C["text_dim"])

        # Clear content
        for w in self._inner.winfo_children():
            w.destroy()
        self._canvas.yview_moveto(0)

        # Render lines
        lines = SECTIONS[name]
        for text, color_key, _ in lines:
            if text == "":
                tk.Frame(self._inner, bg=C["bg"], height=6).pack(fill="x")
                continue

            fg = C.get(color_key, C["text"]) if color_key else C["text"]

            # Section dividers — lines starting with ──
            if text.startswith("──"):
                frame = tk.Frame(self._inner, bg=C["bg"])
                frame.pack(fill="x", padx=16, pady=(10, 2))
                tk.Label(frame, text=text, bg=C["bg"], fg=fg,
                         font=tkfont.Font(family="Courier New", size=10, weight="bold"),
                         anchor="w").pack(fill="x")
                tk.Frame(self._inner, bg=C["border"], height=1).pack(fill="x", padx=16, pady=(0, 4))
                continue

            # Command / mono lines (indented with spaces or all-caps short label)
            if text.startswith("    ") or (len(text) < 30 and text == text.upper() and text.strip()):
                font = self.font_mono
                pad_l = 32 if text.startswith("    ") else 16
            else:
                font = self.font_small
                pad_l = 16

            tk.Label(self._inner, text=text, bg=C["bg"], fg=fg,
                     font=font, anchor="w", justify="left",
                     wraplength=0).pack(fill="x", padx=(pad_l, 16), pady=1)
