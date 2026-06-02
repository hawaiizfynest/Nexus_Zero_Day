"""NEXUS — Skill Tree Window

Visual progression tree. Players spend REP on permanent upgrades organised
into five branches: Recon, Exploit, Stealth, Forensics, Resource.
"""
import tkinter as tk
from tkinter import font as tkfont, messagebox
from game.skill_tree import SKILLS, BRANCHES, get_branch_skills, can_unlock

C = {
    "bg":         "#080c0a",
    "bg2":        "#0d1410",
    "bg3":        "#111a16",
    "bg_hover":   "#152821",
    "green":      "#00ff88",
    "green_dim":  "#00aa55",
    "green_dk":   "#003322",
    "amber":      "#ffaa00",
    "red":        "#ff3344",
    "cyan":       "#00ccff",
    "white":      "#ffffff",
    "text":       "#c0e8d0",
    "text_dim":   "#4a7a5a",
    "text_lock":  "#3a4a40",
    "border":     "#1a3328",
}


class SkillTreeWindow:
    def __init__(self, parent, engine):
        self.engine = engine
        self.parent = parent
        self.selected_skill_id = None

        self.win = tk.Toplevel(parent)
        self.win.title("NEXUS — Operator Progression")
        self.win.configure(bg=C["bg"])
        self.win.geometry("1080x720")
        self.win.transient(parent)
        self.win.resizable(True, True)

        self.font_title = tkfont.Font(family="Courier New", size=14, weight="bold")
        self.font_hdr   = tkfont.Font(family="Courier New", size=11, weight="bold")
        self.font_mono  = tkfont.Font(family="Courier New", size=10)
        self.font_small = tkfont.Font(family="Courier New", size=9)
        self.font_tier  = tkfont.Font(family="Courier New", size=9, weight="bold")
        self.font_skill = tkfont.Font(family="Courier New", size=10, weight="bold")
        self.font_body  = tkfont.Font(family="Georgia", size=10)
        self.font_lore  = tkfont.Font(family="Georgia", size=9, slant="italic")

        # ── Title bar ────────────────────────────────────────
        topbar = tk.Frame(self.win, bg=C["bg2"])
        topbar.pack(fill="x")
        tk.Label(topbar, text="◈ OPERATOR PROGRESSION TREE",
                 bg=C["bg2"], fg=C["green"], font=self.font_hdr,
                 pady=6).pack(side="left", padx=12)

        self.rep_label = tk.Label(topbar, text="", bg=C["bg2"], fg=C["amber"],
                                   font=self.font_hdr, pady=6)
        self.rep_label.pack(side="right", padx=12)

        tk.Frame(self.win, bg=C["border"], height=1).pack(fill="x")

        # ── Main layout ──────────────────────────────────────
        main = tk.Frame(self.win, bg=C["bg"])
        main.pack(fill="both", expand=True)
        main.grid_columnconfigure(0, weight=3)
        main.grid_columnconfigure(1, weight=2)
        main.grid_rowconfigure(0, weight=1)

        # Left: skill tree canvas
        tree_container = tk.Frame(main, bg=C["bg"])
        tree_container.grid(row=0, column=0, sticky="nsew", padx=(8, 4), pady=8)

        self.canvas = tk.Canvas(tree_container, bg=C["bg2"], highlightthickness=1,
                                 highlightbackground=C["border"])
        self.canvas.pack(fill="both", expand=True)

        # Right: skill detail panel
        self.detail_frame = tk.Frame(main, bg=C["bg2"], highlightthickness=1,
                                      highlightbackground=C["border"])
        self.detail_frame.grid(row=0, column=1, sticky="nsew", padx=(4, 8), pady=8)

        # Status bar at bottom
        statusbar = tk.Frame(self.win, bg=C["bg2"])
        statusbar.pack(fill="x")
        tk.Frame(self.win, bg=C["border"], height=1).pack(fill="x", before=statusbar)

        self.status_label = tk.Label(statusbar, text="Select a skill to view details",
                                      bg=C["bg2"], fg=C["text_dim"],
                                      font=self.font_small, pady=6)
        self.status_label.pack(side="left", padx=12)

        tk.Button(statusbar, text="CLOSE", bg=C["bg3"], fg=C["text"],
                  font=self.font_small, bd=0, padx=14, pady=4,
                  activebackground=C["green_dk"], activeforeground=C["green"],
                  command=self.win.destroy).pack(side="right", padx=8, pady=4)

        # Render
        self._build_detail_placeholder()
        self.win.after(50, self._render_tree)
        self._refresh_rep()

    # ── REP display ──────────────────────────────────────────
    def _refresh_rep(self):
        rep = self.engine.state.rep
        unlocked = len(self.engine.state.unlocked_skills)
        total = len(SKILLS)
        self.rep_label.config(text=f"REP: {rep}   |   SKILLS: {unlocked}/{total}")

    # ── Tree rendering ───────────────────────────────────────
    def _render_tree(self):
        self.canvas.delete("all")
        self.canvas.update_idletasks()

        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        if canvas_w < 100:
            self.win.after(100, self._render_tree)
            return

        # Layout: 5 vertical branches, 4 tiers each
        branches = list(BRANCHES.keys())
        branch_count = len(branches)
        col_width = canvas_w / branch_count

        tier_count = 4
        margin_top = 50
        margin_bottom = 30
        usable_h = canvas_h - margin_top - margin_bottom
        row_height = usable_h / tier_count

        node_w = min(int(col_width * 0.78), 165)
        node_h = int(row_height * 0.68)

        unlocked = set(self.engine.state.unlocked_skills)
        rep = self.engine.state.rep

        # Draw branch headers
        for i, branch_id in enumerate(branches):
            cx = col_width * (i + 0.5)
            meta = BRANCHES[branch_id]
            self.canvas.create_text(
                cx, 22,
                text=meta["name"],
                fill=meta["color"],
                font=self.font_tier,
                anchor="center",
            )
            self.canvas.create_text(
                cx, 38,
                text=meta["desc"],
                fill=C["text_dim"],
                font=self.font_small,
                anchor="center",
            )

        # Draw connector lines first (so they sit under nodes)
        for i, branch_id in enumerate(branches):
            skills = get_branch_skills(branch_id)
            cx = col_width * (i + 0.5)
            for j in range(len(skills) - 1):
                y1 = margin_top + row_height * (j + 0.5)
                y2 = margin_top + row_height * (j + 1.5)
                _, this_skill = skills[j]
                _, next_skill = skills[j+1]
                this_id = skills[j][0]
                next_id = skills[j+1][0]

                if next_id in unlocked:
                    color = BRANCHES[branch_id]["color"]
                elif this_id in unlocked:
                    color = C["green_dim"]
                else:
                    color = C["text_lock"]
                self.canvas.create_line(cx, y1 + node_h/2, cx, y2 - node_h/2,
                                        fill=color, width=2, dash=(4, 3))

        # Draw nodes
        self._node_hitboxes = []
        for i, branch_id in enumerate(branches):
            skills = get_branch_skills(branch_id)
            cx = col_width * (i + 0.5)
            branch_color = BRANCHES[branch_id]["color"]

            for j, (skill_id, skill) in enumerate(skills):
                y = margin_top + row_height * (j + 0.5)
                x1 = cx - node_w / 2
                y1 = y - node_h / 2
                x2 = cx + node_w / 2
                y2 = y + node_h / 2

                is_unlocked = skill_id in unlocked
                ok, _ = can_unlock(skill_id, unlocked, rep)

                if is_unlocked:
                    fill = branch_color
                    text_color = C["bg"]
                    border = branch_color
                    cost_color = C["bg"]
                elif ok:
                    fill = C["bg3"]
                    text_color = branch_color
                    border = branch_color
                    cost_color = C["amber"]
                else:
                    fill = C["bg2"]
                    text_color = C["text_lock"]
                    border = C["border"]
                    cost_color = C["text_lock"]

                rect = self.canvas.create_rectangle(x1, y1, x2, y2,
                    fill=fill, outline=border, width=2)
                title = self.canvas.create_text(
                    cx, y - 12, text=skill["name"], fill=text_color,
                    font=self.font_skill, anchor="center", width=node_w - 12,
                )
                tier_label = f"TIER {skill['tier']}"
                self.canvas.create_text(cx, y + 4, text=tier_label,
                    fill=text_color, font=self.font_small, anchor="center")
                cost_text = "UNLOCKED" if is_unlocked else f"{skill['rep_cost']} REP"
                self.canvas.create_text(cx, y + 18, text=cost_text,
                    fill=cost_color, font=self.font_small, anchor="center")

                # Click hitbox
                for item in (rect, title):
                    self.canvas.tag_bind(item, "<Button-1>",
                        lambda e, sid=skill_id: self._on_node_click(sid))
                    self.canvas.tag_bind(item, "<Enter>",
                        lambda e, sid=skill_id: self._on_node_hover(sid, True))
                    self.canvas.tag_bind(item, "<Leave>",
                        lambda e, sid=skill_id: self._on_node_hover(sid, False))

        # Resize handler
        self.canvas.bind("<Configure>", lambda e: self.win.after(50, self._render_tree))

    def _on_node_click(self, skill_id):
        self.selected_skill_id = skill_id
        self._build_detail(skill_id)

    def _on_node_hover(self, skill_id, entering):
        if entering:
            skill = SKILLS[skill_id]
            self.status_label.config(text=f"{skill['name']} — click for details",
                                      fg=BRANCHES[skill["branch"]]["color"])
        else:
            self.status_label.config(text="Select a skill to view details",
                                      fg=C["text_dim"])

    # ── Detail panel ─────────────────────────────────────────
    def _build_detail_placeholder(self):
        for w in self.detail_frame.winfo_children():
            w.destroy()
        tk.Label(self.detail_frame, text="◈", bg=C["bg2"], fg=C["green_dk"],
                 font=tkfont.Font(family="Courier New", size=48)).pack(pady=(80, 16))
        tk.Label(self.detail_frame, text="Click any skill to view details",
                 bg=C["bg2"], fg=C["text_dim"], font=self.font_mono).pack()
        tk.Label(self.detail_frame, text="Spend REP to unlock permanent upgrades",
                 bg=C["bg2"], fg=C["text_dim"], font=self.font_small).pack(pady=4)

    def _build_detail(self, skill_id):
        for w in self.detail_frame.winfo_children():
            w.destroy()

        skill = SKILLS[skill_id]
        branch_meta = BRANCHES[skill["branch"]]
        unlocked = set(self.engine.state.unlocked_skills)
        is_unlocked = skill_id in unlocked
        ok, reason = can_unlock(skill_id, unlocked, self.engine.state.rep)

        inner = tk.Frame(self.detail_frame, bg=C["bg2"])
        inner.pack(fill="both", expand=True, padx=18, pady=16)

        # Header: branch + tier
        tk.Label(inner, text=f"{branch_meta['name']}  •  TIER {skill['tier']}",
                 bg=C["bg2"], fg=branch_meta["color"],
                 font=self.font_tier).pack(anchor="w")

        # Skill name
        tk.Label(inner, text=skill["name"], bg=C["bg2"], fg=C["white"],
                 font=self.font_title, anchor="w").pack(anchor="w", pady=(4, 12))

        # Separator
        tk.Frame(inner, bg=branch_meta["color"], height=1).pack(fill="x", pady=(0, 12))

        # Description
        desc = tk.Label(inner, text=skill["desc"], bg=C["bg2"], fg=C["text"],
                        font=self.font_body, wraplength=380,
                        justify="left", anchor="w")
        desc.pack(anchor="w", fill="x")

        # Lore quote
        if skill.get("lore"):
            tk.Frame(inner, bg=C["border"], height=1).pack(fill="x", pady=14)
            tk.Label(inner, text=skill["lore"], bg=C["bg2"], fg=C["text_dim"],
                     font=self.font_lore, wraplength=380,
                     justify="left", anchor="w").pack(anchor="w", fill="x")

        # Prerequisites
        if skill.get("prereq"):
            prereq_skill = SKILLS[skill["prereq"]]
            prereq_ok = skill["prereq"] in unlocked
            prereq_color = C["green"] if prereq_ok else C["red"]
            tk.Label(inner,
                text=f"Requires: {prereq_skill['name']} {'✓' if prereq_ok else '✗'}",
                bg=C["bg2"], fg=prereq_color,
                font=self.font_small).pack(anchor="w", pady=(14, 0))

        # Cost / status
        cost_frame = tk.Frame(inner, bg=C["bg2"])
        cost_frame.pack(anchor="w", fill="x", pady=(18, 0))

        if is_unlocked:
            tk.Label(cost_frame, text="◈ UNLOCKED", bg=C["bg2"],
                     fg=branch_meta["color"], font=self.font_hdr).pack(anchor="w")
        else:
            cost_color = C["amber"] if ok else C["red"]
            tk.Label(cost_frame, text=f"COST: {skill['rep_cost']} REP",
                     bg=C["bg2"], fg=cost_color, font=self.font_hdr).pack(anchor="w")
            tk.Label(cost_frame,
                     text=f"Current REP: {self.engine.state.rep}",
                     bg=C["bg2"], fg=C["text_dim"],
                     font=self.font_small).pack(anchor="w", pady=(2, 0))

        # Unlock button
        if not is_unlocked:
            btn_frame = tk.Frame(inner, bg=C["bg2"])
            btn_frame.pack(anchor="w", fill="x", pady=(18, 0))
            if ok:
                btn = tk.Button(btn_frame, text=f"  UNLOCK  ",
                                bg=branch_meta["color"], fg=C["bg"],
                                font=self.font_hdr, bd=0,
                                padx=20, pady=8,
                                cursor="hand2",
                                activebackground=C["white"],
                                command=lambda: self._unlock(skill_id))
                btn.pack(anchor="w")
            else:
                tk.Label(btn_frame, text=f"⚠ {reason}", bg=C["bg2"],
                         fg=C["red"], font=self.font_small).pack(anchor="w")

    def _unlock(self, skill_id):
        ok, msg = self.engine.unlock_skill(skill_id)
        if ok:
            self._refresh_rep()
            self._render_tree()
            self._build_detail(skill_id)
            self.status_label.config(text=msg, fg=C["green"])
        else:
            self.status_label.config(text=f"⚠ {msg}", fg=C["red"])
