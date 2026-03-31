"""
NEXUS: Zero Day — Game Engine
Handles all game state, save/load, mission logic.
"""

import json
import os
import time
import random
import string
from datetime import datetime
from pathlib import Path
from game.story import CHARACTERS, CHAPTERS, MISSIONS, EDU_CONTENT, TARGETS, ITEMS


SAVE_DIR = Path(os.path.expanduser("~")) / "Documents" / "NEXUS_ZeroDay" / "saves"
SAVE_DIR.mkdir(parents=True, exist_ok=True)


class GameState:
    def __init__(self):
        self.player_handle = "gh0st"
        self.player_name = "Alex Ryder"
        self.credits = 0
        self.rep = 0
        self.trace = 0.0            # 0–100, triggers BUSTED at 100
        self.trace_multiplier = 1.0
        self.current_chapter_id = "ch0"
        self.completed_missions = []
        self.active_mission_id = None
        self.inventory = []
        self.owned_targets = []     # targets we have shell access on
        self.discovered_targets = ["mediabridge-relay"]
        self.log_entries = []
        self.dialogue_seen = set()
        self.edu_topics_read = set()
        self.play_time_seconds = 0
        self.session_start = time.time()
        self.last_save = None
        self.chapter_intros_seen = set()
        self.terminal_history = []
        self.bouncing = False
        self.bounce_hops = []

    def to_dict(self):
        return {
            "player_handle": self.player_handle,
            "player_name": self.player_name,
            "credits": self.credits,
            "rep": self.rep,
            "trace": self.trace,
            "trace_multiplier": self.trace_multiplier,
            "current_chapter_id": self.current_chapter_id,
            "completed_missions": self.completed_missions,
            "active_mission_id": self.active_mission_id,
            "inventory": self.inventory,
            "owned_targets": self.owned_targets,
            "discovered_targets": self.discovered_targets,
            "log_entries": self.log_entries[-100:],
            "dialogue_seen": list(self.dialogue_seen),
            "edu_topics_read": list(self.edu_topics_read),
            "play_time_seconds": self.play_time_seconds + (time.time() - self.session_start),
            "last_save": datetime.now().isoformat(),
            "chapter_intros_seen": list(self.chapter_intros_seen),
            "terminal_history": self.terminal_history[-50:],
            "bouncing": self.bouncing,
            "bounce_hops": self.bounce_hops,
        }

    @classmethod
    def from_dict(cls, d):
        gs = cls()
        gs.player_handle = d.get("player_handle", "gh0st")
        gs.player_name = d.get("player_name", "Alex Ryder")
        gs.credits = d.get("credits", 0)
        gs.rep = d.get("rep", 0)
        gs.trace = d.get("trace", 0.0)
        gs.trace_multiplier = d.get("trace_multiplier", 1.0)
        gs.current_chapter_id = d.get("current_chapter_id", "ch0")
        gs.completed_missions = d.get("completed_missions", [])
        gs.active_mission_id = d.get("active_mission_id", None)
        gs.inventory = d.get("inventory", [])
        gs.owned_targets = d.get("owned_targets", [])
        gs.discovered_targets = d.get("discovered_targets", ["mediabridge-relay"])
        gs.log_entries = d.get("log_entries", [])
        gs.dialogue_seen = set(d.get("dialogue_seen", []))
        gs.edu_topics_read = set(d.get("edu_topics_read", []))
        gs.play_time_seconds = d.get("play_time_seconds", 0)
        gs.session_start = time.time()
        gs.last_save = d.get("last_save")
        gs.chapter_intros_seen = set(d.get("chapter_intros_seen", []))
        gs.terminal_history = d.get("terminal_history", [])
        gs.bouncing = d.get("bouncing", False)
        gs.bounce_hops = d.get("bounce_hops", [])
        return gs


