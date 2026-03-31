"""NEXUS — Full Codex Browser"""
import tkinter as tk
from tkinter import font as tkfont
from game.story import EDU_CONTENT

C = {
    "bg": "#080c0a", "bg2": "#0d1410", "bg3": "#111a16",
    "green": "#00ff88", "green_dim": "#00aa55", "green_dk": "#003322",
    "amber": "#ffaa00", "red": "#ff3344", "cyan": "#00ccff",
    "text": "#c0e8d0", "text_dim": "#4a7a5a", "border": "#1a3328",
}


class CodexWindow:
    def __init__(self, parent, engine):
        self.engine = engine
        win = tk.Toplevel(parent)
        win.title("NEXUS Codex — Cybersecurity Knowledge Base")
        win.configure(bg=C["bg"])
        win.geometry("900x620")
        win.transient(parent)
        win.resizable(True, True)

        font_title = tkfont.Font(family="Courier New", size=13, weight="bold")
        font_hdr   = tkfont.Font(family="Courier New", size=11, weight="bold")
        font_mono  = tkfont.Font(family="Courier New", size=10)
        font_small = tkfont.Font(family="Courier New", size=9)

        # Title bar
        tk.Label(win, text="◈ NEXUS CODEX — CYBERSECURITY KNOWLEDGE BASE",
                 bg=C["bg2"], fg=C["green"], font=font_hdr, pady=6).pack(fill="x")

        main = tk.Frame(win, bg=C["bg"])
        main.pack(fill="both", expand=True)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)

        # Left: topic list
        left = tk.Frame(main, bg=C["bg2"], width=220)
        left.grid(row=0, column=0, sticky="nsew")
        left.grid_propagate(False)

        tk.Label(left, text="TOPICS", bg=C["bg2"], fg=C["green_dim"],
                 font=font_small, pady=4).pack(fill="x", padx=8)
        tk.Frame(left, bg=C["border"], height=1).pack(fill="x")

        topic_list_frame = tk.Frame(left, bg=C["bg2"])
        topic_list_frame.pack(fill="both", expand=True)

        self.topic_buttons = {}
        for tid, content in EDU_CONTENT.items():
            read = tid in engine.state.edu_topics_read
            btn = tk.Button(
                topic_list_frame,
                text=("✓ " if read else "  ") + content["title"][:28],
                bg=C["bg2"], fg=C["green"] if read else C["text_dim"],
                font=font_small, relief="flat", anchor="w", padx=8, pady=5,
                activebackground=C["green_dk"], activeforeground=C["green"],
                cursor="hand2",
                command=lambda t=tid: self._show_topic(t)
            )
            btn.pack(fill="x")
            self.topic_buttons[tid] = btn

        # Right: content area
        right = tk.Frame(main, bg=C["bg"])
        right.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)
        right.grid_rowconfigure(0, weight=1)
        right.grid_columnconfigure(0, weight=1)

        self.content_canvas = tk.Canvas(right, bg=C["bg"], highlightthickness=0)
        sb = tk.Scrollbar(right, orient="vertical", command=self.content_canvas.yview,
                          bg=C["bg"], width=6)
        self.content_canvas.configure(yscrollcommand=sb.set)
        self.content_canvas.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")

        self.content_inner = tk.Frame(self.content_canvas, bg=C["bg"])
        self._cw = self.content_canvas.create_window((0, 0), window=self.content_inner, anchor="nw")
        self.content_inner.bind("<Configure>",
            lambda e: self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all")))
        self.content_canvas.bind("<Configure>",
            lambda e: self.content_canvas.itemconfig(self._cw, width=e.width))

        self.font_title = font_title
        self.font_hdr   = font_hdr
        self.font_mono  = font_mono
        self.font_small = font_small

        # Show first topic
        first = next(iter(EDU_CONTENT))
        self._show_topic(first)

        tk.Button(win, text="[ CLOSE ]", bg=C["bg3"], fg=C["text_dim"],
                  font=font_small, relief="flat", cursor="hand2",
                  command=win.destroy).pack(pady=6)

    def _show_topic(self, topic_id):
        content = EDU_CONTENT.get(topic_id)
        if not content:
            return

        for w in self.content_inner.winfo_children():
            w.destroy()

        self.content_canvas.yview_moveto(0)

        tk.Label(self.content_inner, text=content["title"], bg=C["bg"],
                 fg=C["green"], font=self.font_title, anchor="w",
                 pady=8).pack(fill="x", padx=8)

        tk.Label(self.content_inner,
                 text=f"TL;DR — {content['tldr']}",
                 bg=C["bg3"], fg=C["amber"], font=self.font_mono,
                 anchor="w", justify="left", wraplength=600,
                 padx=12, pady=8).pack(fill="x", padx=8, pady=4)

        for section in content.get("sections", []):
            tk.Label(self.content_inner, text=section["heading"],
                     bg=C["bg"], fg=C["cyan"], font=self.font_hdr,
                     anchor="w", pady=4).pack(fill="x", padx=8)
            tk.Label(self.content_inner, text=section["body"],
                     bg=C["bg"], fg=C["text"], font=self.font_mono,
                     anchor="w", justify="left", wraplength=630).pack(fill="x", padx=20, pady=(0, 6))
            tk.Frame(self.content_inner, bg=C["border"], height=1).pack(fill="x", padx=8, pady=2)

        rw = content.get("real_world")
        if rw:
            tk.Label(self.content_inner, text="◈ REAL WORLD CASE",
                     bg=C["bg"], fg=C["amber"], font=self.font_hdr,
                     anchor="w").pack(fill="x", padx=8, pady=(4, 0))
            tk.Label(self.content_inner, text=rw,
                     bg=C["bg3"], fg=C["amber"], font=self.font_mono,
                     anchor="w", justify="left", wraplength=630,
                     padx=12, pady=8).pack(fill="x", padx=8, pady=4)

        tools = content.get("tools", [])
        if tools:
            tk.Label(self.content_inner, text="◈ RELATED TOOLS",
                     bg=C["bg"], fg=C["green_dim"], font=self.font_hdr,
                     anchor="w").pack(fill="x", padx=8, pady=(4, 0))
            tk.Label(self.content_inner,
                     text="  " + "   •   ".join(tools),
                     bg=C["bg"], fg=C["text_dim"], font=self.font_small,
                     anchor="w").pack(fill="x", padx=20, pady=(0, 8))

        if topic_id not in self.engine.state.edu_topics_read:
            self.engine.mark_edu_read(topic_id)
            tk.Label(self.content_inner,
                     text="✓ +2 REP — Codex entry read",
                     bg=C["green_dk"], fg=C["green"], font=self.font_small,
                     pady=4).pack(fill="x", padx=8, pady=4)
            # Update button
            btn = self.topic_buttons.get(topic_id)
            if btn:
                content_obj = EDU_CONTENT[topic_id]
                btn.configure(text="✓ " + content_obj["title"][:28], fg=C["green"])
