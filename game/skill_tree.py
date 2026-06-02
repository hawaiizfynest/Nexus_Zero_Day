"""
NEXUS: Zero Day — Skill Tree System

Five branches matching the game's themes. Each branch has four tiers.
Players spend REP to unlock skills; each unlock applies a permanent effect.

Branch design:
  RECON     — defensive intelligence, info-gathering bonuses
  EXPLOIT   — offensive operations, success rate bonuses
  STEALTH   — trace reduction and evasion
  FORENSICS — defensive operations, analysis bonuses (Ch2+ content)
  RESOURCE  — economic and meta upgrades
"""

# Effect keys understood by the engine:
#   exploit_bonus_<id>: float    Adds to base probability for one exploit
#   exploit_bonus_category: dict Adds to base probability for all exploits in a category
#   trace_multiplier: float      Multiplies all trace generation (lower = better)
#   trace_failure_mult: float    Multiplies extra trace from failed exploits
#   bounce_trace_mult: float     Extra trace reduction when bouncing
#   minigame_time_bonus: float   Adds seconds to all minigame timers
#   minigame_score_floor: float  Minimum minigame_score (0.0-1.0) regardless of performance
#   starting_credits: int        One-time credits grant on unlock
#   rep_per_mission: float       Bonus REP multiplier on mission completion
#   codex_rep_bonus: int         Extra REP when reading a new Codex entry
#   trace_decay_per_min: float   Trace passively decays this much per minute

# Exploit categories — used by exploit_bonus_category
EXPLOIT_CATEGORIES = {
    "recon":     ["recon", "portscan", "osint", "internal_recon", "c2_recon"],
    "offensive": ["bruteforce", "sqlinject", "overflow", "shellcode", "sshcrack",
                  "implant", "lateral_move", "lateral_pivot", "kernel_inject",
                  "syscall_hook", "lkm_compile", "ipc_corrupt", "race_exploit",
                  "key_invalidate", "ca_access", "forge_cert", "relay_auth",
                  "relay_disable", "c2_access", "airgap_bridge", "schema_extract",
                  "evidence_extract"],
    "intercept": ["mitm", "arp_spoof", "ssl_strip", "capture", "phish",
                  "craft_phish", "credential_harvest"],
    "stealth":   ["clean_exit", "verify_hidden", "persist", "exfil",
                  "config_extract", "secure_handoff", "metadata_scrub",
                  "relay_rebuild", "verify_clean", "opsec_audit"],
    "analysis": ["file_extract", "static_analysis", "string_dump", "ioc_extract",
                  "sandbox_prep", "detonate", "behaviour_log", "network_capture",
                  "report_iocs", "archive_access", "pcap_filter", "timeline_build",
                  "evidence_package", "implant_capture", "c2_trace", "origin_id"],
}


