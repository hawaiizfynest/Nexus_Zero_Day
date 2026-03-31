"""
NEXUS: Zero Day — Terminal Widget
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

TAG_COLORS = {
    "out":     C["text"],
    "cmd":     C["green"],
    "sys":     C["text_dim"],
    "success": C["green"],
    "err":     C["red"],
    "warn":    C["amber"],
    "info":    C["cyan"],
    "hdr":     C["green"],
    "dim":     C["text_dim"],
    "amber":   C["amber"],
    "purple":  C["purple"],
}


class TerminalWidget:
    def __init__(self, parent, engine, app):
        self.engine = engine
        self.app = app

        self.frame = tk.Frame(parent, bg=C["bg"])
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        font_mono = tkfont.Font(family="Courier New", size=11)

        self.text = tk.Text(
            self.frame,
            bg=C["bg"], fg=C["text"],
            font=font_mono,
            relief="flat", bd=0,
            wrap="word",
            state="disabled",
            padx=12, pady=8,
            selectbackground=C["green_dk"],
            insertbackground=C["green"],
            cursor="arrow",
        )
        self.text.grid(row=0, column=0, sticky="nsew")

        sb = tk.Scrollbar(self.frame, orient="vertical", command=self.text.yview,
                          bg=C["bg"], troughcolor=C["bg2"], width=8)
        sb.grid(row=0, column=1, sticky="ns")
        self.text.configure(yscrollcommand=sb.set)

        for tag, fg in TAG_COLORS.items():
            self.text.tag_configure(tag, foreground=fg)
        self.text.tag_configure("hdr", foreground=C["green"],
                                font=tkfont.Font(family="Courier New", size=11, weight="bold"))

        self._print_boot_sequence()

    def _print_boot_sequence(self):
        lines = [
            ("███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗", "success"),
            ("████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝", "success"),
            ("██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗", "success"),
            ("██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║", "success"),
            ("██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║", "success"),
            ("╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝", "success"),
            ("", "out"),
            ("  Z E R O   D A Y  —  Cybersecurity Simulation", "info"),
            ("", "out"),
            ("  Type 'help' for commands.  'missions' to see contracts.", "sys"),
            ("  Start in the STORY tab for narrative context.", "sys"),
            ("", "out"),
        ]
        for text, tag in lines:
            self.print_line(text, tag)

    def print_line(self, text: str, tag: str = "out"):
        self.text.configure(state="normal")
        self.text.insert("end", text + "\n", tag)
        self.text.configure(state="disabled")
        self.text.see("end")

    def clear(self):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.configure(state="disabled")
