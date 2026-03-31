"""NEXUS — Education (Codex) Panel"""
import tkinter as tk
from tkinter import font as tkfont

C = {
    "bg": "#080c0a", "bg2": "#0d1410", "bg3": "#111a16",
    "green": "#00ff88", "green_dim": "#00aa55", "green_dk": "#003322",
    "amber": "#ffaa00", "red": "#ff3344", "cyan": "#00ccff",
    "text": "#c0e8d0", "text_dim": "#4a7a5a", "border": "#1a3328",
}


class EduPanel:
    def __init__(self, parent, topic_id: str, content: dict, engine=None):
        win = tk.Toplevel(parent)
        win.title(f"Codex — {content['title']}")
        win.configure(bg=C["bg"])
        win.geometry("700x560")
        win.transient(parent)
        win.resizable(True, True)

        font_title = tkfont.Font(family="Courier New", size=13, weight="bold")
        font_hdr   = tkfont.Font(family="Courier New", size=11, weight="bold")
        font_mono  = tkfont.Font(family="Courier New", size=10)
        font_small = tkfont.Font(family="Courier New", size=9)

        # Header
        tk.Label(win, text="◈ NEXUS CODEX — CYBERSECURITY EDUCATION",
                 bg=C["bg2"], fg=C["green_dim"], font=font_small,
                 pady=5).pack(fill="x", padx=0)

        tk.Label(win, text=content["title"], bg=C["bg"], fg=C["green"],
                 font=font_title, pady=6).pack(fill="x", padx=16)

        tk.Label(win, text=f"TL;DR — {content['tldr']}", bg=C["bg"],
                 fg=C["amber"], font=font_mono, pady=4,
                 wraplength=660, justify="left").pack(fill="x", padx=16)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=16, pady=4)

        # Scrollable body
        canvas = tk.Canvas(win, bg=C["bg"], highlightthickness=0)
        sb = tk.Scrollbar(win, orient="vertical", command=canvas.yview,
                          bg=C["bg"], width=6)
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        inner = tk.Frame(canvas, bg=C["bg"])
        cw = canvas.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(cw, width=e.width))

        for section in content.get("sections", []):
            tk.Label(inner, text=section["heading"], bg=C["bg"],
                     fg=C["cyan"], font=font_hdr, anchor="w",
                     pady=6).pack(fill="x", padx=16)
            tk.Label(inner, text=section["body"], bg=C["bg"],
                     fg=C["text"], font=font_mono,
                     anchor="w", justify="left", wraplength=640,
                     pady=2).pack(fill="x", padx=24)
            tk.Frame(inner, bg=C["border"], height=1).pack(fill="x", padx=16, pady=6)

        # Real world example
        rw = content.get("real_world")
        if rw:
            tk.Label(inner, text="◈ REAL WORLD CASE", bg=C["bg"],
                     fg=C["amber"], font=font_hdr, anchor="w").pack(fill="x", padx=16)
            tk.Label(inner, text=rw, bg=C["bg3"], fg=C["amber"],
                     font=font_mono, anchor="w", justify="left",
                     wraplength=640, padx=16, pady=8).pack(fill="x", padx=16, pady=4)

        # Tools
        tools = content.get("tools", [])
        if tools:
            tk.Label(inner, text="◈ TOOLS", bg=C["bg"],
                     fg=C["green_dim"], font=font_hdr, anchor="w",
                     pady=6).pack(fill="x", padx=16)
            tk.Label(inner, text="  " + "   •   ".join(tools), bg=C["bg"],
                     fg=C["text_dim"], font=font_small, anchor="w").pack(fill="x", padx=24)

        # Mark as read
        if engine and topic_id not in engine.state.edu_topics_read:
            engine.mark_edu_read(topic_id)
            tk.Label(inner, text="+2 REP awarded for reading this Codex entry.",
                     bg=C["green_dk"], fg=C["green"], font=font_small,
                     pady=4).pack(fill="x", padx=16, pady=8)

        tk.Button(win, text="[ CLOSE CODEX ]",
                  bg=C["bg3"], fg=C["green_dim"], font=font_small,
                  relief="flat", pady=5, cursor="hand2",
                  activebackground=C["green_dk"], activeforeground=C["green"],
                  command=win.destroy).pack(pady=6, side="bottom")