class GameEngine:
    def __init__(self):
        self.state = None
        self.callbacks = {}   # event -> list of callables
        self._active_target_id = None

    # ── Event system ──

    def on(self, event, callback):
        self.callbacks.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self.callbacks.get(event, []):
            cb(*args, **kwargs)

    # ── New Game / Load ──

    def new_game(self, handle="gh0st"):
        self.state = GameState()
        self.state.player_handle = handle
        # Prologue is story-only — missions and targets begin at ch1
        self.state.current_chapter_id = "ch1"
        self._unlock_chapter_targets("ch1")
        self._active_target_id = "mediabridge-relay"
        self.add_log("NEXUS system initialised.", "sys")
        self.emit("state_changed")
        return self.state

    def load_game(self, slot: int):
        path = SAVE_DIR / f"save_slot_{slot}.json"
        if not path.exists():
            return None
        with open(path, "r") as f:
            data = json.load(f)
        self.state = GameState.from_dict(data)
        self._active_target_id = self.state.discovered_targets[0] if self.state.discovered_targets else "mediabridge-relay"
        self.add_log("Game loaded.", "sys")
        self.emit("state_changed")
        return self.state

    def save_game(self, slot: int):
        if not self.state:
            return False
        path = SAVE_DIR / f"save_slot_{slot}.json"
        with open(path, "w") as f:
            json.dump(self.state.to_dict(), f, indent=2)
        self.state.last_save = datetime.now().isoformat()
        self.add_log(f"Game saved to slot {slot}.", "sys")
        return True

    def get_save_info(self, slot: int):
        path = SAVE_DIR / f"save_slot_{slot}.json"
        if not path.exists():
            return None
        try:
            with open(path, "r") as f:
                d = json.load(f)
            chapter = next((c for c in CHAPTERS if c["id"] == d.get("current_chapter_id", "ch0")), CHAPTERS[0])
            secs = d.get("play_time_seconds", 0)
            h, m = int(secs // 3600), int((secs % 3600) // 60)
            return {
                "slot": slot,
                "handle": d.get("player_handle", "gh0st"),
                "chapter": chapter["title"],
                "rep": d.get("rep", 0),
                "credits": d.get("credits", 0),
                "missions": len(d.get("completed_missions", [])),
                "play_time": f"{h:02d}:{m:02d}",
                "last_save": d.get("last_save", "Unknown"),
            }
        except Exception:
            return None

    # ── Target management ──

    @property
    def active_target(self):
        if self._active_target_id:
            return TARGETS.get(self._active_target_id)
        return None

    def set_active_target(self, target_id: str):
        if target_id in TARGETS:
            self._active_target_id = target_id
            if self.state and target_id not in self.state.discovered_targets:
                self.state.discovered_targets.append(target_id)
            self.emit("target_changed", target_id)

    def get_discovered_targets(self):
        if not self.state:
            return []
        return [TARGETS[tid] for tid in self.state.discovered_targets if tid in TARGETS]

    def has_shell(self, target_id=None):
        tid = target_id or self._active_target_id
        return tid in (self.state.owned_targets if self.state else [])

    # ── Mission logic ──

    def get_current_chapter(self):
        if not self.state:
            return CHAPTERS[0]
        return next((c for c in CHAPTERS if c["id"] == self.state.current_chapter_id), CHAPTERS[0])

    def get_available_missions(self):
        if not self.state:
            return []
        chapter = self.state.current_chapter_id
        done = set(self.state.completed_missions)
        return [m for m in MISSIONS if m["chapter"] == chapter and m["id"] not in done]

    def get_active_mission(self):
        if not self.state or not self.state.active_mission_id:
            return None
        return next((m for m in MISSIONS if m["id"] == self.state.active_mission_id), None)

    def accept_mission(self, mission_id: str):
        mission = next((m for m in MISSIONS if m["id"] == mission_id), None)
        if not mission:
            return False
        self.state.active_mission_id = mission_id
        self.set_active_target(mission["target_id"])
        self.add_log(f"Contract accepted: {mission['title']}", "mission")
        self.emit("mission_accepted", mission)
        return True

    def complete_mission(self, mission_id: str):
        mission = next((m for m in MISSIONS if m["id"] == mission_id), None)
        if not mission:
            return
        if mission_id in self.state.completed_missions:
            return

        self.state.completed_missions.append(mission_id)
        self.state.active_mission_id = None
        self.state.credits += mission["reward_credits"]
        self.state.rep += mission["reward_rep"]

        if mission.get("reward_item") and mission["reward_item"] not in self.state.inventory:
            self.state.inventory.append(mission["reward_item"])
            item = ITEMS.get(mission["reward_item"], {})
            self.apply_item_effect(mission["reward_item"])

        self.add_log(f"Contract complete: {mission['title']} | +${mission['reward_credits']:,} | +{mission['reward_rep']} REP", "success")
        self.emit("mission_complete", mission)
        self._check_chapter_advance()

    def _check_chapter_advance(self):
        chapter_missions = [m for m in MISSIONS if m["chapter"] == self.state.current_chapter_id]
        done = set(self.state.completed_missions)
        if all(m["id"] in done for m in chapter_missions):
            chapters = [c["id"] for c in CHAPTERS]
            idx = chapters.index(self.state.current_chapter_id)
            if idx + 1 < len(chapters):
                new_chap = chapters[idx + 1]
                self.state.current_chapter_id = new_chap
                self._unlock_chapter_targets(new_chap)
                self.emit("chapter_unlocked", new_chap)
                self.add_log(f"Chapter unlocked: {CHAPTERS[idx+1]['title']}", "story")

    def _unlock_chapter_targets(self, chapter_id):
        for m in MISSIONS:
            if m["chapter"] == chapter_id:
                if m["target_id"] not in self.state.discovered_targets:
                    self.state.discovered_targets.append(m["target_id"])

    def apply_item_effect(self, item_id: str):
        item = ITEMS.get(item_id)
        if not item:
            return
        effect = item.get("effect", {})
        if "trace_multiplier" in effect:
            self.state.trace_multiplier = min(self.state.trace_multiplier, effect["trace_multiplier"])
        if "trace_reset" in effect:
            self.state.trace = max(0.0, self.state.trace + effect["trace_reset"])
        if "unlock_chapter" in effect:
            # handled by story events
            pass

    # ── Exploit system ──

    def run_exploit(self, exploit_id: str, target_id: str = None, minigame_score: float = 1.0):
        """
        Execute an exploit. Returns dict with result, messages, trace_added.
        minigame_score: 0.0 – 1.0 bonus multiplier from minigame performance.
        """
        tid = target_id or self._active_target_id
        target = TARGETS.get(tid)
        if not target:
            return {"success": False, "messages": ["ERROR: No valid target."]}

        sec = target["sec_level"]

        # Base success probability by exploit type and security level
        base_probs = {
            "recon":       [1.0, 1.0, 0.95, 0.85, 0.70],
            "portscan":    [1.0, 1.0, 1.0,  0.95, 0.90],
            "bruteforce":  [0.90, 0.80, 0.60, 0.35, 0.15],
            "sqlinject":   [0.95, 0.85, 0.65, 0.40, 0.10],
            "overflow":    [0.85, 0.75, 0.60, 0.40, 0.20],
            "sshcrack":    [0.85, 0.75, 0.55, 0.30, 0.10],
            "mitm":        [0.90, 0.80, 0.65, 0.45, 0.20],
            "implant":     [0.85, 0.75, 0.60, 0.40, 0.15],
            "persist":     [0.90, 0.80, 0.70, 0.50, 0.20],
            "exfil":       [0.95, 0.90, 0.75, 0.55, 0.25],
            "phish":       [0.90, 0.85, 0.70, 0.50, 0.30],
            "arp_spoof":   [0.90, 0.80, 0.65, 0.40, 0.15],
            "ssl_strip":   [0.85, 0.75, 0.60, 0.35, 0.10],
            "capture":     [0.90, 0.85, 0.70, 0.50, 0.20],
            "lkm_compile": [0.90, 0.85, 0.75, 0.55, 0.25],
            "kernel_inject":[0.80, 0.70, 0.55, 0.35, 0.10],
            "syscall_hook":[0.85, 0.75, 0.60, 0.40, 0.15],
            "verify_hidden":[0.95, 0.90, 0.85, 0.70, 0.40],
            "osint":       [1.0,  1.0,  0.95, 0.90, 0.80],
            "craft_phish": [0.90, 0.85, 0.75, 0.60, 0.40],
            "credential_harvest":[0.85, 0.75, 0.60, 0.40, 0.20],
            "c2_recon":    [0.90, 0.85, 0.70, 0.50, 0.30],
            "lateral_move":[0.80, 0.70, 0.55, 0.35, 0.15],
            "c2_access":   [0.75, 0.65, 0.50, 0.30, 0.10],
            "internal_recon":[0.90, 0.85, 0.75, 0.55, 0.30],
            "lateral_pivot":[0.80, 0.70, 0.55, 0.35, 0.15],
            "airgap_bridge":[0.75, 0.65, 0.50, 0.30, 0.10],
            "schema_extract":[0.85, 0.75, 0.60, 0.40, 0.20],
            "zeroday_prep":[0.95, 0.90, 0.85, 0.75, 0.65],
            "ipc_corrupt": [0.85, 0.80, 0.70, 0.60, 0.50],
            "config_extract":[0.90, 0.85, 0.75, 0.65, 0.55],
            "clean_exit":  [0.90, 0.85, 0.80, 0.70, 0.60],
            "timing_analysis":[0.85, 0.80, 0.70, 0.55, 0.40],
            "race_exploit":[0.75, 0.65, 0.55, 0.40, 0.25],
            "key_invalidate":[0.85, 0.75, 0.65, 0.50, 0.35],
            "ca_access":   [0.80, 0.70, 0.55, 0.35, 0.15],
            "forge_cert":  [0.90, 0.85, 0.75, 0.60, 0.40],
            "relay_auth":  [0.85, 0.80, 0.70, 0.55, 0.35],
            "relay_disable":[0.90, 0.85, 0.75, 0.60, 0.40],
            "shellcode":   [0.80, 0.70, 0.55, 0.35, 0.15],
            "token_extract":[0.85, 0.75, 0.60, 0.40, 0.20],
        }

        prob_list = base_probs.get(exploit_id, [0.75, 0.65, 0.50, 0.30, 0.15])
        base_prob = prob_list[min(sec, len(prob_list) - 1)]

        # Bonuses
        if "sqlmap_custom" in self.state.inventory and exploit_id == "sqlinject":
            base_prob = min(0.98, base_prob + 0.25)
        if "rop_chain_kit" in self.state.inventory and exploit_id in ("overflow", "shellcode"):
            base_prob = min(0.98, base_prob + 0.30)

        # Minigame performance bonus
        final_prob = min(0.98, base_prob * (0.7 + 0.3 * minigame_score))

        roll = random.random()
        success = roll < final_prob

        # Trace
        trace_amounts = {0: 0.5, 1: 1.5, 2: 3.0, 3: 5.0, 4: 8.0}
        base_trace = trace_amounts.get(sec, 3.0)
        if not success:
            base_trace *= 2.0
        if self.state.bouncing:
            base_trace *= 0.3
        base_trace *= self.state.trace_multiplier

        self.state.trace = min(100.0, self.state.trace + base_trace)

        messages = self._generate_exploit_messages(exploit_id, target, success)
        log_msg = f"[{exploit_id.upper()}] on {target['name']} — {'SUCCESS' if success else 'FAILED'} (trace +{base_trace:.1f}%)"
        self.add_log(log_msg, "success" if success else "err")

        if success and exploit_id in ("implant", "persist", "lkm_compile", "kernel_inject", "overflow",
                                       "ipc_corrupt", "relay_disable", "key_invalidate", "c2_access",
                                       "airgap_bridge", "schema_extract", "forge_cert", "shellcode"):
            if tid not in self.state.owned_targets:
                self.state.owned_targets.append(tid)

        self.emit("exploit_result", {"success": success, "exploit": exploit_id, "target": tid,
                                      "trace_added": base_trace, "messages": messages})

        if self.state.trace >= 100.0:
            self.emit("player_busted")

        return {"success": success, "messages": messages, "trace_added": base_trace, "prob": final_prob}

    def _generate_exploit_messages(self, exploit_id, target, success):
        ip = target["ip"]
        name = target["name"]
        msgs = []

        templates = {
            "recon":        (["[*] Gathering OSINT data on target...",
                              f"[*] WHOIS lookup: {ip}",
                              "[*] Checking Shodan database...",
                              "[*] Analysing certificate transparency logs..."],
                             [f"[+] Target profiled: {name}", f"[+] IP: {ip}", "[+] Open source recon complete."]),
            "portscan":     ([f"[*] Sending SYN packets to {ip}...",
                               "[*] Mapping service banners...",
                               "[*] OS fingerprinting via TTL analysis..."],
                              [f"[+] Scan complete: {len(target['ports'])} open ports",
                               f"[+] OS: {target['os']}",
                               f"[+] Ports: {', '.join(str(p) for p in target['ports'])}"]),
            "bruteforce":   (["[*] Loading credential wordlist (14.3M entries)...",
                               "[*] Applying hashcat rules (best64, leetspeak)...",
                               f"[*] Testing against {ip}:{target['ports'][0]}..."],
                              ["[+] Credential found!", "[+] Authentication bypass successful."]),
            "sqlinject":    (["[*] Detecting SQL injection vectors...",
                               "[*] Testing UNION-based injection...",
                               "[*] Running time-based blind SQLi..."],
                              ["[+] SQL injection confirmed!", "[+] Database structure enumerated."]),
            "overflow":     (["[*] Analysing heap layout with GDB...",
                               "[*] Building ROP chain for NX bypass...",
                               "[*] Calculating stack offset..."],
                              ["[+] Stack overflow triggered!", "[+] Shellcode executing in target context."]),
            "implant":      (["[*] Uploading implant via established session...",
                               "[*] Setting persistence via cron...",
                               "[*] Configuring beaconing interval..."],
                              ["[+] Implant deployed.", "[+] Beacon active. Checking in every 60s."]),
            "persist":      (["[*] Installing systemd service...",
                               "[*] Adding SSH authorized_keys entry...",
                               "[*] Obfuscating service name..."],
                              ["[+] Persistence established.", "[+] Will survive reboot."]),
            "exfil":        (["[*] Identifying target data...",
                               "[*] Compressing and encrypting payload...",
                               "[*] Routing through proxy chain..."],
                              ["[+] Data exfiltrated successfully.", "[+] Payload delivered to NEXUS drop."]),
            "lkm_compile":  (["[*] Cross-compiling LKM for target kernel version...",
                               "[*] Hooking: sys_getdents64, sys_kill, sys_read...",
                               "[*] Signing bypass via kernel version mismatch..."],
                              ["[+] Kernel module compiled.", "[+] Module ready for injection."]),
            "kernel_inject":(["[*] Uploading LKM to target /tmp...",
                               "[*] Executing insmod...",
                               "[*] Verifying kernel hooks active..."],
                              ["[+] Rootkit loaded into kernel!", "[+] Process hiding active."]),
            "zeroday_prep": (["[*] Loading Kai's 0-day payload...",
                               "[*] ASLR entropy calculated via side-channel...",
                               "[*] Crafting heap spray..."],
                              ["[+] Zero-day primed.", "[+] No patch exists for this. One shot."]),
            "ipc_corrupt":  (["[*] Triggering memory corruption in IPC daemon...",
                               "[*] Heap grooming sequence initiated...",
                               "[*] Overwriting vtable pointer..."],
                              ["[+] IPC daemon pwned.", "[+] Arbitrary code execution achieved."]),
            "timing_analysis":(["[*] Measuring credential validation timing...",
                                  "[*] Statistical analysis of response deltas...",
                                  "[*] Identifying race window (187 nanoseconds)..."],
                                 ["[+] Race condition mapped.", "[+] Exploit window identified."]),
            "race_exploit": (["[*] Spinning up 32 concurrent threads...",
                               "[*] Hammering the race window...",
                               "[*] Microsecond-precision exploit timing..."],
                              ["[+] Race condition hit!", "[+] Auth bypass successful."]),
            "ca_access":    (["[*] Accessing OmniCorp internal CA server...",
                               "[*] Using harvested admin credentials...",
                               "[*] Locating CA signing key..."],
                              ["[+] CA access granted.", "[+] Signing key accessible."]),
            "forge_cert":   (["[*] Generating key pair...",
                               "[*] Crafting certificate signing request...",
                               "[*] Signing with compromised CA key..."],
                              ["[+] Rogue certificate forged.", "[+] Valid chain to OmniCorp root CA."]),
        }

        specific = templates.get(exploit_id, (
            [f"[*] Executing {exploit_id} against {ip}...",
             "[*] Processing target response...",
             "[*] Analysing output..."],
            [f"[+] {exploit_id.upper()} succeeded on {name}."]
        ))

        msgs.extend(specific[0])
        if success:
            msgs.extend(specific[1])
        else:
            msgs.append(f"[!] {exploit_id.upper()} FAILED — target defences held.")
            msgs.append("[!] IDS/IPS alert triggered. Trace level increased.")
        return msgs

    # ── Utility ──

    def add_log(self, message: str, level: str = "info"):
        if not self.state:
            return
        entry = {"time": datetime.now().strftime("%H:%M:%S"), "msg": message, "level": level}
        self.state.log_entries.append(entry)
        self.emit("log_entry", entry)

    def add_trace(self, amount: float):
        if not self.state:
            return
        self.state.trace = min(100.0, max(0.0, self.state.trace + amount * self.state.trace_multiplier))
        if self.state.trace >= 100.0:
            self.emit("player_busted")

    def reduce_trace(self, amount: float):
        if not self.state:
            return
        self.state.trace = max(0.0, self.state.trace - amount)

    def mark_edu_read(self, topic: str):
        if self.state:
            self.state.edu_topics_read.add(topic)
            # Small rep reward for learning
            self.state.rep += 2
            self.emit("state_changed")

    def get_chapter_progress(self):
        if not self.state:
            return 0, 0
        chapter_missions = [m for m in MISSIONS if m["chapter"] == self.state.current_chapter_id]
        done = sum(1 for m in chapter_missions if m["id"] in self.state.completed_missions)
        return done, len(chapter_missions)

    def random_hex(self, n=16):
        return ''.join(random.choices('0123456789abcdef', k=n))

    def format_play_time(self):
        if not self.state:
            return "00:00"
        secs = self.state.play_time_seconds + (time.time() - self.state.session_start)
        h, m = int(secs // 3600), int((secs % 3600) // 60)
        return f"{h:02d}h {m:02d}m"