# Skill definitions
# Each branch has 4 tiers. Tiers must be unlocked sequentially.
SKILLS = {
    # ── RECON branch ──────────────────────────────────────────
    "recon_1": {
        "branch": "recon",
        "tier": 1,
        "name": "Banner Reader",
        "desc": "Years of reviewing service banners pays off. +10% success on all reconnaissance exploits.",
        "rep_cost": 15,
        "effect": {"exploit_bonus_category": {"recon": 0.10}},
        "lore": "Vera: 'Banners tell you everything. The version, the patch state, the laziness of the admin.'",
    },
    "recon_2": {
        "branch": "recon",
        "tier": 2,
        "name": "OSINT Specialist",
        "desc": "Priya's methodology, internalised. +15% recon success and reveals one extra service banner per scan.",
        "rep_cost": 30,
        "effect": {"exploit_bonus_category": {"recon": 0.15}},
        "prereq": "recon_1",
        "lore": "Priya: 'The information is already public. You just need to know where to look.'",
    },
    "recon_3": {
        "branch": "recon",
        "tier": 3,
        "name": "Network Cartographer",
        "desc": "Build mental maps of target infrastructure before touching it. +20% recon and +5% to all offensive exploits.",
        "rep_cost": 55,
        "effect": {"exploit_bonus_category": {"recon": 0.20, "offensive": 0.05}},
        "prereq": "recon_2",
        "lore": "ARIA: 'You are now using approximately fourteen percent of my cartographic capabilities. That is more than most operators.'",
    },
    "recon_4": {
        "branch": "recon",
        "tier": 4,
        "name": "Pattern Recognition",
        "desc": "You see what others miss. +25% recon, +5% offensive, +10% intercept. New targets revealed earlier in chapters.",
        "rep_cost": 90,
        "effect": {"exploit_bonus_category": {"recon": 0.25, "offensive": 0.05, "intercept": 0.10}},
        "prereq": "recon_3",
        "lore": "Vera: 'You have become useful.'",
    },

    # ── EXPLOIT branch ────────────────────────────────────────
    "exploit_1": {
        "branch": "exploit",
        "tier": 1,
        "name": "Payload Crafter",
        "desc": "Cleaner shellcode, fewer crashes. +10% success on all offensive exploits.",
        "rep_cost": 15,
        "effect": {"exploit_bonus_category": {"offensive": 0.10}},
        "lore": "Kai: 'Half the failed exploits I see fail because the payload was sloppy.'",
    },
    "exploit_2": {
        "branch": "exploit",
        "tier": 2,
        "name": "Buffer Surgeon",
        "desc": "Memory corruption is your art form. +20% on buffer overflows, +5% on all offensive exploits.",
        "rep_cost": 30,
        "effect": {"exploit_bonus_<overflow>": 0.20, "exploit_bonus_<shellcode>": 0.20,
                   "exploit_bonus_category": {"offensive": 0.05}},
        "prereq": "exploit_1",
        "lore": "Kai: 'It is a daemon from 2009. It deserves to be loved.'",
    },
    "exploit_3": {
        "branch": "exploit",
        "tier": 3,
        "name": "Race Conditions",
        "desc": "Microsecond-precision timing. +25% on race/timing exploits, +10% on all offensive.",
        "rep_cost": 55,
        "effect": {"exploit_bonus_<race_exploit>": 0.25, "exploit_bonus_<timing_analysis>": 0.25,
                   "exploit_bonus_<key_invalidate>": 0.20, "exploit_bonus_category": {"offensive": 0.10}},
        "prereq": "exploit_2",
        "lore": "Vera: 'A hundred and eighty-seven nanoseconds is forever, if you can see it.'",
    },
    "exploit_4": {
        "branch": "exploit",
        "tier": 4,
        "name": "Zero-Day Hunter",
        "desc": "You see vulnerabilities others can't. +15% on every offensive exploit. +20% on zero-day prep.",
        "rep_cost": 90,
        "effect": {"exploit_bonus_<zeroday_prep>": 0.20, "exploit_bonus_<ipc_corrupt>": 0.15,
                   "exploit_bonus_category": {"offensive": 0.15}},
        "prereq": "exploit_3",
        "lore": "Kai: 'You found three bugs in my own code last week. I am not sure how I feel about this.'",
    },

    # ── STEALTH branch ────────────────────────────────────────
    "stealth_1": {
        "branch": "stealth",
        "tier": 1,
        "name": "Quiet Footsteps",
        "desc": "Less noise on every operation. All trace generation reduced by 15%.",
        "rep_cost": 15,
        "effect": {"trace_multiplier": 0.85},
        "lore": "Vera: 'The hack is the last five minutes. The preparation is everything else.'",
    },
    "stealth_2": {
        "branch": "stealth",
        "tier": 2,
        "name": "Bounce Master",
        "desc": "Better proxy chains, deeper obfuscation. Bouncing now reduces trace by 85% instead of 70%.",
        "rep_cost": 30,
        "effect": {"bounce_trace_mult": 0.15, "trace_multiplier": 0.80},
        "prereq": "stealth_1",
        "lore": "ARIA: 'Bounce nodes available: thirty-two. Healthy. Diverse jurisdictions. Ready.'",
    },
    "stealth_3": {
        "branch": "stealth",
        "tier": 3,
        "name": "Log Surgeon",
        "desc": "Failures barely register. Failed exploits only generate 50% extra trace (down from 100%).",
        "rep_cost": 55,
        "effect": {"trace_failure_mult": 1.5, "trace_multiplier": 0.75},
        "prereq": "stealth_2",
        "lore": "Vera: 'A failure that leaves no trace is not a failure.'",
    },
    "stealth_4": {
        "branch": "stealth",
        "tier": 4,
        "name": "Ghost Protocol",
        "desc": "Trace decays naturally over time. -2% trace per minute, all trace generation reduced by 35%.",
        "rep_cost": 90,
        "effect": {"trace_multiplier": 0.65, "trace_decay_per_min": 2.0},
        "prereq": "stealth_3",
        "lore": "Kai: 'I am genuinely unsure how you are still under the threshold.'",
    },

    # ── FORENSICS branch ──────────────────────────────────────
    "forensics_1": {
        "branch": "forensics",
        "tier": 1,
        "name": "Static Eye",
        "desc": "PE headers reveal their secrets. +15% on all malware analysis and forensics exploits.",
        "rep_cost": 15,
        "effect": {"exploit_bonus_category": {"analysis": 0.15}},
        "lore": "Kai: 'I knew you would come around to analysis eventually.'",
    },
    "forensics_2": {
        "branch": "forensics",
        "tier": 2,
        "name": "Dynamic Mind",
        "desc": "Sandbox detonation revealed. +20% on analysis, +10% extra Codex REP per topic read.",
        "rep_cost": 30,
        "effect": {"exploit_bonus_category": {"analysis": 0.20}, "codex_rep_bonus": 1},
        "prereq": "forensics_1",
        "lore": "Kai: 'The malware will think it is on bare metal. I love this part.'",
    },
    "forensics_3": {
        "branch": "forensics",
        "tier": 3,
        "name": "Chain of Custody",
        "desc": "Court-admissible evidence at every step. +25% on analysis, +10% on stealth exploits.",
        "rep_cost": 55,
        "effect": {"exploit_bonus_category": {"analysis": 0.25, "stealth": 0.10}},
        "prereq": "forensics_2",
        "lore": "Priya: 'Evidence that holds up under cross-examination is worth more than evidence that does not.'",
    },
    "forensics_4": {
        "branch": "forensics",
        "tier": 4,
        "name": "Threat Hunter",
        "desc": "You read attacker behaviour like a book. +30% on analysis, +10% on recon, +5% offensive.",
        "rep_cost": 90,
        "effect": {"exploit_bonus_category": {"analysis": 0.30, "recon": 0.10, "offensive": 0.05}},
        "prereq": "forensics_3",
        "lore": "Vera: 'You can defend now. You should be proud of this. Most operators never get there.'",
    },

    # ── RESOURCE branch ───────────────────────────────────────
    "resource_1": {
        "branch": "resource",
        "tier": 1,
        "name": "Side Gigs",
        "desc": "Freelance security consulting on the side. Grants 2,500 credits.",
        "rep_cost": 15,
        "effect": {"starting_credits": 2500},
        "lore": "Vera: 'Pay your rent. We do not need our operators distracted by ordinary problems.'",
    },
    "resource_2": {
        "branch": "resource",
        "tier": 2,
        "name": "Reputation Network",
        "desc": "Word travels. +25% REP from every completed mission.",
        "rep_cost": 30,
        "effect": {"rep_per_mission": 1.25},
        "prereq": "resource_1",
        "lore": "Priya: 'I have started hearing your handle from sources I did not give it to.'",
    },
    "resource_3": {
        "branch": "resource",
        "tier": 3,
        "name": "Custom Toolkit",
        "desc": "Bespoke scripts and rules tuned to your style. +5% on all exploits. Grants 5,000 credits.",
        "rep_cost": 55,
        "effect": {"exploit_bonus_category": {"recon": 0.05, "offensive": 0.05, "intercept": 0.05,
                                              "stealth": 0.05, "analysis": 0.05},
                   "starting_credits": 5000},
        "prereq": "resource_2",
        "lore": "Kai: 'You built your own YARA rules. I am professionally moved.'",
    },
    "resource_4": {
        "branch": "resource",
        "tier": 4,
        "name": "NEXUS Operator",
        "desc": "You are no longer the new hire. +50% REP per mission, +5% all exploits, +5s on minigame timers.",
        "rep_cost": 90,
        "effect": {"rep_per_mission": 1.50, "minigame_time_bonus": 5.0,
                   "exploit_bonus_category": {"recon": 0.05, "offensive": 0.05, "intercept": 0.05,
                                              "stealth": 0.05, "analysis": 0.05}},
        "prereq": "resource_3",
        "lore": "Vera: 'You are NEXUS now. Welcome.'",
    },
}


