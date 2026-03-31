"""NEXUS — Mission Panel"""
import tkinter as tk
from tkinter import font as tkfont
from game.story import MISSIONS, TARGETS

C = {
    "bg": "#080c0a", "bg2": "#0d1410", "bg3": "#111a16",
    "green": "#00ff88", "green_dim": "#00aa55", "green_dk": "#003322",
    "amber": "#ffaa00", "red": "#ff3344", "cyan": "#00ccff",
    "text": "#c0e8d0", "text_dim": "#4a7a5a", "border": "#1a3328",
}

DIFF_COLORS = {"tutorial": "#00ff88", "easy": "#66ff33", "medium": "#ffaa00",
               "hard": "#ff6600", "elite": "#cc44ff"}


class MissionPanel:
    def __init__(self, parent, engine, app):
        self.engine = engine
        self.app = app
        self.frame = tk.Frame(parent, bg=C["bg2"])
        self.frame.grid_columnconfigure(0, weight=1)

        font_s = tkfont.Font(family="Courier New", size=9)
        font_m = tkfont.Font(family="Courier New", size=10)
        font_b = tkfont.Font(family="Courier New", size=10, weight="bold")

        self.canvas = tk.Canvas(self.frame, bg=C["bg2"], highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical",
                                       command=self.canvas.yview,
                                       bg=C["bg2"], troughcolor=C["bg2"], width=6)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.frame.grid_rowconfigure(0, weight=1)

        self.inner = tk.Frame(self.canvas, bg=C["bg2"])
        self.canvas_window = self.canvas.create_window((0, 0), window=self.inner,
                                                        anchor="nw")
        self.inner.bind("<Configure>", self._on_inner_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>",   lambda e: self.canvas.yview_scroll(-1, "units"))
        self.canvas.bind("<Button-5>",   lambda e: self.canvas.yview_scroll( 1, "units"))

        self.font_s = font_s
        self.font_m = font_m
        self.font_b = font_b
        self.refresh()

    def _on_inner_configure(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, e):
        self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    def _on_canvas_configure(self, e):
        self.canvas.itemconfig(self.canvas_window, width=e.width)

    def refresh(self):
        for w in self.inner.winfo_children():
            w.destroy()

        gs = self.engine.state
        if not gs:
            return

        missions = self.engine.get_available_missions()
        active_id = gs.active_mission_id
        done_ids = set(gs.completed_missions)

        if not missions:
            tk.Label(self.inner, text="No contracts available.\nComplete current chapter.",
                     bg=C["bg2"], fg=C["text_dim"], font=self.font_s,
                     justify="center").pack(pady=12, padx=8)
            return

        for m in missions:
            is_active = m["id"] == active_id
            is_done = m["id"] in done_ids
            tgt = TARGETS.get(m["target_id"], {})
            diff_col = DIFF_COLORS.get(m["difficulty"], C["text_dim"])
            border_col = C["green"] if is_active else C["border"]
            bg_col = C["green_dk"] if is_active else C["bg3"]

            card = tk.Frame(self.inner, bg=bg_col, bd=1, relief="solid",
                            highlightbackground=border_col, highlightthickness=1)
            card.pack(fill="x", padx=6, pady=3)

            # Title — wraplength tracks canvas width dynamically
            card_w = max(160, self.canvas.winfo_width() - 32)
            title_text = ("✓ " if is_done else "► " if is_active else "") + m["title"]
            tk.Label(card, text=title_text, bg=bg_col,
                     fg=C["green"] if is_active else C["text_dim"] if is_done else C["text"],
                     font=self.font_m, anchor="w", wraplength=card_w, justify="left").pack(
                fill="x", padx=8, pady=(6, 2))

            tk.Label(card, text=f"TARGET: {tgt.get('name', '?')[:28]}",
                     bg=bg_col, fg=C["text_dim"], font=self.font_s, anchor="w").pack(
                fill="x", padx=8)

            btm = tk.Frame(card, bg=bg_col)
            btm.pack(fill="x", padx=8, pady=(2, 6))
            tk.Label(btm, text=f"${m['reward_credits']:,} + {m['reward_rep']} REP",
                     bg=bg_col, fg=C["amber"], font=self.font_s).pack(side="left")
            tk.Label(btm, text=f"[{m['difficulty'].upper()}]",
                     bg=bg_col, fg=diff_col, font=self.font_s).pack(side="right")

            if not is_active and not is_done:
                card.bind("<Button-1>", lambda e, mid=m["id"]: self._accept(mid))
                for child in card.winfo_children():
                    child.bind("<Button-1>", lambda e, mid=m["id"]: self._accept(mid))
                card.configure(cursor="hand2")

    def _accept(self, mission_id):
        self.engine.accept_mission(mission_id)
        self.refresh()
