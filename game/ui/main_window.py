"""
NEXUS: Zero Day — Main Window
Full desktop UI using tkinter with custom dark theme.
"""

import tkinter as tk
from tkinter import ttk, font as tkfont, messagebox, simpledialog
import threading
import time
import random
import string

from game.story import CHARACTERS, CHAPTERS, MISSIONS, EDU_CONTENT, TARGETS, ITEMS
from game.ui.terminal import TerminalWidget
from game.ui.mission_panel import MissionPanel
from game.ui.network_map import NetworkMapPanel
from game.ui.dialogue import DialogueWindow
from game.ui.edu_panel import EduPanel
from game.ui.minigame import MinigameController


# ── Colour palette ──
C = {
    "bg":        "#080c0a",
    "bg2":       "#0d1410",
    "bg3":       "#111a16",
    "bg4":       "#0a1208",
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
    "border_br": "#00ff8833",
}


class MainWindow:
    def __init__(self, root: tk.Tk, engine):
        self.root = root
        self.engine = engine
        self.minigame = MinigameController()

        self._setup_window()
        self._apply_theme()
        self._build_ui()
        self._register_events()
        self._show_title_screen()

    # ─────────────────────────────────────────
    # WINDOW SETUP
    # ─────────────────────────────────────────

    def _setup_window(self):
        self.root.title("NEXUS: Zero Day — Cybersecurity Simulation")
        self.root.configure(bg=C["bg"])
        self.root.geometry("1440x880")
        self.root.minsize(1000, 600)
        self._fullscreen = False

        # F11 / Escape toggle fullscreen
        self.root.bind("<F11>",  lambda e: self._toggle_fullscreen())
        self.root.bind("<Escape>", lambda e: self._exit_fullscreen())

        # Fonts
        self.font_mono   = tkfont.Font(family="Courier New", size=11)
        self.font_mono_s = tkfont.Font(family="Courier New", size=10)
        self.font_mono_b = tkfont.Font(family="Courier New", size=11, weight="bold")
        self.font_title  = tkfont.Font(family="Courier New", size=14, weight="bold")
        self.font_hdr    = tkfont.Font(family="Courier New", size=10, weight="bold")
        self.font_small  = tkfont.Font(family="Courier New", size=9)

    def _apply_theme(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame",       background=C["bg"])
        style.configure("TLabel",       background=C["bg"],       foreground=C["text"],     font=self.font_mono_s)
        style.configure("TButton",      background=C["bg3"],      foreground=C["green_dim"],font=self.font_mono_s,
                        relief="flat",  borderwidth=1)
        style.map("TButton",
                  background=[("active", C["green_dk"]), ("pressed", C["bg"])],
                  foreground=[("active", C["green"])])
        style.configure("Header.TLabel", background=C["bg2"], foreground=C["green"], font=self.font_hdr)
        style.configure("Dim.TLabel",    background=C["bg2"], foreground=C["text_dim"], font=self.font_small)
        style.configure("Amber.TLabel",  background=C["bg2"], foreground=C["amber"], font=self.font_mono_s)
        style.configure("Red.TLabel",    background=C["bg2"], foreground=C["red"], font=self.font_mono_s)
        style.configure("Cyan.TLabel",   background=C["bg2"], foreground=C["cyan"], font=self.font_mono_s)

    # ─────────────────────────────────────────
    # UI BUILD
    # ─────────────────────────────────────────

    def _build_ui(self):
        # Root grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Main container (hidden until game starts)
        self.game_frame = tk.Frame(self.root, bg=C["bg"])
        self.game_frame.grid(row=1, column=0, sticky="nsew")
        self.game_frame.grid_remove()

        self._build_topbar()
        self._build_main_layout()
        self._build_statusbar()

    def _build_topbar(self):
        bar = tk.Frame(self.root, bg=C["bg2"], height=42)
        bar.grid(row=0, column=0, sticky="ew")
        bar.grid_propagate(False)

        # Logo
        logo = tk.Label(bar, text="◈ NEXUS: ZERO DAY", bg=C["bg2"], fg=C["green"],
                        font=tkfont.Font(family="Courier New", size=15, weight="bold"))
        logo.pack(side="left", padx=16)

        tk.Label(bar, text="v1.0 — Cybersecurity Simulation", bg=C["bg2"],
                 fg=C["text_dim"], font=self.font_small).pack(side="left", padx=4)

        # Right stats
        right = tk.Frame(bar, bg=C["bg2"])
        right.pack(side="right", padx=12)

        self.lbl_time   = self._stat_label(right, "TIME:", "00:00")
        self.lbl_credits= self._stat_label(right, "CREDITS:", "$0")
        self.lbl_rep    = self._stat_label(right, "REP:", "0")
        self.lbl_owned  = self._stat_label(right, "SHELLS:", "0")

        # Trace meter
        tk.Label(right, text="TRACE:", bg=C["bg2"], fg=C["text_dim"],
                 font=self.font_small).pack(side="left", padx=(12, 4))
        self.trace_frame = tk.Frame(right, bg=C["bg2"])
        self.trace_frame.pack(side="left")
        self.trace_canvas = tk.Canvas(self.trace_frame, width=120, height=14,
                                       bg="#0a0a0a", highlightthickness=1,
                                       highlightbackground=C["border"])
        self.trace_canvas.pack()
        self.lbl_trace_pct = tk.Label(right, text="0%", bg=C["bg2"],
                                       fg=C["green"], font=self.font_small, width=4)
        self.lbl_trace_pct.pack(side="left", padx=2)

        # Menu buttons
        for lbl, cmd in [("SAVE", self._save_menu), ("LOAD", self._load_menu),
                          ("CODEX", self._open_codex), ("HELP", self._open_help), ("F11", self._toggle_fullscreen), ("QUIT", self._quit)]:
            tk.Button(bar, text=lbl, bg=C["bg3"], fg=C["text_dim"],
                      font=self.font_small, relief="flat", bd=1,
                      activebackground=C["green_dk"], activeforeground=C["green"],
                      cursor="hand2", command=cmd, padx=8).pack(side="right", padx=2, pady=6)

    def _stat_label(self, parent, key, val):
        f = tk.Frame(parent, bg=C["bg2"])
        f.pack(side="left", padx=8)
        tk.Label(f, text=key, bg=C["bg2"], fg=C["text_dim"],
                 font=self.font_small).pack(side="left")
        lbl = tk.Label(f, text=val, bg=C["bg2"], fg=C["green"],
                       font=self.font_mono_b)
        lbl.pack(side="left", padx=2)
        return lbl

    def _build_main_layout(self):
        f = self.game_frame
        f.grid_rowconfigure(0, weight=1)
        # Left fixed, centre expands, right fixed
        # Left and right panels use weight=1 each, centre uses weight=4
        # This makes all three panels scale proportionally in fullscreen
        f.grid_columnconfigure(0, weight=1, minsize=220)
        f.grid_columnconfigure(1, weight=4)
        f.grid_columnconfigure(2, weight=1, minsize=280)

        # ── Left panel ──
        left = tk.Frame(f, bg=C["bg2"])
        left.grid(row=0, column=0, sticky="nsew")
        left.grid_propagate(False)
        left.grid_columnconfigure(0, weight=1)
        # Network map gets most space; toolkit fixed at bottom
        left.grid_rowconfigure(1, weight=1)

        self._panel_header(left, "◈ NETWORK MAP").grid(row=0, column=0, sticky="ew")
        self.network_panel = NetworkMapPanel(left, self.engine, self)
        self.network_panel.frame.grid(row=1, column=0, sticky="nsew")

        tk.Frame(left, bg=C["border"], height=1).grid(row=2, column=0, sticky="ew")
        self._panel_header(left, "◈ TOOLKIT").grid(row=3, column=0, sticky="ew")

        tk_frame = tk.Frame(left, bg=C["bg2"])
        tk_frame.grid(row=4, column=0, sticky="ew", padx=4, pady=4)
        self._build_toolkit(tk_frame)

        # ── Centre — terminal + tabs ──
        centre = tk.Frame(f, bg=C["bg"])
        centre.grid(row=0, column=1, sticky="nsew")
        centre.grid_rowconfigure(1, weight=1)
        centre.grid_columnconfigure(0, weight=1)

        self._build_tabs(centre)

        self.terminal = TerminalWidget(centre, self.engine, self)
        self.terminal.frame.grid(row=1, column=0, sticky="nsew")

        # Input row
        inp = tk.Frame(centre, bg=C["bg2"])
        inp.grid(row=2, column=0, sticky="ew")
        inp.grid_columnconfigure(1, weight=1)
        self.prompt_lbl = tk.Label(inp, text="nexus@localhost:~$", bg=C["bg2"],
                                    fg=C["green"], font=self.font_mono)
        self.prompt_lbl.grid(row=0, column=0, padx=(8,4), pady=4)
        self.cmd_entry = tk.Entry(inp, bg=C["bg"], fg=C["green"],
                                   font=self.font_mono, insertbackground=C["green"],
                                   relief="flat", bd=0)
        self.cmd_entry.grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        self.cmd_entry.bind("<Return>", self._on_command)
        self.cmd_entry.bind("<Up>",     self._history_up)
        self.cmd_entry.bind("<Down>",   self._history_down)
        self.cmd_entry.bind("<Tab>",    self._tab_complete)
        self.cmd_entry.focus_set()

        # ── Right panel ──
        right = tk.Frame(f, bg=C["bg2"])
        right.grid(row=0, column=2, sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        # Contracts panel takes 60% of height, intel takes 40%
        right.grid_rowconfigure(1, weight=3)
        right.grid_rowconfigure(4, weight=2)

        self._panel_header(right, "◈ ACTIVE CONTRACTS").grid(row=0, column=0, sticky="ew")
        self.mission_panel = MissionPanel(right, self.engine, self)
        self.mission_panel.frame.grid(row=1, column=0, sticky="nsew")

        tk.Frame(right, bg=C["border"], height=1).grid(row=2, column=0, sticky="ew")
        self._panel_header(right, "◈ TARGET INTEL").grid(row=3, column=0, sticky="ew")
        self.intel_frame = tk.Frame(right, bg=C["bg2"])
        self.intel_frame.grid(row=4, column=0, sticky="nsew", padx=6, pady=4)
        self._update_intel_panel()

    def _build_tabs(self, parent):
        tab_bar = tk.Frame(parent, bg=C["bg2"])
        tab_bar.grid(row=0, column=0, sticky="ew")
        self.active_tab = tk.StringVar(value="terminal")
        self.tab_btns = {}
        for name in ["TERMINAL", "STORY", "INTEL", "FILES", "LOGS"]:
            key = name.lower()
            btn = tk.Button(tab_bar, text=name, bg=C["bg"], fg=C["text_dim"],
                            font=self.font_small, relief="flat", bd=0, padx=12, pady=6,
                            activebackground=C["bg3"], activeforeground=C["green"],
                            cursor="hand2",
                            command=lambda k=key: self._switch_tab(k))
            btn.pack(side="left")
            self.tab_btns[key] = btn
        self._switch_tab("terminal", init=True)

    def _build_toolkit(self, parent):
        tools = [
            ("PORT SCAN",    "portscan"),
            ("BRUTE FORCE",  "bruteforce"),
            ("SQL INJECT",   "sqlinject"),
            ("BUF OVERFLOW", "overflow"),
            ("SSH CRACK",    "sshcrack"),
            ("0-DAY XPLOIT", "zeroday_prep"),
            ("MAN-IN-MID",   "mitm"),
            ("IMPLANT",      "implant"),
            ("ROOTKIT",      "lkm_compile"),
            ("PHISHING",     "craft_phish"),
            ("BOUNCE",       "bounce"),
            ("LOG WIPE",     "log_wipe"),
        ]
        self.tool_buttons = {}
        for i, (label, tid) in enumerate(tools):
            r, c = divmod(i, 2)
            btn = tk.Button(parent, text=label, bg=C["bg3"], fg=C["text_dim"],
                            font=self.font_small, relief="flat", bd=1,
                            highlightbackground=C["border"], highlightthickness=1,
                            activebackground=C["green_dk"], activeforeground=C["green"],
                            cursor="hand2", padx=4, pady=3,
                            command=lambda t=tid: self._run_tool(t))
            btn.grid(row=r, column=c, sticky="ew", padx=2, pady=2)
            self.tool_buttons[tid] = btn
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

    def _build_statusbar(self):
        bar = tk.Frame(self.root, bg=C["green_dk"], height=26)
        bar.grid(row=2, column=0, sticky="ew")
        bar.grid_propagate(False)

        self.status_msg = tk.Label(bar, text="System ready. Start a new game or load a save.  |  F11 = Fullscreen",
                                    bg=C["green_dk"], fg=C["green"], font=self.font_small)
        self.status_msg.pack(side="left", padx=12)

        for key, val in [("CPU", "8%"), ("NET", "2.1MB/s"), ("CONN", "LOCAL")]:
            f = tk.Frame(bar, bg=C["green_dk"])
            f.pack(side="right", padx=10)
            tk.Label(f, text=f"{key}:", bg=C["green_dk"], fg=C["green_dim"],
                     font=self.font_small).pack(side="left")
            lbl = tk.Label(f, text=val, bg=C["green_dk"], fg=C["green"],
                           font=self.font_small)
            lbl.pack(side="left")

    # ─────────────────────────────────────────
    # TITLE SCREEN
    # ─────────────────────────────────────────

    # ─────────────────────────────────────────
    # FULLSCREEN
    # ─────────────────────────────────────────

    def _toggle_fullscreen(self):
        self._fullscreen = not self._fullscreen
        self.root.attributes("-fullscreen", self._fullscreen)
        # Update status bar hint
        hint = "Press F11 or Escape to exit fullscreen" if self._fullscreen else "Press F11 for fullscreen"
        self.set_status(hint)

    def _exit_fullscreen(self):
        if self._fullscreen:
            self._fullscreen = False
            self.root.attributes("-fullscreen", False)

    def _show_title_screen(self):
        self.title_frame = tk.Frame(self.root, bg=C["bg"])
        self.title_frame.grid(row=1, column=0, sticky="nsew")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Centre column
        inner = tk.Frame(self.title_frame, bg=C["bg"])
        inner.place(relx=0.5, rely=0.5, anchor="center")

        # ASCII art title
        art = [
            "███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗",
            "████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝",
            "██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗",
            "██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║",
            "██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║",
            "╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝",
        ]
        for line in art:
            tk.Label(inner, text=line, bg=C["bg"], fg=C["green"],
                     font=tkfont.Font(family="Courier New", size=13, weight="bold")).pack()

        tk.Label(inner, text="Z E R O   D A Y", bg=C["bg"], fg=C["text_dim"],
                 font=tkfont.Font(family="Courier New", size=12,
                                  weight="bold")).pack(pady=(4, 0))
        tk.Label(inner, text="A Cybersecurity Education Simulation", bg=C["bg"],
                 fg=C["text_dim"], font=self.font_small).pack(pady=(2, 24))

        # Buttons
        for label, cmd in [
            ("[ NEW GAME ]", self._new_game_dialog),
            ("[ CONTINUE ]", lambda: self._load_menu()),
            ("[ HOW TO PLAY ]", self._open_help),
            ("[ QUIT ]", self._quit),
        ]:
            tk.Button(inner, text=label, bg=C["bg3"], fg=C["green_dim"],
                      font=self.font_mono, relief="flat", bd=1,
                      highlightbackground=C["border"], highlightthickness=1,
                      activebackground=C["green_dk"], activeforeground=C["green"],
                      cursor="hand2", width=30, pady=6,
                      command=cmd).pack(pady=4)

        tk.Label(inner, text="Educational simulation — no real systems are targeted",
                 bg=C["bg"], fg=C["text_dim"], font=self.font_small).pack(pady=(20, 0))

    def _new_game_dialog(self):
        handle = simpledialog.askstring("New Game",
                                         "Enter your hacker handle:",
                                         initialvalue="gh0st",
                                         parent=self.root)
        if handle:
            handle = handle.strip().lower().replace(" ", "_") or "gh0st"
            self._start_game(handle)

    def _start_game(self, handle="gh0st"):
        self.engine.new_game(handle)
        self.title_frame.destroy()
        self.game_frame.grid()
        self.root.grid_rowconfigure(1, weight=1)
        self._refresh_all()
        self._start_clock()
        self._print_welcome()
        # Show Vera's prologue message first, then ch1 intro after player closes it
        self.root.after(600, lambda: self._show_chapter_intro("ch0"))
        self.set_status("Welcome to NEXUS. Check your contracts on the right — type 'missions' or click a card.")

    def _print_welcome(self):
        """Print oriented boot messages after new game starts."""
        gs = self.engine.state
        lines = [
            ("", "out"),
            ("╔══════════════════════════════════════════════════════════════╗", "success"),
            ("║          NEXUS OPERATIVE TERMINAL — SYSTEM READY            ║", "success"),
            ("╚══════════════════════════════════════════════════════════════╝", "success"),
            ("", "out"),
            (f"  Handle   : {gs.player_handle}", "out"),
            (f"  Status   : ACTIVE — Chapter 1: First Contact", "out"),
            (f"  Target   : MEDIABRIDGE-RELAY-01  [10.44.12.8]", "out"),
            ("", "out"),
            ("  ┌─ GETTING STARTED ────────────────────────────────────────┐", "info"),
            ("  │  1. Your contracts are in the RIGHT PANEL →              │", "info"),
            ("  │     Click a mission card to accept it, or type:          │", "info"),
            ("  │       missions    then    accept 1                        │", "info"),
            ("  │                                                           │", "info"),
            ("  │  2. Run recon on your target first:  scan                │", "info"),
            ("  │  3. Use the TOOLKIT buttons (left) to run exploits       │", "info"),
            ("  │  4. Click HELP in the top bar for the full guide         │", "info"),
            ("  │  5. Press F11 for fullscreen                             │", "info"),
            ("  └───────────────────────────────────────────────────────────┘", "info"),
            ("", "out"),
            ("  ARIA: 'You have 3 contracts waiting. Start with Ghost in the Wire.'", "sys"),
            ("", "out"),
        ]
        for text, tag in lines:
            self.terminal.print_line(text, tag)

    # ─────────────────────────────────────────
    # EVENT CALLBACKS
    # ─────────────────────────────────────────

    def _register_events(self):
        e = self.engine
        e.on("state_changed",    lambda: self.root.after(0, self._refresh_all))
        e.on("target_changed",   lambda tid: self.root.after(0, self._on_target_changed))
        e.on("mission_accepted", lambda m: self.root.after(0, lambda: self._on_mission_accepted(m)))
        e.on("mission_complete", lambda m: self.root.after(0, lambda: self._on_mission_complete(m)))
        e.on("chapter_unlocked", lambda cid: self.root.after(0, lambda: self._on_chapter_unlocked(cid)))
        e.on("exploit_result",   lambda r: self.root.after(0, lambda: self._on_exploit_result(r)))
        e.on("player_busted",    lambda: self.root.after(0, self._player_busted))
        e.on("log_entry",        lambda entry: self.root.after(0, lambda: self._on_log(entry)))

    def _on_target_changed(self):
        self._update_intel_panel()
        self._update_prompt()
        self.network_panel.refresh()

    def _on_mission_accepted(self, mission):
        self.terminal.print_line(f"", "out")
        self.terminal.print_line(f"◈ CONTRACT ACCEPTED: {mission['title']}", "success")
        self.terminal.print_line(f"  OBJECTIVE: {mission['objective']}", "sys")
        self.terminal.print_line(f"  REWARD: ${mission['reward_credits']:,} + {mission['reward_rep']} REP", "sys")
        self.terminal.print_line(f"", "out")
        self.mission_panel.refresh()
        self.set_status(f"Mission active: {mission['title']}")

    def _on_mission_complete(self, mission):
        self.terminal.print_line("", "out")
        self.terminal.print_line("╔══════════════════════════════════════════════╗", "success")
        self.terminal.print_line(f"║  CONTRACT COMPLETE                          ║", "success")
        self.terminal.print_line(f"║  {mission['title'][:44].ljust(44)}║", "success")
        self.terminal.print_line(f"║  +${mission['reward_credits']:,}  |  +{mission['reward_rep']} REP{'':>20}║", "success")
        self.terminal.print_line("╚══════════════════════════════════════════════╝", "success")
        self.terminal.print_line("", "out")
        self._refresh_stats()
        self.mission_panel.refresh()

        # Show completion dialogue
        comp_dlg = mission.get("completion_dialog")
        if comp_dlg:
            self.root.after(1200, lambda: self._show_dialogue(comp_dlg))

        # Edu topic
        edu = mission.get("edu_topic")
        if edu and edu not in self.engine.state.edu_topics_read:
            self.root.after(2500, lambda: self._prompt_edu(edu))

        self.set_status(f"Contract complete! +${mission['reward_credits']:,} earned")

    def _on_chapter_unlocked(self, chapter_id):
        chapter = next((c for c in CHAPTERS if c["id"] == chapter_id), None)
        if not chapter:
            return
        self.root.after(1000, lambda: self._show_chapter_intro(chapter_id))
        self.mission_panel.refresh()
        self.network_panel.refresh()

    def _on_exploit_result(self, result):
        self._refresh_stats()
        self._update_intel_panel()

    def _on_log(self, entry):
        pass  # logs visible in LOGS tab

    def _player_busted(self):
        self.terminal.clear()
        lines = [
            "██████████████████████████████████████████████████",
            "██                                              ██",
            "██    ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗   ██",
            "██    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ╚════██╗  ██",
            "██     ╚████╔╝ ██║   ██║██║   ██║     █████╔╝  ██",
            "██      ╚██╔╝  ██║   ██║██║   ██║    ██╔═══╝   ██",
            "██       ██║   ╚██████╔╝╚██████╔╝    ███████╗  ██",
            "██       ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝  ██",
            "██                                              ██",
            "██  TRACE LEVEL: 100%  —  IDENTITY COMPROMISED  ██",
            "██  Federal agents are triangulating your pos.  ██",
            "██                                              ██",
            "██████████████████████████████████████████████████",
        ]
        for line in lines:
            self.terminal.print_line(line, "err")
        self.terminal.print_line("", "out")
        self.terminal.print_line("  Type 'restart' to wipe your tracks and start over.", "warn")
        self.set_status("BUSTED — Identity exposed. Game over.")

    # ─────────────────────────────────────────
    # TAB SYSTEM
    # ─────────────────────────────────────────

    def _switch_tab(self, key, init=False):
        self.active_tab.set(key)
        for k, btn in self.tab_btns.items():
            if k == key:
                btn.configure(bg=C["bg"], fg=C["green"], relief="flat")
            else:
                btn.configure(bg=C["bg2"], fg=C["text_dim"], relief="flat")

        if init:
            return

        if key == "terminal":
            self.terminal.frame.tkraise()
            self.cmd_entry.focus_set()
        elif key == "story":
            self._show_story_tab()
        elif key == "intel":
            self._show_intel_tab()
        elif key == "files":
            self._show_files_tab()
        elif key == "logs":
            self._show_logs_tab()

    def _show_story_tab(self):
        self.terminal.clear()
        gs = self.engine.state
        if not gs:
            return
        chapter = self.engine.get_current_chapter()
        self.terminal.print_line("◈ CURRENT CHAPTER", "hdr")
        self.terminal.print_line("─" * 60, "dim")
        self.terminal.print_line(chapter["title"], "success")
        self.terminal.print_line(chapter["subtitle"], "info")
        self.terminal.print_line("", "out")
        for line in chapter["intro"].split("\n"):
            self.terminal.print_line(line, "out")
        self.terminal.print_line("", "out")
        self.terminal.print_line("─" * 60, "dim")
        self.terminal.print_line("◈ PROGRESS", "hdr")
        done, total = self.engine.get_chapter_progress()
        bar = ("█" * done) + ("░" * (total - done))
        self.terminal.print_line(f"  Missions: [{bar}] {done}/{total}", "out")
        self.terminal.print_line(f"  Credits : ${gs.credits:,}", "out")
        self.terminal.print_line(f"  Rep     : {gs.rep}", "out")
        self.terminal.print_line(f"  Playtime: {self.engine.format_play_time()}", "out")
        self.terminal.print_line("", "out")
        self.terminal.print_line("─" * 60, "dim")
        self.terminal.print_line("◈ CHARACTERS", "hdr")
        for cid, char in CHARACTERS.items():
            self.terminal.print_line(f"  {char['portrait']} {char['name']}  [{char['handle']}]", "info")
            self.terminal.print_line(f"     {char['role']}", "dim")

    def _show_intel_tab(self):
        self.terminal.clear()
        t = self.engine.active_target
        if not t:
            self.terminal.print_line("[!] No target selected.", "err")
            return
        self.terminal.print_line(f"◈ INTELLIGENCE REPORT — {t['name']}", "hdr")
        self.terminal.print_line("─" * 60, "dim")
        fields = [
            ("IP ADDRESS", t["ip"]),
            ("ORGANISATION", t["org"]),
            ("OS / STACK", t["os"]),
            ("SECURITY", t["sec_label"]),
            ("OPEN PORTS", ", ".join(str(p) for p in t["ports"])),
        ]
        for k, v in fields:
            self.terminal.print_line(f"  {k:<16}: {v}", "out")
        self.terminal.print_line("", "out")
        self.terminal.print_line("  SERVICES:", "hdr")
        for port, svc in t.get("services", {}).items():
            self.terminal.print_line(f"    {port:<6} {svc}", "out")
        self.terminal.print_line("", "out")
        self.terminal.print_line("  KNOWN VULNERABILITIES:", "warn")
        for v in t.get("vulns", []):
            self.terminal.print_line(f"    ◈ {v}", "warn")
        self.terminal.print_line("", "out")
        self.terminal.print_line(f"  LORE: {t.get('lore', '')}", "dim")

    def _show_files_tab(self):
        self.terminal.clear()
        t = self.engine.active_target
        if not t:
            self.terminal.print_line("[!] No target selected.", "err")
            return
        if not self.engine.has_shell():
            self.terminal.print_line(f"[!] No shell on {t['name']}.", "err")
            self.terminal.print_line("[*] Gain root access first using the TOOLKIT.", "sys")
            return
        self.terminal.print_line(f"◈ FILE SYSTEM — {t['name']}", "hdr")
        self.terminal.print_line("─" * 60, "dim")
        files = self._get_fake_files(t)
        for f_entry in files:
            self.terminal.print_line(f_entry, "out")
        self.terminal.print_line("", "out")
        if t.get("data"):
            self.terminal.print_line("  ◈ EXFILTRABLE DATA:", "success")
            for k, v in t["data"].items():
                self.terminal.print_line(f"    [{k}]  {v}", "amber")

    def _get_fake_files(self, t):
        base = [
            "total 128",
            "drwxr-xr-x  4 root root  4096 Jan 12 09:14 .",
            "drwxr-xr-x 22 root root  4096 Jan 12 09:14 ..",
            "-rw-r--r--  1 root root   220 Mar 15 2023  .bash_logout",
            "-rwxr-xr-x  1 root root 12288 Jan  3 11:22 /bin/startup",
            "drwx------  2 root root  4096 Jan 12 09:14 .ssh",
        ]
        if 80 in t["ports"] or 443 in t["ports"]:
            base += ["-rw-r--r--  1 www  www  155264 Jan  8 ./www/index.php",
                     "-rw-------  1 www  www    4096 Dec 22 ./www/config.php"]
        if 3306 in t["ports"] or 5432 in t["ports"]:
            base += ["-rw-r--r--  1 db   db  196608 Jan 12 ./db/schema.sql",
                     "-rw-------  1 db   db   49152 Jan 12 ./db/credentials.cnf"]
        if 22 in t["ports"]:
            base += ["-rw-------  1 root root   1679 Nov  4 .ssh/id_rsa",
                     "-rw-r--r--  1 root root    398 Nov  4 .ssh/id_rsa.pub"]
        for k in t.get("data", {}):
            base.append(f"-rw-------  1 root root   8192 Jan 12 ./root/{k.replace(' ','_')}.dat")
        return base

    def _show_logs_tab(self):
        self.terminal.clear()
        gs = self.engine.state
        if not gs:
            return
        self.terminal.print_line("◈ OPERATION LOG", "hdr")
        self.terminal.print_line("─" * 60, "dim")
        entries = gs.log_entries[-40:]
        if not entries:
            self.terminal.print_line("  No entries.", "dim")
        for entry in entries:
            cls = {"success": "success", "err": "err", "warn": "warn",
                   "mission": "info", "story": "purple"}.get(entry["level"], "out")
            self.terminal.print_line(f"  [{entry['time']}] {entry['msg']}", cls)

    # ─────────────────────────────────────────
    # COMMAND HANDLER
    # ─────────────────────────────────────────

    def _on_command(self, event=None):
        raw = self.cmd_entry.get().strip()
        self.cmd_entry.delete(0, tk.END)
        if not raw:
            return
        gs = self.engine.state
        if gs:
            gs.terminal_history.append(raw)
        prompt = self.prompt_lbl.cget("text")
        self.terminal.print_line(f"{prompt} {raw}", "cmd")
        self._process_command(raw)

    def _process_command(self, raw):
        parts = raw.strip().split()
        if not parts:
            return
        cmd = parts[0].lower()
        args = parts[1:]

        commands = {
            "help":       lambda a: self._open_help(),
            "commands":   self._cmd_help,
            "ls":         self._cmd_ls,
            "dir":        self._cmd_ls,
            "cat":        lambda a: self._cmd_cat(a),
            "scan":       lambda a: self._run_tool("portscan"),
            "nmap":       lambda a: self._run_tool("portscan"),
            "connect":    lambda a: self._cmd_connect(a),
            "disconnect": lambda a: self._cmd_disconnect(),
            "whoami":     lambda a: self._cmd_whoami(),
            "ifconfig":   lambda a: self._cmd_ifconfig(),
            "ps":         lambda a: self._cmd_ps(),
            "netstat":    lambda a: self._cmd_netstat(),
            "missions":   lambda a: self._cmd_missions(),
            "status":     lambda a: self._cmd_status(),
            "credits":    lambda a: self._cmd_credits(),
            "inventory":  lambda a: self._cmd_inventory(),
            "clear":      lambda a: self.terminal.clear(),
            "cls":        lambda a: self.terminal.clear(),
            "trace":      lambda a: self._cmd_trace(),
            "bounce":     lambda a: self._cmd_bounce(),
            "history":    lambda a: self._cmd_history(),
            "codex":      lambda a: self._open_codex(),
            "save":       lambda a: self._save_menu(),
            "load":       lambda a: self._load_menu(),
            "restart":    lambda a: self._restart(),
            "story":      lambda a: self._switch_tab("story"),
            "logs":       lambda a: self._switch_tab("logs"),
            "intel":      lambda a: self._switch_tab("intel"),
            "hack":       lambda a: self._run_tool("bruteforce"),
            "exploit":    lambda a: self._run_tool(a[0] if a else "bruteforce"),
            "accept":     lambda a: self._cmd_accept(a),
            "recon":      lambda a: self._run_tool("recon"),
        }

        if cmd in commands:
            try:
                commands[cmd](args)
            except Exception as ex:
                self.terminal.print_line(f"[!] Command error: {ex}", "err")
        elif cmd == "":
            pass
        else:
            self.terminal.print_line(f"-bash: {cmd}: command not found. Type 'help'.", "err")

    def _cmd_help(self, *_):
        self.terminal.print_line("", "out")
        self.terminal.print_line("┌───────────────────────────────────────────────────────────┐", "hdr")
        self.terminal.print_line("│              NEXUS COMMAND REFERENCE                      │", "hdr")
        self.terminal.print_line("├───────────────────────────────────────────────────────────┤", "hdr")
        rows = [
            ("scan / nmap",    "Port scan target",      "missions",  "List contracts"),
            ("connect <ip>",   "Connect to target",     "accept <n>","Accept mission #N"),
            ("recon",          "OSINT reconnaissance",  "status",    "Player status"),
            ("exploit <tool>", "Run exploit on target", "inventory", "Your items"),
            ("ls / dir",       "List target files",     "codex",     "Open Codex (edu)"),
            ("cat <file>",     "Read a file",           "bounce",    "Mask your origin"),
            ("ps",             "List processes",        "trace",     "Trace level"),
            ("whoami",         "Current user",          "history",   "Command history"),
            ("story",          "Story/chapter view",    "logs",      "Operation log"),
            ("intel",          "Target intel tab",      "save/load", "Save/Load game"),
            ("clear",          "Clear terminal",        "restart",   "Restart after bust"),
        ]
        for r in rows:
            self.terminal.print_line(f"│  {r[0]:<18} {r[1]:<22} {r[2]:<12} {r[3]:<14}│", "out")
        self.terminal.print_line("└───────────────────────────────────────────────────────────┘", "hdr")
        self.terminal.print_line("", "out")
        self.terminal.print_line("  Toolkit buttons on the LEFT also run exploits on current target.", "sys")
        self.terminal.print_line("  CODEX button opens the cybersecurity education library.", "sys")
        self.terminal.print_line("", "out")

    def _cmd_ls(self, *_):
        t = self.engine.active_target
        if not t:
            self.terminal.print_line("No target.", "err")
            return
        self._show_files_tab()
        self._switch_tab("files")

    def _cmd_cat(self, args):
        t = self.engine.active_target
        if not args:
            self.terminal.print_line("Usage: cat <filename>", "err")
            return
        if not self.engine.has_shell():
            self.terminal.print_line("Permission denied — no shell access.", "err")
            return
        fn = args[0].lower()
        h = self.engine.random_hex
        if "config" in fn or ".php" in fn:
            for line in [f"<?php", f"define('DB_HOST', 'localhost');",
                         f"define('DB_PASS', '{h(12)}');",
                         f"define('SECRET_KEY', '{h(32)}');", f"?>"]:
                self.terminal.print_line(line, "warn" if "PASS" in line or "KEY" in line else "out")
        elif "shadow" in fn:
            self.terminal.print_line(f"root:$6${h(16)}${h(64)}:19000:0:99999:7:::", "warn")
            self.terminal.print_line(f"svc:{h(8)}:19200:0:99999:7:::", "out")
        elif "id_rsa" in fn:
            self.terminal.print_line("-----BEGIN RSA PRIVATE KEY-----", "warn")
            for _ in range(6):
                self.terminal.print_line(h(32).upper(), "warn")
            self.terminal.print_line("-----END RSA PRIVATE KEY-----", "warn")
        else:
            self.terminal.print_line(f"cat: {args[0]}: No such file or directory", "err")

    def _cmd_connect(self, args):
        if not args:
            self.terminal.print_line("Usage: connect <ip or target-id>", "err")
            return
        target = next((t for t in TARGETS.values()
                        if t["ip"] == args[0] or args[0].lower() in t["name"].lower()), None)
        if not target:
            self.terminal.print_line(f"connect: {args[0]}: No route to host", "err")
            return
        tid = next(k for k, v in TARGETS.items() if v is target)
        self.engine.set_active_target(tid)
        self.terminal.print_line(f"[+] Connected to {target['name']} [{target['ip']}]", "success")
        self.terminal.print_line(f"    OS: {target['os']}", "sys")
        self._update_prompt()

    def _cmd_disconnect(self):
        self.terminal.print_line("[*] Disconnected. Returned to localhost.", "sys")
        self._update_prompt()

    def _cmd_whoami(self):
        owned = self.engine.has_shell()
        self.terminal.print_line("root" if owned else "nobody", "success" if owned else "err")

    def _cmd_ifconfig(self):
        gs = self.engine.state
        self.terminal.print_line("", "out")
        self.terminal.print_line("eth0  inet 10.0.0.47  netmask 255.255.255.0", "out")
        self.terminal.print_line("      inet6 fe80::a00:27ff  prefixlen 64", "out")
        if gs and gs.bouncing:
            self.terminal.print_line("tun0  BOUNCE ACTIVE — Origin masked", "success")
            self.terminal.print_line(f"      Chain: {' → '.join(gs.bounce_hops)}", "success")
        self.terminal.print_line("", "out")

    def _cmd_ps(self):
        owned = self.engine.has_shell()
        self.terminal.print_line("  PID   CMD", "hdr")
        for p in ["1 systemd", "245 sshd", "789 nginx", "1024 postgres", "2048 cron", "3001 bash"]:
            self.terminal.print_line(f"  {p}", "out")
        if owned:
            self.terminal.print_line("  4096 [nexus-implant] <hidden>", "success")

    def _cmd_netstat(self):
        t = self.engine.active_target
        self.terminal.print_line("Proto  Local                Foreign              State", "hdr")
        self.terminal.print_line("tcp    0.0.0.0:22           0.0.0.0:*            LISTEN", "out")
        self.terminal.print_line("tcp    0.0.0.0:80           0.0.0.0:*            LISTEN", "out")
        if t and self.engine.has_shell():
            self.terminal.print_line(f"tcp    {t['ip']}:{t['ports'][0]}        10.0.0.47:48321      ESTABLISHED", "success")

    def _cmd_missions(self):
        self.terminal.print_line("", "out")
        self.terminal.print_line("◈ AVAILABLE CONTRACTS", "hdr")
        self.terminal.print_line("─" * 55, "dim")
        missions = self.engine.get_available_missions()
        if not missions:
            self.terminal.print_line("  No contracts available in current chapter.", "dim")
        for i, m in enumerate(missions):
            tgt = TARGETS.get(m["target_id"], {})
            self.terminal.print_line(f"  [{i+1}] {m['title']}", "out")
            self.terminal.print_line(f"      Target: {tgt.get('name','?')}  |  ${m['reward_credits']:,} + {m['reward_rep']} REP  |  [{m['difficulty'].upper()}]", "sys")
        self.terminal.print_line("", "out")
        self.terminal.print_line("  Type 'accept <N>' to accept a contract.", "sys")
        self.terminal.print_line("", "out")

    def _cmd_accept(self, args):
        missions = self.engine.get_available_missions()
        if not args:
            self.terminal.print_line("Usage: accept <mission number>", "err")
            return
        try:
            idx = int(args[0]) - 1
            if 0 <= idx < len(missions):
                self.engine.accept_mission(missions[idx]["id"])
            else:
                self.terminal.print_line("Invalid mission number.", "err")
        except ValueError:
            self.terminal.print_line("Usage: accept <number>", "err")

    def _cmd_status(self):
        gs = self.engine.state
        if not gs:
            return
        self.terminal.print_line("", "out")
        self.terminal.print_line("◈ OPERATOR STATUS", "hdr")
        self.terminal.print_line(f"  Handle   : {gs.player_handle}", "out")
        self.terminal.print_line(f"  Credits  : ${gs.credits:,}", "out")
        self.terminal.print_line(f"  Rep      : {gs.rep}", "out")
        trace_cls = "err" if gs.trace > 60 else "warn" if gs.trace > 30 else "success"
        self.terminal.print_line(f"  Trace    : {gs.trace:.1f}%", trace_cls)
        self.terminal.print_line(f"  Shells   : {len(gs.owned_targets)}", "out")
        self.terminal.print_line(f"  Missions : {len(gs.completed_missions)}", "out")
        self.terminal.print_line(f"  Playtime : {self.engine.format_play_time()}", "out")
        self.terminal.print_line(f"  Bouncing : {'YES' if gs.bouncing else 'NO'}", "success" if gs.bouncing else "dim")
        self.terminal.print_line("", "out")

    def _cmd_credits(self):
        gs = self.engine.state
        self.terminal.print_line(f"Balance: ${gs.credits:,}", "success")

    def _cmd_inventory(self):
        gs = self.engine.state
        self.terminal.print_line("", "out")
        self.terminal.print_line("◈ INVENTORY", "hdr")
        if not gs.inventory:
            self.terminal.print_line("  Empty.", "dim")
        for iid in gs.inventory:
            item = ITEMS.get(iid, {"name": iid, "desc": "", "icon": "?"})
            self.terminal.print_line(f"  {item['icon']}  {item['name']}", "out")
            self.terminal.print_line(f"     {item['desc']}", "dim")
        self.terminal.print_line("", "out")

    def _cmd_trace(self):
        gs = self.engine.state
        lvl = gs.trace
        cls = "err" if lvl > 60 else "warn" if lvl > 30 else "success"
        self.terminal.print_line(f"Trace level: {lvl:.1f}%", cls)
        if lvl > 70:
            self.terminal.print_line("[!] CRITICAL: Reduce trace immediately — use 'bounce' or log wipe.", "err")
        elif lvl > 40:
            self.terminal.print_line("[*] Elevated. Consider activating bounce routing.", "warn")
        else:
            self.terminal.print_line("[*] Manageable. Stay clean.", "sys")

    def _cmd_bounce(self):
        gs = self.engine.state
        self.terminal.print_line("[*] Establishing proxy chain...", "sys")
        hops = [f"185.{random.randint(10,200)}.{random.randint(1,250)}.{random.randint(1,250)}" for _ in range(3)]

        def _do_bounce():
            for i, h in enumerate(hops):
                time.sleep(0.4)
                self.root.after(0, lambda hh=h, ii=i: self.terminal.print_line(f"[+] Hop {ii+1}: {hh} ✓", "success"))
            time.sleep(0.4)
            def _done():
                gs.bouncing = True
                gs.bounce_hops = hops
                gs.trace_multiplier = min(gs.trace_multiplier, 0.3)
                self.terminal.print_line("[+] Bounce chain active. Trace generation reduced 70%.", "success")
                self.engine.reduce_trace(10.0)
                self._refresh_stats()
            self.root.after(0, _done)

        threading.Thread(target=_do_bounce, daemon=True).start()

    def _cmd_history(self):
        gs = self.engine.state
        for i, cmd in enumerate(gs.terminal_history[-20:], 1):
            self.terminal.print_line(f"  {i:3}  {cmd}", "dim")

    def _tab_complete(self, event):
        partial = self.cmd_entry.get().lower()
        cmds = ["help","ls","cat","scan","nmap","connect","disconnect","whoami","ifconfig",
                "ps","netstat","missions","status","credits","inventory","clear","trace",
                "bounce","history","codex","save","load","restart","story","logs","intel",
                "hack","exploit","accept","recon","bounce"]
        match = next((c for c in cmds if c.startswith(partial) and c != partial), None)
        if match:
            self.cmd_entry.delete(0, tk.END)
            self.cmd_entry.insert(0, match)
        return "break"

    def _history_up(self, event):
        gs = self.engine.state
        if not gs or not gs.terminal_history:
            return
        hist = gs.terminal_history
        current = self.cmd_entry.get()
        try:
            idx = hist.index(current) - 1
        except ValueError:
            idx = len(hist) - 1
        idx = max(0, idx)
        self.cmd_entry.delete(0, tk.END)
        self.cmd_entry.insert(0, hist[idx])

    def _history_down(self, event):
        gs = self.engine.state
        if not gs or not gs.terminal_history:
            return
        self.cmd_entry.delete(0, tk.END)

    # ─────────────────────────────────────────
    # TOOLKIT / EXPLOITS
    # ─────────────────────────────────────────

    def _run_tool(self, tool_id: str):
        gs = self.engine.state
        if not gs:
            return
        t = self.engine.active_target
        if not t:
            self.terminal.print_line("[!] No target selected.", "err")
            return
        if t.get("name") == "LOCAL HOST" or self.engine._active_target_id == "localhost":
            self.terminal.print_line("[!] Cannot attack localhost.", "err")
            return

        if tool_id == "bounce":
            self._cmd_bounce()
            return
        if tool_id == "log_wipe":
            self._run_log_wipe()
            return

        # Check active mission
        am = self.engine.get_active_mission()
        if not am:
            missions = self.engine.get_available_missions()
            if missions:
                self.terminal.print_line("[*] No active contract. Accepting first available...", "sys")
                self.engine.accept_mission(missions[0]["id"])
                am = self.engine.get_active_mission()
            else:
                self.terminal.print_line("[!] No contracts available. Check MISSIONS.", "err")
                return

        # Launch minigame then execute exploit
        self._launch_exploit_sequence(tool_id, am)

    def _launch_exploit_sequence(self, tool_id, mission):
        from game.ui.exploit_window import ExploitWindow
        ExploitWindow(self.root, self.engine, self, tool_id, mission)

    def _run_log_wipe(self):
        if not self.engine.has_shell():
            self.terminal.print_line("[!] Need shell access first.", "err")
            return
        t = self.engine.active_target
        self.terminal.print_line("[*] Wiping event logs...", "sys")
        logs = ["/var/log/auth.log", "/var/log/syslog", "~/.bash_history",
                "/var/log/apache2/access.log", "/var/log/secure"]

        def _wipe():
            for log in logs:
                time.sleep(0.3)
                self.root.after(0, lambda l=log: self.terminal.print_line(f"[*] Shredding: {l}", "sys"))
            time.sleep(0.3)
            def _done():
                self.engine.reduce_trace(20.0)
                self.terminal.print_line("[+] Logs wiped. Trace reduced.", "success")
                self._refresh_stats()
            self.root.after(0, _done)

        threading.Thread(target=_wipe, daemon=True).start()

    # ─────────────────────────────────────────
    # STORY / DIALOGUE
    # ─────────────────────────────────────────

    def _show_chapter_intro(self, chapter_id=None):
        gs = self.engine.state
        if not gs:
            return
        cid = chapter_id or gs.current_chapter_id
        if cid in gs.chapter_intros_seen:
            return
        gs.chapter_intros_seen.add(cid)
        chapter = next((c for c in CHAPTERS if c["id"] == cid), None)
        if not chapter:
            return
        DialogueWindow(self.root, chapter["title"], chapter["intro"], "NEXUS DISPATCH")

    def _show_dialogue(self, dlg: dict):
        char = CHARACTERS.get(dlg.get("speaker", "mentor"), {})
        name = f"{char.get('portrait','?')} {char.get('name','?')} [{char.get('handle','?')}]"
        DialogueWindow(self.root, name, dlg["text"], dlg.get("speaker","").upper())

    def _prompt_edu(self, topic: str):
        content = EDU_CONTENT.get(topic)
        if not content:
            return
        ans = messagebox.askyesno(
            "Cybersecurity Codex",
            f"ARIA: 'This operation involved: {content['title']}.\n\n"
            f"{content['tldr']}\n\nOpen the Codex to learn more?'",
            parent=self.root
        )
        if ans:
            EduPanel(self.root, topic, content, self.engine)

    # ─────────────────────────────────────────
    # PANELS & REFRESH
    # ─────────────────────────────────────────

    def _panel_header(self, parent, text):
        lbl = tk.Label(parent, text=text, bg=C["bg"], fg=C["green_dim"],
                       font=self.font_hdr, anchor="w", padx=8, pady=4)
        return lbl

    def _update_intel_panel(self):
        for w in self.intel_frame.winfo_children():
            w.destroy()
        t = self.engine.active_target
        if not t:
            tk.Label(self.intel_frame, text="No target selected.", bg=C["bg2"],
                     fg=C["text_dim"], font=self.font_small).pack(anchor="w")
            return
        owned = self.engine.has_shell()
        fields = [
            (t["name"], C["text"], self.font_mono_b),
            (t["ip"], C["cyan"], self.font_small),
            (t["os"], C["text"], self.font_small),
            (f"SECURITY: {t['sec_label']}", C["red"] if t["sec_level"] >= 3 else C["amber"] if t["sec_level"] == 2 else C["green"], self.font_small),
            (f"PORTS: {', '.join(str(p) for p in t['ports'])}", C["cyan"], self.font_small),
        ]
        panel_w = max(200, self.intel_frame.winfo_width() - 20)
        for text, fg, fnt in fields:
            tk.Label(self.intel_frame, text=text, bg=C["bg2"], fg=fg,
                     font=fnt, anchor="w", wraplength=panel_w).pack(anchor="w", pady=1)
        if owned:
            tk.Label(self.intel_frame, text="◉ ROOT ACCESS", bg=C["bg2"],
                     fg=C["green"], font=self.font_small).pack(anchor="w", pady=(4, 0))
        # Vulnerability hint
        vulns = t.get("vulns", [])
        if vulns:
            tk.Frame(self.intel_frame, bg=C["border"], height=1).pack(fill="x", pady=4)
            tk.Label(self.intel_frame, text="KNOWN VULNERABILITIES:", bg=C["bg2"],
                     fg=C["amber"], font=self.font_small).pack(anchor="w")
            for v in vulns[:3]:
                tk.Label(self.intel_frame, text=f"• {v}", bg=C["bg2"],
                         fg=C["amber"], font=self.font_small,
                         wraplength=panel_w, justify="left").pack(anchor="w", padx=4)

    def _update_prompt(self):
        owned = self.engine.has_shell()
        t = self.engine.active_target
        if t and owned:
            self.prompt_lbl.configure(text=f"{self.engine.state.player_handle}@{t['ip'].split('.')[0]}:~#")
        elif t:
            self.prompt_lbl.configure(text=f"{self.engine.state.player_handle}@localhost:~$")
        else:
            self.prompt_lbl.configure(text="nexus@localhost:~$")

    def _refresh_all(self):
        self._refresh_stats()
        self.network_panel.refresh()
        self.mission_panel.refresh()
        self._update_intel_panel()
        self._update_prompt()

    def _refresh_stats(self):
        gs = self.engine.state
        if not gs:
            return
        self.lbl_credits.configure(text=f"${gs.credits:,}")
        self.lbl_rep.configure(text=str(gs.rep))
        self.lbl_owned.configure(text=str(len(gs.owned_targets)))

        # Trace bar
        self.trace_canvas.delete("all")
        pct = gs.trace / 100.0
        colour = C["red"] if gs.trace > 70 else C["amber"] if gs.trace > 40 else C["green"]
        w = int(120 * pct)
        if w > 0:
            self.trace_canvas.create_rectangle(0, 0, w, 14, fill=colour, outline="")
        self.lbl_trace_pct.configure(text=f"{gs.trace:.0f}%", fg=colour)

    def _start_clock(self):
        def _tick():
            gs = self.engine.state
            if gs:
                self.lbl_time.configure(text=self.engine.format_play_time())
                # Passive trace decay if bouncing
                if gs.bouncing and gs.trace > 0:
                    gs.trace = max(0.0, gs.trace - 0.1)
                    self._refresh_stats()
            self.root.after(1000, _tick)
        _tick()

    def set_status(self, msg: str):
        self.status_msg.configure(text=msg)

    # ─────────────────────────────────────────
    # SAVE / LOAD
    # ─────────────────────────────────────────

    def _save_menu(self):
        if not self.engine.state:
            messagebox.showinfo("Save", "No game in progress.", parent=self.root)
            return
        win = tk.Toplevel(self.root)
        win.title("Save Game")
        win.configure(bg=C["bg"])
        win.geometry("380x320")
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="◈ SAVE GAME", bg=C["bg"], fg=C["green"],
                 font=self.font_title).pack(pady=12)

        for slot in range(1, 4):
            info = self.engine.get_save_info(slot)
            if info:
                text = f"Slot {slot}: {info['handle']}  |  {info['chapter'][:28]}  |  {info['play_time']}"
            else:
                text = f"Slot {slot}: [Empty]"
            tk.Button(win, text=text, bg=C["bg3"], fg=C["text_dim"],
                      font=self.font_mono_s, relief="flat", bd=1, padx=8, pady=8,
                      activebackground=C["green_dk"], activeforeground=C["green"],
                      cursor="hand2", anchor="w",
                      command=lambda s=slot, w=win: self._do_save(s, w)).pack(
                fill="x", padx=16, pady=3)

        tk.Button(win, text="[ CANCEL ]", bg=C["bg3"], fg=C["text_dim"],
                  font=self.font_small, relief="flat", command=win.destroy).pack(pady=8)

    def _do_save(self, slot, win):
        if self.engine.save_game(slot):
            messagebox.showinfo("Saved", f"Game saved to slot {slot}.", parent=win)
        win.destroy()

    def _load_menu(self):
        win = tk.Toplevel(self.root)
        win.title("Load Game")
        win.configure(bg=C["bg"])
        win.geometry("380x320")
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="◈ LOAD GAME", bg=C["bg"], fg=C["green"],
                 font=self.font_title).pack(pady=12)

        found = False
        for slot in range(1, 4):
            info = self.engine.get_save_info(slot)
            if info:
                found = True
                text = (f"Slot {slot}: {info['handle']}\n"
                        f"  {info['chapter']}\n"
                        f"  ${info['credits']:,}  |  {info['rep']} REP  |  {info['missions']} missions  |  {info['play_time']}")
                tk.Button(win, text=text, bg=C["bg3"], fg=C["text_dim"],
                          font=self.font_small, relief="flat", bd=1, padx=8, pady=6,
                          activebackground=C["green_dk"], activeforeground=C["green"],
                          cursor="hand2", justify="left",
                          command=lambda s=slot, w=win: self._do_load(s, w)).pack(
                    fill="x", padx=16, pady=3)
            else:
                tk.Label(win, text=f"Slot {slot}: [Empty]", bg=C["bg"],
                         fg=C["text_dim"], font=self.font_small).pack(padx=16, anchor="w")

        if not found:
            tk.Label(win, text="No saved games found.", bg=C["bg"],
                     fg=C["text_dim"], font=self.font_small).pack()

        tk.Button(win, text="[ CANCEL ]", bg=C["bg3"], fg=C["text_dim"],
                  font=self.font_small, relief="flat", command=win.destroy).pack(pady=8)

    def _do_load(self, slot, win):
        win.destroy()
        gs = self.engine.load_game(slot)
        if gs:
            try:
                self.title_frame.destroy()
            except Exception:
                pass
            self.game_frame.grid()
            self.root.grid_rowconfigure(1, weight=1)
            self._refresh_all()
            self._start_clock()
            self.terminal.print_line("", "out")
            self.terminal.print_line(f"[+] Save loaded. Welcome back, {gs.player_handle}.", "success")
            self.terminal.print_line("", "out")
            self.set_status(f"Save loaded — {gs.player_handle}")
        else:
            messagebox.showerror("Error", "Failed to load save.", parent=self.root)

    def _open_codex(self):
        if not self.engine.state:
            messagebox.showinfo("Codex", "Start a game first.", parent=self.root)
            return
        from game.ui.codex_window import CodexWindow
        CodexWindow(self.root, self.engine)

    def _open_help(self):
        from game.ui.help_window import HelpWindow
        HelpWindow(self.root)

    def _show_howto(self):
        text = (
            "HOW TO PLAY — NEXUS: ZERO DAY\n\n"
            "You are gh0st — a former network engineer investigating a global conspiracy.\n\n"
            "1. ACCEPT A CONTRACT from the right panel, or type 'missions' in the terminal.\n\n"
            "2. SELECT YOUR TARGET in the network map on the left. The target will be shown\n"
            "   in the TARGET INTEL panel.\n\n"
            "3. RECON FIRST — use 'scan' or 'nmap' to identify open ports and vulnerabilities.\n\n"
            "4. USE THE TOOLKIT — click exploit buttons on the left, or type 'exploit <name>'.\n"
            "   Exploits trigger interactive minigames that affect your success rate.\n\n"
            "5. COMPLETE YOUR OBJECTIVE — gain shell access, exfiltrate data, or plant implants\n"
            "   depending on the mission.\n\n"
            "6. MANAGE YOUR TRACE — every action increases your trace level. Hit 100% and you\n"
            "   are BUSTED. Use 'bounce' routing and log wipes to reduce trace.\n\n"
            "7. READ THE CODEX — after each mission, you'll be prompted to read about the real\n"
            "   cybersecurity concepts you just used. This earns +2 REP per topic.\n\n"
            "8. SAVE OFTEN — use the SAVE button or type 'save' in the terminal.\n\n"
            "Good luck. The network is the target."
        )
        win = tk.Toplevel(self.root)
        win.title("How to Play")
        win.configure(bg=C["bg"])
        win.geometry("560x500")
        win.transient(self.root)

        tk.Label(win, text="◈ HOW TO PLAY", bg=C["bg"], fg=C["green"],
                 font=self.font_title).pack(pady=12)

        txt = tk.Text(win, bg=C["bg2"], fg=C["text"], font=self.font_mono_s,
                      relief="flat", wrap="word", padx=16, pady=12)
        txt.pack(fill="both", expand=True, padx=16)
        txt.insert("1.0", text)
        txt.configure(state="disabled")

        tk.Button(win, text="[ CLOSE ]", bg=C["bg3"], fg=C["text_dim"],
                  font=self.font_small, relief="flat",
                  command=win.destroy).pack(pady=8)

    def _restart(self):
        if messagebox.askyesno("Restart", "Wipe current run and restart?", parent=self.root):
            self.engine.state.trace = 0.0
            self.engine.state.owned_targets = []
            self.engine.state.completed_missions = []
            self.engine.state.active_mission_id = None
            self.engine.state.credits = 0
            self.engine.state.rep = 0
            self.engine.state.current_chapter_id = "ch1"
            self.engine._unlock_chapter_targets("ch1")
            self.engine.state.bouncing = False
            self.engine.state.chapter_intros_seen = set()
            self.terminal.clear()
            self._refresh_all()
            self.terminal.print_line("[+] System reset. Starting fresh.", "success")
            self.set_status("System reset.")

    def _quit(self):
        if messagebox.askyesno("Quit", "Save before quitting?", parent=self.root):
            self._save_menu()
        else:
            self.root.destroy()