# Branch metadata
BRANCHES = {
    "recon":     {"name": "RECON",     "color": "#00ccff", "desc": "Intelligence and reconnaissance"},
    "exploit":   {"name": "EXPLOIT",   "color": "#ff3344", "desc": "Offensive operations"},
    "stealth":   {"name": "STEALTH",   "color": "#ffaa00", "desc": "Trace evasion and OPSEC"},
    "forensics": {"name": "FORENSICS", "color": "#00ff88", "desc": "Defensive analysis"},
    "resource":  {"name": "RESOURCE",  "color": "#c0c0c0", "desc": "Economic and meta upgrades"},
}


def get_branch_skills(branch_id):
    """Return all skills in a branch, sorted by tier."""
    return sorted(
        [(sid, s) for sid, s in SKILLS.items() if s["branch"] == branch_id],
        key=lambda x: x[1]["tier"],
    )


def can_unlock(skill_id, unlocked_skills, current_rep):
    """Check whether a skill can be unlocked right now."""
    skill = SKILLS.get(skill_id)
    if not skill:
        return False, "Unknown skill"
    if skill_id in unlocked_skills:
        return False, "Already unlocked"
    if current_rep < skill["rep_cost"]:
        return False, f"Insufficient REP ({current_rep}/{skill['rep_cost']})"
    prereq = skill.get("prereq")
    if prereq and prereq not in unlocked_skills:
        prereq_name = SKILLS[prereq]["name"]
        return False, f"Requires: {prereq_name}"
    return True, "Available"


