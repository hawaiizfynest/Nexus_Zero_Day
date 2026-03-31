"""NEXUS — Dialogue / Story Window"""
import tkinter as tk
from tkinter import font as tkfont

C = {
    "bg": "#080c0a", "bg2": "#0d1410", "bg3": "#111a16",
    "green": "#00ff88", "green_dim": "#00aa55", "green_dk": "#003322",
    "amber": "#ffaa00", "red": "#ff3344", "cyan": "#00ccff",
    "text": "#c0e8d0", "text_dim": "#4a7a5a", "border": "#1a3328",
}


class DialogueWindow:
    def __init__(self, parent, title: str, body: str, speaker: str = ""):
        win = tk.Toplevel(parent)
        win.title("Transmission")
        win.configure(bg=C["bg"])
        win.geometry("640x480")
        win.transient(parent)
        win.grab_set()
        win.resizable(True, True)

        font_title = tkfont.Font(family="Courier New", size=12, weight="bold")
        font_mono  = tkfont.Font(family="Courier New", size=11)
        font_small = tkfont.Font(family="Courier New", size=9)

        # Header
        hdr = tk.Frame(win, bg=C["bg2"])
        hdr.pack(fill="x")
        tk.Label(hdr, text="◈ ENCRYPTED TRANSMISSION", bg=C["bg2"],
                 fg=C["green_dim"], font=font_small, pady=4).pack(side="left", padx=12)
        tk.Label(hdr, text=f"FROM: {speaker}", bg=C["bg2"],
                 fg=C["amber"], font=font_small).pack(side="right", padx=12)

        # Speaker
        tk.Label(win, text=title, bg=C["bg"], fg=C["green"],
                 font=font_title, pady=8).pack(fill="x", padx=16)

        tk.Frame(win, bg=C["border"], height=1).pack(fill="x", padx=16)

        # Body text — typewriter effect
        text_frame = tk.Frame(win, bg=C["bg"])
        text_frame.pack(fill="both", expand=True, padx=16, pady=12)

        self.text_widget = tk.Text(
            text_frame, bg=C["bg"], fg=C["text"], font=font_mono,
            relief="flat", wrap="word", padx=8, pady=8,
            state="disabled", cursor="arrow",
        )
        self.text_widget.pack(fill="both", expand=True)
        self.text_widget.tag_configure("body", foreground=C["text"])

        # Close button
        tk.Button(win, text="[ ACKNOWLEDGE TRANSMISSION ]",
                  bg=C["bg3"], fg=C["green_dim"], font=font_small,
                  relief="flat", bd=1, pady=6, cursor="hand2",
                  activebackground=C["green_dk"], activeforeground=C["green"],
                  command=win.destroy).pack(pady=8)

        # Typewriter
        self._body = body
        self._idx = 0
        self._widget = self.text_widget
        self._win = win
        win.after(100, self._type_next)

    def _type_next(self):
        if self._idx >= len(self._body):
            return
        chunk = self._body[self._idx:self._idx + 3]
        self._widget.configure(state="normal")
        self._widget.insert("end", chunk, "body")
        self._widget.configure(state="disabled")
        self._widget.see("end")
        self._idx += 3
        delay = 18 if chunk.strip() else 8
        self._win.after(delay, self._type_next)
