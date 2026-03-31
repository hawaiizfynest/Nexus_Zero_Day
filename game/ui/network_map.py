"""NEXUS — Network Map Panel"""
import tkinter as tk
from tkinter import font as tkfont
from game.story import TARGETS

C = {
    "bg": "#080c0a", "bg2": "#0d1410", "bg3": "#111a16",
    "green": "#00ff88", "green_dim": "#00aa55", "green_dk": "#003322",
    "amber": "#ffaa00", "red": "#ff3344", "cyan": "#00ccff",
    "text": "#c0e8d0", "text_dim": "#4a7a5a", "border": "#1a3328",
}

SEC_COLORS = {0: "#4a7a5a", 1: "#66ff33", 2: "#ffaa00", 3: "#ff6600", 4: "#ff3344"}
SEC_LABELS = {0: "NONE", 1: "LOW", 2: "MED", 3: "HIGH", 4: "CRIT"}


class NetworkMapPanel:
    def __init__(self, parent, engine, app):
        self.engine = engine
        self.app = app

        self.frame = tk.Frame(parent, bg=C["bg2"])
        self.frame.grid_columnconfigure(0, weight=1)

        font_s = tkfont.Font(family="Courier New", size=9)
        font_m = tkfont.Font(family="Courier New", size=10)
        self.font_s = font_s
        self.font_m = font_m

        self.canvas = tk.Canvas(self.frame, bg=C["bg2"], highlightthickness=0)
        sb = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview,
                          bg=C["bg2"], width=5)
        self.canvas.configure(yscrollcommand=sb.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")
        self.frame.grid_rowconfigure(0, weight=1)

        self.inner = tk.Frame(self.canvas, bg=C["bg2"])
        self._win = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.inner.bind("<Configure>",
                        lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>",
                         lambda e: self.canvas.itemconfig(self._win, width=e.width))
        self.canvas.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self.canvas.bind("<Button-4>",   lambda e: self.canvas.yview_scroll(-1, "units"))
        self.canvas.bind("<Button-5>",   lambda e: self.canvas.yview_scroll( 1, "units"))
        self.refresh()

    def refresh(self):
        for w in self.inner.winfo_children():
            w.destroy()

        gs = self.engine.state
        if not gs:
            return

        for tid in gs.discovered_targets:
            t = TARGETS.get(tid)
            if not t:
                continue
            is_active = self.engine._active_target_id == tid
            owned = tid in gs.owned_targets
            sec = t["sec_level"]
            sec_col = SEC_COLORS.get(sec, C["text_dim"])
            border = C["green"] if is_active else C["border"]
            bg = C["green_dk"] if is_active else C["bg3"]

            row = tk.Frame(self.inner, bg=bg, highlightbackground=border,
                           highlightthickness=1, cursor="hand2")
            row.pack(fill="x", padx=4, pady=2)
            row.bind("<Button-1>", lambda e, t_id=tid: self._select(t_id))

            name_lbl = tk.Label(row, text=t["name"][:24], bg=bg,
                                fg=C["green"] if is_active else C["text"],
                                font=self.font_m, anchor="w")
            name_lbl.pack(fill="x", padx=6, pady=(4, 0))
            name_lbl.bind("<Button-1>", lambda e, t_id=tid: self._select(t_id))

            ip_lbl = tk.Label(row, text=t["ip"], bg=bg, fg=C["cyan"],
                              font=self.font_s, anchor="w")
            ip_lbl.pack(fill="x", padx=6)
            ip_lbl.bind("<Button-1>", lambda e, t_id=tid: self._select(t_id))

            badge_row = tk.Frame(row, bg=bg)
            badge_row.pack(fill="x", padx=6, pady=(2, 4))
            badge_row.bind("<Button-1>", lambda e, t_id=tid: self._select(t_id))

            self._badge(badge_row, t["type"][:6].upper(), C["cyan"])
            self._badge(badge_row, SEC_LABELS[sec], sec_col)
            if owned:
                self._badge(badge_row, "ROOT", C["green"])

    def _badge(self, parent, text, color):
        lbl = tk.Label(parent, text=text, bg=C["bg"], fg=color,
                       font=tkfont.Font(family="Courier New", size=8),
                       padx=4, pady=1, relief="solid", bd=1)
        lbl.pack(side="left", padx=2)

    def _select(self, tid):
        self.engine.set_active_target(tid)
        self.refresh()