def get_effects_for(unlocked_skills):
    """
    Combine effects from all unlocked skills.
    Returns a flat dict suitable for applying in the engine.
    """
    combined = {
        "trace_multiplier": 1.0,
        "trace_failure_mult": 2.0,           # default doubling on failure
        "bounce_trace_mult": 0.3,            # default 70% reduction
        "minigame_time_bonus": 0.0,
        "minigame_score_floor": 0.0,
        "rep_per_mission": 1.0,
        "codex_rep_bonus": 0,
        "trace_decay_per_min": 0.0,
        "exploit_bonus_specific": {},        # exploit_id -> bonus float
        "exploit_bonus_category": {},        # category -> bonus float
    }

    for skill_id in unlocked_skills:
        skill = SKILLS.get(skill_id)
        if not skill:
            continue
        effect = skill.get("effect", {})
        for key, val in effect.items():
            if key.startswith("exploit_bonus_<") and key.endswith(">"):
                exploit_id = key[len("exploit_bonus_<"):-1]
                combined["exploit_bonus_specific"][exploit_id] = \
                    combined["exploit_bonus_specific"].get(exploit_id, 0) + val
            elif key == "exploit_bonus_category":
                for cat, bonus in val.items():
                    combined["exploit_bonus_category"][cat] = \
                        combined["exploit_bonus_category"].get(cat, 0) + bonus
            elif key in ("trace_multiplier", "bounce_trace_mult"):
                combined[key] = min(combined[key], val)   # take best (lowest)
            elif key == "trace_failure_mult":
                combined[key] = min(combined[key], val)   # lower = better
            elif key in ("rep_per_mission",):
                combined[key] = max(combined[key], val)
            elif key in ("minigame_time_bonus", "minigame_score_floor",
                         "codex_rep_bonus", "trace_decay_per_min"):
                combined[key] = combined[key] + val
            elif key == "starting_credits":
                # handled at unlock time, not here
                pass

    return combined


def get_exploit_bonus(unlocked_skills, exploit_id):
    """Return the total bonus probability for a given exploit_id."""
    effects = get_effects_for(unlocked_skills)
    bonus = effects["exploit_bonus_specific"].get(exploit_id, 0.0)

    for category, exploits in EXPLOIT_CATEGORIES.items():
        if exploit_id in exploits:
            bonus += effects["exploit_bonus_category"].get(category, 0.0)

    return bonus
