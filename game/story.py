"""
NEXUS: Zero Day — Story, Characters, Missions, and Lore
All narrative content and cybersecurity educational material.
"""

# ─────────────────────────────────────────────
# CHARACTERS
# ─────────────────────────────────────────────

CHARACTERS = {
    "player": {
        "name": "ALEX RYDER",
        "handle": "gh0st",
        "role": "Protagonist — former network engineer turned hacktivist",
        "bio": (
            "You are Alex Ryder, 28 years old. You spent six years as a senior "
            "network security engineer at OmniCorp, one of the world's largest "
            "defence contractors. When you discovered OmniCorp was selling "
            "surveillance software to authoritarian regimes — software that got "
            "dissidents killed — you tried the legal route. Your whistleblower "
            "report was buried. Your career was destroyed. Now you operate under "
            "the handle 'gh0st' from a rented server farm in an undisclosed location."
        ),
        "portrait": "👤",
    },
    "mentor": {
        "name": "VERA KAINE",
        "handle": "0xVERA",
        "role": "Mentor — veteran hacker and ex-NSA analyst",
        "bio": (
            "Vera Kaine spent twelve years inside Fort Meade running TAO "
            "(Tailored Access Operations) before walking out the day she was "
            "asked to plant malware in a hospital network. She now runs a "
            "loose collective called NEXUS — ethical hackers, journalists, "
            "and ex-intelligence operators working to expose corporate and "
            "government abuse of technology. She is brilliant, paranoid, "
            "and the closest thing to a mentor you have."
        ),
        "portrait": "🧑‍💻",
    },
    "ally": {
        "name": "KAI OSEI",
        "handle": "byte_kai",
        "role": "Ally — malware analyst and reverse engineer",
        "bio": (
            "Kai is 23, a self-taught malware analyst from Accra who learned "
            "to code on a secondhand laptop with a cracked screen. He's the "
            "best reverse engineer you've ever met and has an uncanny ability "
            "to find patterns in obfuscated code. He's also the most cheerful "
            "person in NEXUS, which keeps everyone sane."
        ),
        "portrait": "🧑‍🔬",
    },
    "handler": {
        "name": "PRIYA NAIR",
        "handle": "pr1sm",
        "role": "Handler — OSINT specialist and journalist",
        "bio": (
            "Priya is an investigative journalist who has embedded with NEXUS "
            "to document everything. She keeps NEXUS legally and ethically "
            "grounded — if you go too far, she'll be the first to say so. "
            "Her OSINT (Open Source Intelligence) skills are world-class; "
            "she can build a target profile from nothing but a username."
        ),
        "portrait": "📰",
    },
    "villain": {
        "name": "DIRECTOR HARLAN VOSS",
        "handle": "N/A",
        "role": "Antagonist — OmniCorp Chief of Cyber Operations",
        "bio": (
            "Harlan Voss doesn't see himself as a villain. He sees himself as "
            "pragmatic. Forty years in intelligence, now running OmniCorp's "
            "'Cyber Sovereignty Division' — a unit that sells surveillance "
            "infrastructure to anyone who can pay. He knows NEXUS exists. "
            "He's the one who buried your whistleblower report. And he's "
            "building something called PROJECT LAZARUS."
        ),
        "portrait": "🕴️",
    },
    "ai_guide": {
        "name": "ARIA",
        "handle": "ARIA-v2",
        "role": "AI companion — your on-board assistant",
        "bio": (
            "ARIA (Adaptive Reconnaissance and Intrusion Assistant) is a "
            "custom AI you built from open-source models. She provides "
            "real-time cybersecurity guidance, flags ethical risks, and "
            "occasionally editorialises about your life choices."
        ),
        "portrait": "🤖",
    },
}

# ─────────────────────────────────────────────
# CHAPTERS & STORY MISSIONS
# ─────────────────────────────────────────────

CHAPTERS = [
    {
        "id": "ch0",
        "title": "PROLOGUE — The Spark",
        "subtitle": "How it all began",
        "unlock_rep": 0,
        "intro": (
            "ENCRYPTED TRANSMISSION — NEXUS CHANNEL 7\n"
            "FROM: 0xVERA\n"
            "TO: gh0st\n\n"
            "Alex. I know what OmniCorp did to you. I know about the report, "
            "the NDA, the 'performance review' that ended your career. I've been "
            "watching their network for eight months. Two weeks ago I found "
            "something that changes everything.\n\n"
            "They're calling it PROJECT LAZARUS. I don't know what it is yet, "
            "but the server trail leads to three continents and a black budget "
            "line that doesn't officially exist.\n\n"
            "I need someone on the inside who already knows how they think. "
            "Someone who has every reason to want the truth out.\n\n"
            "NEXUS doesn't pay. We don't promise safety. But we promise this: "
            "if there's something to find, we find it, and the world sees it.\n\n"
            "Are you in?\n\n"
            "— Vera"
        ),
    },
    {
        "id": "ch1",
        "title": "CHAPTER 1 — First Contact",
        "subtitle": "Learning to move in the shadows",
        "unlock_rep": 0,
        "intro": (
            "Vera's first lesson: 'Before you ever touch a target, you understand "
            "it completely. Reconnaissance is 80% of any operation. The hack is "
            "just the last five minutes.'\n\n"
            "Your first target is a low-security relay node used by OmniCorp's "
            "subsidiary, MediaBridge. Getting in won't win the war — but it will "
            "teach you how to move without being seen, and begin mapping the "
            "infrastructure that hides PROJECT LAZARUS."
        ),
    },
    {
        "id": "ch2",
        "title": "CHAPTER 2 — The Network Beneath",
        "subtitle": "Following the data trail",
        "unlock_rep": 25,
        "intro": (
            "Kai delivers news over an encrypted voice call:\n\n"
            "'Okay so — good news and terrifying news. Good news: I found a "
            "reference to LAZARUS in a MediaBridge config backup. Terrifying news: "
            "it's not a surveillance tool. It's infrastructure. Someone built a "
            "hidden network INSIDE the internet. Overlaid on legitimate CDN nodes. "
            "It could reroute traffic, intercept comms, even fake DNS responses "
            "at a national scale.'\n\n"
            "The next targets are the CDN edge nodes. You need data — and you need "
            "to understand the protocols well enough to pull it clean."
        ),
    },
    {
        "id": "ch3",
        "title": "CHAPTER 3 — Ghost Protocol",
        "subtitle": "OmniCorp knows you exist",
        "unlock_rep": 60,
        "intro": (
            "Priya's message arrives at 03:47:\n\n"
            "'Voss knows about NEXUS. I've confirmed it. He's brought in a "
            "private cyber team — ex-GCHQ operators. They're not defending anymore. "
            "They're hunting. Two of our relay nodes were quietly compromised last "
            "week — I only caught it because the CPU fan noise changed on one of "
            "my boxes. (Yes, I physically listen to my servers. Don't judge me.)\n\n"
            "We have a trace on a senior OmniCorp database administrator. He has "
            "no idea what LAZARUS actually does — he just maintains the servers. "
            "But those servers hold the full architectural diagram. We need it.'\n\n"
            "The stakes just got real. Move carefully."
        ),
    },
    {
        "id": "ch4",
        "title": "CHAPTER 4 — Zero Day",
        "subtitle": "The endgame begins",
        "unlock_rep": 120,
        "intro": (
            "Vera's voice is flat. Controlled. That means she's scared.\n\n"
            "'LAZARUS goes live in 72 hours. We finally know what it does: "
            "it's a kill switch. For internet infrastructure across fourteen "
            "countries — the ones that refused to buy OmniCorp's government "
            "surveillance contracts. Voss isn't selling anymore. He's going to "
            "demonstrate that OmniCorp can turn off your internet unless you comply.\n\n"
            "Three targets stand between us and stopping this. The LAZARUS "
            "command node. The authentication server that holds the launch key. "
            "And Voss's private backup relay — the dead man's switch that "
            "triggers LAZARUS automatically if Voss goes offline.\n\n"
            "Kai says we have one viable zero-day that will work against all three. "
            "We use it tonight, or LAZARUS activates Thursday morning.'\n\n"
            "This is everything NEXUS was built for."
        ),
    },
    {
        "id": "epilogue",
        "title": "EPILOGUE — Daylight",
        "subtitle": "What comes after",
        "unlock_rep": 200,
        "intro": (
            "The data Priya published made every major news outlet simultaneously. "
            "Forty-seven OmniCorp executives were indicted within a month. "
            "PROJECT LAZARUS was dismantled by a joint international taskforce "
            "that used NEXUS's own network diagrams as their roadmap.\n\n"
            "Voss disappeared before the arrests. Interpol has an open warrant.\n\n"
            "NEXUS still exists. The threats still exist. But something shifted — "
            "three governments quietly amended their cybersecurity disclosure laws "
            "because of what you helped expose.\n\n"
            "Vera sends one final message:\n"
            "'You asked me once if any of this matters. Look at the news today.\n"
            "— V'"
        ),
    },
]

# ─────────────────────────────────────────────
# MISSIONS
# ─────────────────────────────────────────────

MISSIONS = [
    # ── CHAPTER 1 ──
    {
        "id": "m01",
        "chapter": "ch1",
        "title": "Ghost in the Wire",
        "target_id": "mediabridge-relay",
        "briefing": (
            "ARIA: 'Your first real target. MediaBridge relay node — OmniCorp subsidiary. "
            "Security is minimal, but sloppy habits here will get you caught on harder "
            "targets later. Vera wants you to scan the open ports and retrieve the "
            "server's configuration backup. Nothing glamorous — but Vera says: "
            "\"If you can't do the boring work cleanly, you'll die on the exciting work.\"'"
        ),
        "objective": "Perform reconnaissance and exfiltrate the server config",
        "steps": ["recon", "portscan", "exfil"],
        "reward_credits": 0,
        "reward_rep": 10,
        "reward_item": "proxy_chain_v1",
        "difficulty": "tutorial",
        "edu_topic": "port_scanning",
        "completion_dialog": {
            "speaker": "mentor",
            "text": (
                "Good. Clean in, clean out. Did you notice how much information "
                "an open port gives you even before you touch it? The service banner "
                "alone told us the OS version, the SSH daemon version, even the "
                "approximate patch date. That's why reconnaissance is everything."
            ),
        },
    },
    {
        "id": "m02",
        "chapter": "ch1",
        "title": "Default Sins",
        "target_id": "mediabridge-cms",
        "briefing": (
            "KAI: 'Okay so I found something beautiful and horrifying. MediaBridge's "
            "content management server? Still running default admin credentials. "
            "admin/admin123. I am not joking. This is a company that processes "
            "traffic for eleven governments and their CMS password is admin123.\n\n"
            "Get in, drop a read-only implant so we can monitor traffic, and get out. "
            "And please — change nothing, touch nothing, leave it exactly as you found it. "
            "We are here to observe, not to break things.'"
        ),
        "objective": "Exploit default credentials and install a passive monitor",
        "steps": ["bruteforce", "implant", "persist"],
        "reward_credits": 500,
        "reward_rep": 15,
        "reward_item": "keylogger_passive",
        "difficulty": "easy",
        "edu_topic": "default_credentials",
        "completion_dialog": {
            "speaker": "ally",
            "text": (
                "Default credentials are responsible for roughly 15% of all breaches "
                "reported to CISA annually. It sounds almost too simple to be real, "
                "but attackers don't need sophistication when defenders hand them the keys. "
                "Every production system should have its defaults changed on day one — "
                "it's literally the first item in every hardening checklist ever written."
            ),
        },
    },
    {
        "id": "m03",
        "chapter": "ch1",
        "title": "Injection Season",
        "target_id": "mediabridge-db",
        "briefing": (
            "ARIA: 'The MediaBridge customer database is reachable through their "
            "web portal. Priya found a login page with — and I want you to appreciate "
            "how 2005 this is — no prepared statements. The SQL query is built by "
            "string concatenation.\n\n"
            "Classic SQL injection. Your goal is to extract the internal routing "
            "table that maps MediaBridge traffic to OmniCorp backbone nodes. "
            "This map is the first piece of LAZARUS architecture we can confirm.'"
        ),
        "objective": "Extract routing data via SQL injection vulnerability",
        "steps": ["sqlinject", "extract", "exfil"],
        "reward_credits": 800,
        "reward_rep": 20,
        "reward_item": "sqlmap_custom",
        "difficulty": "easy",
        "edu_topic": "sql_injection",
        "completion_dialog": {
            "speaker": "handler",
            "text": (
                "SQL injection has been in the OWASP Top 10 since 2003. Twenty years. "
                "It's preventable with two lines of code — parameterised queries. "
                "Yet it remains one of the most common vulnerabilities in the wild. "
                "The fix costs almost nothing. The consequences of not fixing it — "
                "as you just demonstrated — are total database exposure."
            ),
        },
    },

    # ── CHAPTER 2 ──
    {
        "id": "m04",
        "chapter": "ch2",
        "title": "Man in the Middle",
        "target_id": "cdn-edge-node-7",
        "briefing": (
            "VERA: 'CDN edge node 7. OmniCorp routes encrypted OmniCorp-to-subsidiary "
            "traffic through it. They think TLS protects them.\n\n"
            "Here's what they missed: the node itself doesn't validate certificate "
            "chains properly. We can intercept the connection, present our own "
            "certificate, and read the traffic in plaintext before re-encrypting "
            "and forwarding it. Classic MITM against misconfigured TLS.\n\n"
            "Target data: any packets tagged with LAZARUS internal routing headers. "
            "ARIA will filter.'"
        ),
        "objective": "Execute TLS MITM attack to intercept LAZARUS traffic",
        "steps": ["arp_spoof", "ssl_strip", "capture", "exfil"],
        "reward_credits": 1200,
        "reward_rep": 25,
        "reward_item": "ssl_intercept_cert",
        "difficulty": "medium",
        "edu_topic": "mitm_tls",
        "completion_dialog": {
            "speaker": "mentor",
            "text": (
                "Certificate pinning would have stopped this cold. When an application "
                "pins a certificate, it refuses any connection that doesn't present that "
                "exact cert — even if it's signed by a trusted CA. Mobile banking apps "
                "use it. Signal uses it. OmniCorp didn't bother for internal CDN traffic "
                "because they assumed the network was 'trusted'. There is no trusted network."
            ),
        },
    },
    {
        "id": "m05",
        "chapter": "ch2",
        "title": "Buffer Overflow Blues",
        "target_id": "omnicorp-legacy-auth",
        "briefing": (
            "KAI: 'So this is interesting. OmniCorp's secondary auth server is running "
            "a custom authentication daemon written in C. From 2009. And it hasn't "
            "been updated since 2014.\n\n"
            "I found a stack buffer overflow in the session token handler. When the "
            "input exceeds 512 bytes, we overwrite the return address and redirect "
            "execution to our shellcode. It's textbook — like a CTF challenge that "
            "somehow made it into production.\n\n"
            "The auth server holds session tokens for the LAZARUS admin panel. "
            "One of those tokens is our next breadcrumb.'"
        ),
        "objective": "Exploit buffer overflow to extract admin session tokens",
        "steps": ["overflow", "shellcode", "token_extract"],
        "reward_credits": 2000,
        "reward_rep": 30,
        "reward_item": "rop_chain_kit",
        "difficulty": "medium",
        "edu_topic": "buffer_overflow",
        "completion_dialog": {
            "speaker": "ai_guide",
            "text": (
                "Modern mitigations make this significantly harder in the real world: "
                "ASLR randomises memory layout so you can't hardcode return addresses. "
                "Stack canaries are sentinel values that detect stack corruption before "
                "the return. NX/DEP marks stack memory non-executable. "
                "Safe languages like Rust eliminate entire classes of memory bugs at "
                "compile time. Legacy C code without these protections is a gift to attackers."
            ),
        },
    },
    {
        "id": "m06",
        "chapter": "ch2",
        "title": "Phishing Season",
        "target_id": "omnicorp-hr",
        "briefing": (
            "PRIYA: 'I've profiled Marcus Webb, OmniCorp's senior HR sysadmin. "
            "LinkedIn: 14 years at OmniCorp, Manchester United fan, three kids, "
            "dog named Biscuit — I found that from a half-public Facebook post. "
            "He uses the same email handle across three platforms.\n\n"
            "We're going to send him a spear-phishing email. It will look like "
            "an internal HR portal update notification. When he clicks the link, "
            "it'll capture his SSO credentials.\n\n"
            "I want to be transparent: this feels uncomfortable. We're deceiving "
            "a human being who is almost certainly not aware of LAZARUS. "
            "But his credentials get us into the HR database — and LAZARUS "
            "personnel records are stored there.'"
        ),
        "objective": "Craft spear-phish to capture SSO credentials",
        "steps": ["osint", "craft_phish", "credential_harvest"],
        "reward_credits": 1500,
        "reward_rep": 25,
        "reward_item": "sso_token_omnicorp",
        "difficulty": "medium",
        "edu_topic": "phishing_spearphish",
        "completion_dialog": {
            "speaker": "handler",
            "text": (
                "Spear phishing works because it is tailored. Generic phishing has "
                "~3% click rates. Spear phishing targeting a specific individual with "
                "contextual detail — their company, their manager's name, a current "
                "project — can exceed 50%. The defence is multi-factor authentication: "
                "a stolen password alone cannot log in. And security awareness training "
                "that teaches people to verify links before clicking, even from 'trusted' senders."
            ),
        },
    },

    # ── CHAPTER 3 ──
    {
        "id": "m07",
        "chapter": "ch3",
        "title": "Rootkit",
        "target_id": "omnicorp-db-primary",
        "briefing": (
            "VERA: 'We're inside their perimeter now, but we need to stay inside. "
            "Voss's hunting team will eventually find and clean our entry points. "
            "We need persistence — something that survives a reboot and hides "
            "from their own security tools.\n\n"
            "A kernel-level rootkit loaded as a Linux kernel module. It will "
            "hook the getdents64 syscall to hide our processes and files from "
            "standard tools. Their EDR won't see it because their EDR runs in "
            "user space. We live in kernel space.\n\n"
            "I know what you're thinking. Yes, this is serious. We are planting "
            "a rootkit in a live production database server. Do not touch any "
            "client data. Read the LAZARUS tables only. ARIA will enforce this.'"
        ),
        "objective": "Deploy kernel rootkit for persistent database access",
        "steps": ["lkm_compile", "kernel_inject", "syscall_hook", "verify_hidden"],
        "reward_credits": 3000,
        "reward_rep": 35,
        "reward_item": "lkm_rootkit",
        "difficulty": "hard",
        "edu_topic": "rootkits_persistence",
        "completion_dialog": {
            "speaker": "ai_guide",
            "text": (
                "Kernel rootkits are among the most difficult threats to detect because "
                "they operate at the same privilege level as the security tools trying to "
                "find them. Detection methods include: integrity verification of kernel "
                "memory from a trusted hypervisor, cross-view detection comparing "
                "kernel-level and hardware-level process lists, and secure boot with "
                "module signing — which would have prevented this specific attack by "
                "rejecting our unsigned kernel module."
            ),
        },
    },
    {
        "id": "m08",
        "chapter": "ch3",
        "title": "The Counter-Hunt",
        "target_id": "voss-hunting-team",
        "briefing": (
            "ARIA: 'Alert. I've identified the OmniCorp hunting team's C2 "
            "(command-and-control) server. They are actively scanning NEXUS "
            "infrastructure. Current threat: elevated.\n\n"
            "Priya is pushing for us to hack back — compromise their C2, "
            "see what they know about NEXUS. Vera says this is legally and "
            "ethically murky but operationally necessary. She's leaving the "
            "call to you.\n\n"
            "If we hack their hunting infrastructure, we gain intelligence "
            "and slow them down. But we also become more like what we're "
            "fighting against. This is not a simple decision. Consider carefully "
            "before choosing your approach.'"
        ),
        "objective": "Neutralise the counter-intel team's C2 server",
        "steps": ["c2_recon", "lateral_move", "c2_access"],
        "reward_credits": 2500,
        "reward_rep": 40,
        "reward_item": "c2_intercept_data",
        "difficulty": "hard",
        "edu_topic": "c2_infrastructure",
        "completion_dialog": {
            "speaker": "mentor",
            "text": (
                "Command-and-control infrastructure is the nervous system of any "
                "offensive operation. Cutting it blinds an attacker. In real incident "
                "response, one of the first priorities is identifying C2 channels — "
                "often identified by unusual beaconing patterns, DNS queries to recently "
                "registered domains, or TLS certificates with unusual attributes. "
                "Threat intelligence feeds like MISP help defenders share indicators of compromise."
            ),
        },
    },
    {
        "id": "m09",
        "chapter": "ch3",
        "title": "The Architecture",
        "target_id": "lazarus-schema-server",
        "briefing": (
            "KAI: 'I've got coordinates on the server holding the full LAZARUS "
            "architecture diagram. It's air-gapped — not connected to the regular "
            "internet. But it IS connected to OmniCorp's internal research network, "
            "which IS connected to a server we already own.\n\n"
            "Lateral movement. We hop from our compromised DB server, across the "
            "internal network, to the research segment, then to the air-gapped node "
            "via a shared backup system they thought was isolated.\n\n"
            "Air gaps are only as strong as the humans who maintain them. "
            "Someone connected a backup drive to both sides. That someone "
            "just became our bridge.'"
        ),
        "objective": "Lateral movement to reach air-gapped LAZARUS schema server",
        "steps": ["internal_recon", "lateral_pivot", "airgap_bridge", "schema_extract"],
        "reward_credits": 4000,
        "reward_rep": 45,
        "reward_item": "lazarus_schema",
        "difficulty": "hard",
        "edu_topic": "lateral_movement_airgap",
        "completion_dialog": {
            "speaker": "handler",
            "text": (
                "Air gaps fail most often through human behaviour — USB drives, "
                "shared backup media, a technician who connected 'just temporarily'. "
                "The famous Stuxnet worm — which destroyed Iranian nuclear centrifuges — "
                "crossed an air gap via infected USB drives carried by unknowing contractors. "
                "True security requires both technical controls AND procedural discipline "
                "from every human in the chain."
            ),
        },
    },

    # ── CHAPTER 4 ──
    {
        "id": "m10",
        "chapter": "ch4",
        "title": "Zero Day",
        "target_id": "lazarus-command-node",
        "briefing": (
            "VERA: 'This is it. The LAZARUS command node. Kai's zero-day exploits "
            "a memory corruption vulnerability in the custom IPC daemon — it was "
            "developed by OmniCorp's internal team and has never been audited. "
            "No CVE, no patch, no signature.\n\n"
            "A true zero-day. Named because defenders have had zero days to "
            "prepare. Once we use it, Voss will know it's blown and patch it. "
            "We get one shot.\n\n"
            "Get in. Retrieve the LAZARUS launch configuration. Don't destroy "
            "anything — we need evidence, not a crime scene. Priya needs "
            "everything intact to publish.'"
        ),
        "objective": "Deploy zero-day exploit against LAZARUS command node",
        "steps": ["zeroday_prep", "ipc_corrupt", "config_extract", "clean_exit"],
        "reward_credits": 5000,
        "reward_rep": 50,
        "reward_item": "lazarus_config",
        "difficulty": "elite",
        "edu_topic": "zero_day_exploits",
        "completion_dialog": {
            "speaker": "ally",
            "text": (
                "Zero-days are the most valuable currency in offensive security. "
                "Bug bounty programmes pay $500 to $2.5 million for critical zero-days "
                "in major software. Governments pay even more. The ethical question: "
                "when you find a zero-day, do you report it (responsible disclosure) "
                "or sell it? Bug bounty programmes exist specifically to make "
                "responsible disclosure financially viable — so the right choice "
                "is also the rewarding one."
            ),
        },
    },
    {
        "id": "m11",
        "chapter": "ch4",
        "title": "The Kill Switch",
        "target_id": "lazarus-auth-server",
        "briefing": (
            "ARIA: 'The LAZARUS authentication server validates the launch key. "
            "Without it, the command node can't arm. We need to invalidate "
            "all existing launch credentials before Thursday.\n\n"
            "This is the most heavily defended target we've approached. "
            "Vera's intel shows it runs a hardened HSM — Hardware Security Module — "
            "for key storage. The HSM itself is unbreakable. But the software "
            "that talks TO the HSM has a race condition in the credential "
            "validation routine.\n\n"
            "Timing attack. Microsecond precision. Kai has written the exploit. "
            "Your job is execution.'"
        ),
        "objective": "Exploit race condition to invalidate LAZARUS launch keys",
        "steps": ["timing_analysis", "race_exploit", "key_invalidate"],
        "reward_credits": 6000,
        "reward_rep": 55,
        "reward_item": "lazarus_keys_null",
        "difficulty": "elite",
        "edu_topic": "race_conditions_timing",
        "completion_dialog": {
            "speaker": "mentor",
            "text": (
                "Race conditions occur when a system's behaviour depends on the "
                "sequence or timing of events. In security, the classic example is "
                "TOCTOU — Time of Check to Time of Use. You check a condition is safe, "
                "then an attacker changes it before you use it. Mitigations include "
                "atomic operations, proper mutex locking, and HSMs that handle "
                "crypto operations as single indivisible transactions."
            ),
        },
    },
    {
        "id": "m12",
        "chapter": "ch4",
        "title": "Dead Man's Switch",
        "target_id": "voss-dead-mans-relay",
        "briefing": (
            "PRIYA: 'If Voss goes offline — arrested, disappeared, even just "
            "loses connectivity — his dead man's switch automatically fires "
            "LAZARUS. We have to disable it before we do anything that might "
            "tip him off.\n\n"
            "It's a simple relay server, but it uses certificate-based mutual "
            "authentication. Both sides prove their identity with client certificates. "
            "No cert, no connection.\n\n"
            "However — I found Voss's certificate was issued by an OmniCorp "
            "internal CA. And we own the CA server. We can issue ourselves "
            "a valid certificate that the relay will accept.\n\n"
            "Rogue CA attack. Vera says this is the kind of thing that keeps "
            "her awake at night — the terrifying power of certificate authorities.'"
        ),
        "objective": "Use rogue CA cert to disable Voss's dead man's relay",
        "steps": ["ca_access", "forge_cert", "relay_auth", "relay_disable"],
        "reward_credits": 7000,
        "reward_rep": 60,
        "reward_item": "relay_disabled",
        "difficulty": "elite",
        "edu_topic": "pki_certificate_trust",
        "completion_dialog": {
            "speaker": "ai_guide",
            "text": (
                "Certificate Authorities are the root of trust for the entire web. "
                "If a CA is compromised, every certificate it has ever issued becomes "
                "suspect. This happened in 2011 when DigiNotar was breached — attackers "
                "issued fraudulent certificates for Google, Mozilla, and intelligence agencies. "
                "Certificate Transparency logs now make it impossible to silently issue "
                "rogue certs for major domains — every certificate is publicly logged "
                "and can be audited by domain owners."
            ),
        },
    },
]

# ─────────────────────────────────────────────
# CYBERSECURITY EDUCATION CONTENT
# ─────────────────────────────────────────────

EDU_CONTENT = {
    "port_scanning": {
        "title": "Port Scanning & Network Reconnaissance",
        "tldr": "Discovering what services a target exposes before attacking.",
        "sections": [
            {
                "heading": "What is a Port?",
                "body": (
                    "A network port is a numbered endpoint (0–65535) for network "
                    "communication. Port 80 = HTTP web traffic. Port 443 = HTTPS. "
                    "Port 22 = SSH (secure shell). Port 3306 = MySQL database.\n\n"
                    "When a service 'listens' on a port, it's waiting for connections. "
                    "Scanning reveals which ports are open — and therefore which services "
                    "are running and potentially exploitable."
                ),
            },
            {
                "heading": "SYN Scanning (Stealth Scan)",
                "body": (
                    "TCP connections normally use a 3-way handshake: SYN → SYN/ACK → ACK.\n"
                    "A SYN scan sends only the initial SYN packet. If the port is open, "
                    "it replies with SYN/ACK — we immediately send RST to tear down the "
                    "connection without completing the handshake.\n\n"
                    "Result: faster, leaves fewer log entries, harder to detect.\n"
                    "Tool: nmap -sS (requires root)\n"
                    "CVE relevance: Identifies services to target for known vulnerabilities."
                ),
            },
            {
                "heading": "Service & Version Detection",
                "body": (
                    "Banner grabbing reads the initial response from a service — often "
                    "it literally announces: 'OpenSSH_8.9p1 Ubuntu-3'\n\n"
                    "This version number maps directly to known CVEs. OpenSSH 8.9p1 "
                    "has no critical RCE. OpenSSH 9.x before 9.8p1 has CVE-2024-6387 "
                    "(regreSSHion) — an unauthenticated remote code execution flaw.\n\n"
                    "Defenders: disable version banners in service configs."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "• Firewall rules: only expose ports that absolutely need to be public\n"
                    "• Network segmentation: internal services unreachable from outside\n"
                    "• IDS/IPS: tools like Snort detect port scanning patterns\n"
                    "• Port knocking: ports only open after a specific sequence of connection attempts\n"
                    "• Regular vulnerability scanning of your own infrastructure (Nessus, OpenVAS)"
                ),
            },
        ],
        "real_world": "The 2017 Equifax breach began with port scanning that identified an unpatched Apache Struts server (CVE-2017-5638). 147 million people's data was exposed.",
        "tools": ["nmap", "masscan", "netcat", "shodan (passive recon)"],
    },

    "default_credentials": {
        "title": "Default & Weak Credentials",
        "tldr": "The most common and embarrassing vulnerability in existence.",
        "sections": [
            {
                "heading": "The Scale of the Problem",
                "body": (
                    "The Mirai botnet (2016) infected 600,000 IoT devices — cameras, "
                    "routers, DVRs — using only 62 default username/password combinations. "
                    "It then launched the largest DDoS attack ever recorded at the time, "
                    "taking down major internet infrastructure.\n\n"
                    "62 passwords. No exotic exploits. No zero-days. Just: admin/admin."
                ),
            },
            {
                "heading": "Why Do Defaults Persist?",
                "body": (
                    "• Manufacturers ship with defaults for 'ease of setup'\n"
                    "• IT teams deprioritise 'basic' hardening under workload pressure\n"
                    "• Shadow IT: devices deployed by departments without security review\n"
                    "• Forgotten systems: a server set up in 2016 and never reviewed\n"
                    "• Credential stuffing: leaked passwords from one breach reused elsewhere"
                ),
            },
            {
                "heading": "Credential Stuffing vs Brute Force",
                "body": (
                    "Brute force tries every possible combination — slow, detectable, "
                    "often locked out after N attempts.\n\n"
                    "Credential stuffing uses real leaked credentials from data breaches. "
                    "Have I Been Pwned catalogues 12+ billion compromised accounts. "
                    "If your users reuse passwords, a breach somewhere else becomes "
                    "your problem too. This is why password managers and unique passwords matter."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "• Change ALL default credentials on deployment — make it automated\n"
                    "• Multi-factor authentication (MFA/2FA) — a stolen password alone is useless\n"
                    "• Account lockout policies after N failed attempts\n"
                    "• Password managers + unique passwords per service\n"
                    "• Regular audits using tools like Shodan to find exposed defaults on your network"
                ),
            },
        ],
        "real_world": "The 2021 Oldsmar water treatment plant attack: attackers gained access via a remote desktop connection with a weak password and no MFA, attempting to poison the water supply.",
        "tools": ["hydra", "medusa", "burpsuite (web auth)", "crackmapexec"],
    },

    "sql_injection": {
        "title": "SQL Injection",
        "tldr": "Inserting SQL code into inputs to manipulate the database.",
        "sections": [
            {
                "heading": "How It Works",
                "body": (
                    "Vulnerable code builds a query by concatenating user input:\n\n"
                    "  query = \"SELECT * FROM users WHERE name='\" + username + \"'\"\n\n"
                    "Attacker inputs:  ' OR '1'='1\n"
                    "Result:  SELECT * FROM users WHERE name='' OR '1'='1'\n\n"
                    "Since 1=1 is always true, this returns ALL users. The attacker "
                    "is now logged in as the first user in the database — often admin."
                ),
            },
            {
                "heading": "Types of SQL Injection",
                "body": (
                    "UNION-based: Append a UNION SELECT to extract data from other tables.\n\n"
                    "Blind (Boolean): Ask true/false questions — 'Does the password start with A?' "
                    "and infer data from different responses.\n\n"
                    "Time-based Blind: Use SLEEP() — if the page delays 5 seconds, condition is true. "
                    "Works even when no data is returned in the response.\n\n"
                    "Out-of-band: Exfiltrate via DNS queries or HTTP requests to attacker-controlled server."
                ),
            },
            {
                "heading": "The Fix (2 Lines of Code)",
                "body": (
                    "Parameterised queries (prepared statements) separate code from data:\n\n"
                    "  stmt = db.prepare('SELECT * FROM users WHERE name = ?')\n"
                    "  stmt.execute([username])\n\n"
                    "The database now KNOWS that username is data, never code. "
                    "No amount of SQL syntax in the input can escape this separation.\n\n"
                    "Also use: ORM frameworks (SQLAlchemy, Hibernate), input validation, "
                    "principle of least privilege on DB accounts."
                ),
            },
        ],
        "real_world": "The 2008 Heartland Payment Systems breach: SQL injection exposed 130 million credit card numbers. Cost: $140 million in settlements.",
        "tools": ["sqlmap", "burp suite", "manual testing with browser dev tools"],
    },

    "mitm_tls": {
        "title": "Man-in-the-Middle & TLS Security",
        "tldr": "Intercepting communications by positioning between two parties.",
        "sections": [
            {
                "heading": "ARP Spoofing",
                "body": (
                    "On a local network, ARP (Address Resolution Protocol) maps IP addresses "
                    "to MAC addresses. It has no authentication.\n\n"
                    "An attacker broadcasts: 'I am 192.168.1.1 (the gateway), my MAC is XX:XX'\n"
                    "Now all traffic intended for the gateway flows through the attacker first.\n\n"
                    "This is how MITM attacks begin on local networks."
                ),
            },
            {
                "heading": "TLS and Certificate Validation",
                "body": (
                    "TLS (Transport Layer Security) protects web traffic. It works because:\n"
                    "1. The server presents a certificate proving its identity\n"
                    "2. The certificate is signed by a trusted Certificate Authority\n"
                    "3. Your browser maintains a list of trusted CAs\n\n"
                    "MITM against TLS requires either: a compromised CA (rare), a user clicking "
                    "'Accept Certificate Warning' (common), or certificate pinning being absent."
                ),
            },
            {
                "heading": "SSL Stripping",
                "body": (
                    "SSLStrip downgrades HTTPS connections to HTTP.\n"
                    "When a user types 'bank.com', the attacker intercepts the initial "
                    "HTTP request (before HTTPS redirect), serves an HTTP page, and "
                    "forwards HTTPS requests to the real server on the victim's behalf.\n\n"
                    "User sees: http://bank.com (often doesn't notice the missing S)\n"
                    "Fix: HSTS (HTTP Strict Transport Security) — tells browsers to ALWAYS "
                    "use HTTPS for this domain, refusing HTTP connections."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "• HSTS with long max-age and includeSubDomains\n"
                    "• Certificate pinning in mobile/desktop apps\n"
                    "• Dynamic ARP Inspection on managed switches\n"
                    "• VPN for any sensitive communication on untrusted networks\n"
                    "• Always check for the padlock and verify domain spelling"
                ),
            },
        ],
        "real_world": "The 2015 Superfish adware on Lenovo laptops installed a root CA certificate, enabling MITM of all HTTPS traffic on affected machines — including banking.",
        "tools": ["bettercap", "ettercap", "mitmproxy", "wireshark"],
    },

    "buffer_overflow": {
        "title": "Buffer Overflow Vulnerabilities",
        "tldr": "Writing beyond a buffer's boundary to overwrite adjacent memory.",
        "sections": [
            {
                "heading": "Memory Layout",
                "body": (
                    "A running program's stack looks roughly like this (simplified):\n\n"
                    "  [local variables / buffer]\n"
                    "  [saved frame pointer]\n"
                    "  [return address]  ← where execution goes when function returns\n"
                    "  [caller's variables]\n\n"
                    "If we write more data into 'buffer' than it can hold, we spill "
                    "into adjacent memory — eventually reaching the return address."
                ),
            },
            {
                "heading": "The Exploit",
                "body": (
                    "Classic overflow:\n"
                    "1. Fill buffer with 'A' * N to measure overflow offset\n"
                    "2. Craft payload: [padding] + [new return address] + [shellcode]\n"
                    "3. When function returns, execution jumps to shellcode\n\n"
                    "Shellcode is machine code that does something useful: spawn a shell, "
                    "add a user, download a payload. Written in x86/x64 assembly, "
                    "often constrained to avoid null bytes."
                ),
            },
            {
                "heading": "Modern Mitigations",
                "body": (
                    "ASLR (Address Space Layout Randomisation): randomises stack/heap/lib "
                    "locations on each run. You can't hardcode 'jump to 0xbfffxxxx'.\n\n"
                    "Stack Canaries: a random value placed before the return address. "
                    "If it's changed when the function returns, execution aborts.\n\n"
                    "NX/DEP (No-Execute / Data Execution Prevention): marks stack as "
                    "non-executable. Your shellcode can't run there.\n\n"
                    "ROP Chains (attacker counter): chain existing executable code snippets "
                    "('gadgets') to achieve goals without injecting new code. "
                    "This is why CFI (Control Flow Integrity) was developed."
                ),
            },
        ],
        "real_world": "CVE-2021-44228 (Log4Shell) wasn't a classic buffer overflow, but stack-based vulnerabilities like CVE-2021-3156 (Sudo heap overflow) gave instant root on millions of Linux systems.",
        "tools": ["pwntools", "gdb + peda", "ropper", "checksec"],
    },

    "phishing_spearphish": {
        "title": "Phishing & Social Engineering",
        "tldr": "Exploiting human trust rather than technical vulnerabilities.",
        "sections": [
            {
                "heading": "Why Phishing Works",
                "body": (
                    "Technical defences are getting better. Humans are the constant. "
                    "A well-crafted phishing email exploits:\n\n"
                    "• Authority (email from 'your CEO')\n"
                    "• Urgency ('Your account will be closed in 24 hours')\n"
                    "• Familiarity (uses your real name, company, ongoing project)\n"
                    "• Fear (security alert, legal notice)\n"
                    "• Curiosity (invoice attached, package tracking)\n\n"
                    "The 2016 Podesta email breach that influenced a US election "
                    "used a single phishing email. One click."
                ),
            },
            {
                "heading": "OSINT for Spear Phishing",
                "body": (
                    "Attackers research targets before crafting a message:\n\n"
                    "LinkedIn: job titles, reporting structure, current projects, "
                    "tech stack, colleagues' names.\n"
                    "Twitter/X: interests, travel, who they follow, tone of voice.\n"
                    "Company website: org chart, press releases, current events.\n"
                    "Data breach dumps: email format, potentially reused passwords.\n\n"
                    "This intelligence makes 'Hi [FirstName], regarding the [RealProject]' "
                    "emails indistinguishable from legitimate internal comms."
                ),
            },
            {
                "heading": "Email Authentication Defences",
                "body": (
                    "SPF (Sender Policy Framework): lists which mail servers can send "
                    "email for your domain. Receiving server checks and rejects others.\n\n"
                    "DKIM (DomainKeys Identified Mail): cryptographically signs outgoing email. "
                    "Proves it wasn't modified in transit.\n\n"
                    "DMARC: policy that says what to do if SPF/DKIM fail — reject, quarantine, "
                    "or report. With reporting, you see every spoofing attempt.\n\n"
                    "MFA: even if credentials are stolen, attacker can't log in."
                ),
            },
        ],
        "real_world": "The 2020 Twitter hack that compromised Obama, Biden, Musk, Apple, and others began with a phone phishing call to a Twitter employee. Pure social engineering — no code needed.",
        "tools": ["gophish", "set (social-engineer toolkit)", "maltego (OSINT)"],
    },

    "rootkits_persistence": {
        "title": "Rootkits & Persistence Mechanisms",
        "tldr": "Hiding malicious presence and surviving reboots.",
        "sections": [
            {
                "heading": "Types of Rootkits",
                "body": (
                    "User-space rootkits: replace system binaries (ls, ps, netstat) with "
                    "versions that hide the attacker's files and processes. Easy to detect "
                    "by comparing binaries against known-good hashes.\n\n"
                    "Kernel rootkits (LKM): loaded as kernel modules, hook syscalls. "
                    "When 'ps' calls getdents64 to list processes, the hooked version "
                    "omits attacker processes from results. Very hard to detect from within "
                    "the compromised OS.\n\n"
                    "Bootkits: infect the bootloader/MBR, load before the OS, "
                    "even before antivirus. Survive OS reinstallation."
                ),
            },
            {
                "heading": "Persistence Methods",
                "body": (
                    "Cron jobs: scheduled tasks that re-establish the backdoor if removed.\n"
                    "Systemd services: a 'maintenance' service that starts on boot.\n"
                    "LD_PRELOAD hooks: library injection that affects all processes.\n"
                    "Bashrc/profile: code that runs every time a shell opens.\n"
                    "SSH authorized_keys: attacker's public key grants permanent access.\n\n"
                    "Windows: Registry run keys, scheduled tasks, service installation, "
                    "DLL hijacking, WMI subscriptions."
                ),
            },
            {
                "heading": "Detection",
                "body": (
                    "File integrity monitoring (Tripwire, AIDE): hash all system files and "
                    "alert when they change.\n\n"
                    "Cross-view detection: compare process list from inside OS vs from "
                    "hypervisor or hardware — discrepancies reveal hidden processes.\n\n"
                    "Memory forensics (Volatility): analyse raw memory for hooks, "
                    "hidden modules, injected code.\n\n"
                    "Secure boot + module signing: prevents unsigned kernel modules from loading."
                ),
            },
        ],
        "real_world": "The 2020 SolarWinds compromise planted a backdoor (SUNBURST) in software updates that persisted on 18,000 networks including US Treasury and NSA. Went undetected for 9 months.",
        "tools": ["volatility (forensics)", "chkrootkit", "rkhunter", "AIDE"],
    },

    "c2_infrastructure": {
        "title": "Command & Control Infrastructure",
        "tldr": "How attackers communicate with compromised systems.",
        "sections": [
            {
                "heading": "The C2 Model",
                "body": (
                    "Once an attacker has a foothold (an implant on a compromised system), "
                    "they need to communicate with it to issue commands and receive results. "
                    "This is the C2 (or C&C) channel.\n\n"
                    "The implant periodically 'beacons' home — checks in for instructions. "
                    "C2 traffic must blend in with normal network traffic to avoid detection."
                ),
            },
            {
                "heading": "C2 Evasion Techniques",
                "body": (
                    "DNS C2: commands encoded in DNS queries/responses. DNS is rarely blocked "
                    "and hard to fully inspect. Tool: iodine, dnscat2.\n\n"
                    "HTTPS C2: traffic looks identical to normal web browsing. "
                    "Tools: Cobalt Strike, Metasploit, Sliver.\n\n"
                    "Domain Fronting: route C2 traffic through CDN infrastructure (Cloudflare, "
                    "AWS) making the destination appear to be a legitimate service.\n\n"
                    "Steganography: hide commands in images posted to public platforms."
                ),
            },
            {
                "heading": "Detection",
                "body": (
                    "Beaconing detection: implants phone home on a timer — look for "
                    "regular interval connections to external IPs.\n\n"
                    "DNS analytics: unusually long DNS queries, high-entropy subdomains, "
                    "queries to recently registered domains.\n\n"
                    "Threat intelligence: blocklists of known C2 infrastructure (Abuse.ch, "
                    "MISP, VirusTotal).\n\n"
                    "Network segmentation: internal systems that shouldn't make outbound "
                    "connections are blocked by egress filtering."
                ),
            },
        ],
        "real_world": "APT29 (Cozy Bear, Russian GRU) used Twitter posts as a C2 channel — commands hidden in tweets from compromised or dummy accounts. The C2 traffic looked like social media use.",
        "tools": ["cobalt strike (commercial)", "sliver", "metasploit", "wireshark for detection"],
    },

    "lateral_movement_airgap": {
        "title": "Lateral Movement & Air Gap Attacks",
        "tldr": "Moving from one compromised system to others on the network.",
        "sections": [
            {
                "heading": "Lateral Movement Techniques",
                "body": (
                    "Pass-the-Hash: use a captured NTLM password hash directly for "
                    "authentication without cracking it — Windows-specific.\n\n"
                    "Pass-the-Ticket: steal Kerberos tickets and use them to authenticate "
                    "to other services — the 'Golden Ticket' attack creates a ticket for any user.\n\n"
                    "Remote service exploitation: use credentials or vulnerabilities to "
                    "compromise adjacent systems (RDP, SMB, SSH, WMI).\n\n"
                    "Living off the land: use built-in OS tools (PowerShell, WMI, psexec) "
                    "to move laterally — harder to detect as 'malware'."
                ),
            },
            {
                "heading": "Air Gap Bridging",
                "body": (
                    "Air-gapped systems are physically isolated from internet-connected networks. "
                    "Historically considered unbreakable. But:\n\n"
                    "USB drops: Stuxnet spread via infected USB drives to Iranian nuclear facility.\n\n"
                    "Acoustic: researchers transmitted data using computer fan noise.\n\n"
                    "RF emissions: 'TEMPEST' attacks capture electromagnetic emissions from monitors.\n\n"
                    "Supply chain: compromise the software or hardware before it reaches the facility.\n\n"
                    "Insider: the most common — a human who bridges the gap, knowingly or not."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "Network segmentation with strict ACLs and firewall rules.\n"
                    "Micro-segmentation: each system only communicates with specific others.\n"
                    "Privileged Access Workstations (PAW): dedicated machines for admin tasks, "
                    "not used for email or web browsing.\n"
                    "Credential tiering: admin accounts for Tier 0 (domain controllers) "
                    "cannot be used on Tier 1/2 systems.\n"
                    "Air gap procedures: strict physical security, no removable media."
                ),
            },
        ],
        "real_world": "Stuxnet (2010) destroyed Iranian nuclear centrifuges after spreading via USB drives across an air gap — the first known nation-state cyberweapon to cause physical destruction.",
        "tools": ["bloodhound (AD attack paths)", "impacket", "crackmapexec"],
    },

    "zero_day_exploits": {
        "title": "Zero-Day Vulnerabilities",
        "tldr": "Vulnerabilities unknown to the vendor — no patch exists.",
        "sections": [
            {
                "heading": "What is a Zero-Day?",
                "body": (
                    "A vulnerability is 'zero-day' (0-day) when the software vendor has "
                    "had zero days to prepare a patch — because they don't know it exists.\n\n"
                    "Timeline of a vulnerability:\n"
                    "T=0: Vulnerability created (a developer writes flawed code)\n"
                    "T+X: Someone discovers it (researcher, attacker, or both)\n"
                    "T+Y: Vendor is notified (responsible disclosure) or it's sold/exploited\n"
                    "T+Z: Patch released\n"
                    "T+Z+: Still unpatched on most systems\n\n"
                    "The window between T+X (discovery) and T+Z (patch) is when it's 0-day."
                ),
            },
            {
                "heading": "The Zero-Day Market",
                "body": (
                    "Zero-days are bought and sold:\n\n"
                    "Bug bounty programmes (ethical): Google pays up to $250K for Chrome. "
                    "Apple up to $1M for iPhone kernel exploits. Microsoft, Meta, others pay.\n\n"
                    "Brokers (grey): Zerodium publicly pays $2.5M for iOS full chain. "
                    "These are often resold to governments.\n\n"
                    "Exploit vendors (controversial): NSO Group sold Pegasus "
                    "(mobile zero-day exploit suite) to governments who used it "
                    "to target journalists and dissidents.\n\n"
                    "Responsible disclosure is the ethical path — and now often the financially "
                    "comparable one due to bug bounties."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "You can't patch what you don't know about. Defence in depth matters most:\n\n"
                    "Sandboxing: even if code executes, it's in a restricted environment.\n"
                    "Exploit mitigations: ASLR, DEP, CFI make exploitation harder even for 0-days.\n"
                    "Least privilege: compromising one service shouldn't compromise the host.\n"
                    "Telemetry and anomaly detection: unusual process behaviour may reveal exploitation.\n"
                    "Threat intelligence: nation-state 0-days often get burned; signatures emerge."
                ),
            },
        ],
        "real_world": "EternalBlue (CVE-2017-0144) was an NSA 0-day against Windows SMB, stolen and leaked by Shadow Brokers. It was then weaponised in WannaCry and NotPetya — ransomware attacks that cost $10+ billion globally.",
        "tools": ["fuzzing (AFL++, LibFuzzer)", "static analysis (semgrep)", "exploit-db"],
    },

    "race_conditions_timing": {
        "title": "Race Conditions & Timing Attacks",
        "tldr": "Exploiting the gap between when a check happens and when it's used.",
        "sections": [
            {
                "heading": "TOCTOU — Time of Check to Time of Use",
                "body": (
                    "Classic race condition:\n\n"
                    "1. Program checks: 'Does this user have permission to access /etc/shadow?'\n"
                    "2. [tiny gap]\n"
                    "3. Program uses: opens /etc/shadow\n\n"
                    "Attacker in the gap: replaces /etc/shadow with a symlink to a file they "
                    "control — or replaces the target file with /etc/shadow.\n\n"
                    "The check was on one thing; the use operates on another."
                ),
            },
            {
                "heading": "Cryptographic Timing Attacks",
                "body": (
                    "When comparing a submitted password/token with the real one, "
                    "a naive comparison:\n\n"
                    "  if submitted == real: return True\n\n"
                    "Returns slightly faster if the first character matches (comparison stops "
                    "early on mismatch). An attacker can measure nanosecond timing differences "
                    "to determine characters one by one — effectively brute-forcing without "
                    "any lockout triggering.\n\n"
                    "Fix: constant-time comparison functions that always take the same time "
                    "regardless of where the mismatch occurs."
                ),
            },
            {
                "heading": "Defence",
                "body": (
                    "Atomic operations: use OS primitives that check and act as a single "
                    "indivisible operation — no gap to exploit.\n\n"
                    "Mutex locks: ensure only one thread can execute critical sections.\n\n"
                    "Constant-time comparison: for any security-sensitive comparison (HMAC, tokens).\n\n"
                    "HSMs: Hardware Security Modules perform cryptographic operations internally — "
                    "no timing data leaks out."
                ),
            },
        ],
        "real_world": "CVE-2022-21449 (Psychic Signatures): a Java ECDSA signature verification bug that allowed forging signatures by submitting r=0, s=0. Bypassed authentication in Java-based OAuth/JWT systems.",
        "tools": ["pwntools (race exploits)", "time-memory trade-off analysis"],
    },

    "pki_certificate_trust": {
        "title": "Public Key Infrastructure & Certificate Trust",
        "tldr": "The chain of trust that makes HTTPS and email authentication work.",
        "sections": [
            {
                "heading": "How PKI Works",
                "body": (
                    "Public Key Infrastructure is a hierarchy of trust:\n\n"
                    "Root CA: the ultimate authority (a few dozen worldwide — DigiCert, "
                    "Let's Encrypt, etc.). Their root certificates are baked into browsers/OS.\n\n"
                    "Intermediate CA: signs certificates on behalf of the root, limiting risk.\n\n"
                    "End-entity certificate: the certificate your bank's website presents. "
                    "Signed by Intermediate, which is signed by Root.\n\n"
                    "Your browser trusts bank.com because it trusts the chain back to a "
                    "Root CA it was pre-loaded to trust."
                ),
            },
            {
                "heading": "Attack Vectors",
                "body": (
                    "Rogue CA: compromise an intermediate CA and issue certificates for "
                    "any domain. Happened to DigiNotar (2011) and CNNIC (2015).\n\n"
                    "Certificate Mis-issuance: trick a CA into issuing a cert for a domain "
                    "you don't own (domain validation can be fooled).\n\n"
                    "Private key theft: steal the private key corresponding to a certificate "
                    "— now you can impersonate that server.\n\n"
                    "BGP hijacking: reroute traffic to a malicious server before it even "
                    "reaches TLS negotiation."
                ),
            },
            {
                "heading": "Certificate Transparency",
                "body": (
                    "Introduced after the DigiNotar breach, Certificate Transparency (CT) "
                    "requires all publicly-trusted certificates to be logged in public, "
                    "append-only logs.\n\n"
                    "This means: if a rogue CA issues a certificate for google.com, "
                    "Google will see it in the CT log immediately and can alert browsers "
                    "to distrust it — even before it's used in an attack.\n\n"
                    "Tools like crt.sh let anyone see every certificate ever issued for a domain."
                ),
            },
        ],
        "real_world": "In 2017, Google caught Symantec (a major CA) mis-issuing certificates. Symantec's CA business was eventually distrusted by all major browsers and transferred to DigiCert.",
        "tools": ["openssl", "crt.sh (CT transparency)", "ssllabs.com (cert audit)"],
    },
}

# ─────────────────────────────────────────────
# TARGET NODES
# ─────────────────────────────────────────────

TARGETS = {
    "mediabridge-relay": {
        "name": "MEDIABRIDGE-RELAY-01",
        "ip": "10.44.12.8",
        "type": "RELAY",
        "org": "MediaBridge Networks (OmniCorp subsidiary)",
        "os": "Ubuntu 20.04.3 LTS",
        "ports": [21, 22, 80, 8080],
        "sec_level": 1,
        "sec_label": "LOW",
        "services": {21: "vsftpd 3.0.3", 22: "OpenSSH 8.2p1", 80: "nginx/1.18.0", 8080: "Apache Tomcat/9.0.41"},
        "vulns": ["CVE-2021-3156 (sudo heap overflow)", "Anonymous FTP enabled", "Outdated Tomcat"],
        "data": {"config_backup": "mediabridge-relay.conf.bak", "routing_table": "routes_internal.xml"},
        "lore": "Low-traffic relay node. Likely forgotten during last security audit.",
    },
    "mediabridge-cms": {
        "name": "MEDIABRIDGE-CMS",
        "ip": "10.44.12.19",
        "type": "CMS",
        "org": "MediaBridge Networks",
        "os": "Windows Server 2016",
        "ports": [80, 443, 3389],
        "sec_level": 1,
        "sec_label": "LOW",
        "services": {80: "IIS 10.0", 443: "IIS 10.0 (TLS 1.2)", 3389: "RDP — MS-RDPBCGR"},
        "vulns": ["Default credentials (admin/admin123)", "RDP exposed publicly", "No MFA"],
        "data": {"cms_admin": "Credentials for CMS admin panel", "traffic_logs": "6 months of CDN traffic logs"},
        "lore": "Content management server. IT deployed it in 2019 and apparently never touched it again.",
    },
    "mediabridge-db": {
        "name": "MEDIABRIDGE-DB",
        "ip": "10.44.12.33",
        "type": "DB",
        "org": "MediaBridge Networks",
        "os": "CentOS 7.9",
        "ports": [22, 3306, 8080],
        "sec_level": 1,
        "sec_label": "LOW",
        "services": {22: "OpenSSH 7.4p1", 3306: "MySQL 5.7.33", 8080: "phpMyAdmin 5.0.2"},
        "vulns": ["SQL injection in web portal login", "phpMyAdmin exposed", "MySQL root without password on localhost"],
        "data": {"routing_db": "lazarus_routing_map.sql", "customer_data": "11.2M routing records"},
        "lore": "The database backing MediaBridge's customer portal. phpMyAdmin is publicly accessible. Someone is going to regret this.",
    },
    "cdn-edge-node-7": {
        "name": "CDN-EDGE-07",
        "ip": "203.55.12.7",
        "type": "CDN",
        "org": "OmniCorp CDN Division",
        "os": "Debian 11 (Bullseye)",
        "ports": [80, 443, 8443],
        "sec_level": 2,
        "sec_label": "MEDIUM",
        "services": {80: "nginx/1.20.2", 443: "nginx TLS 1.3", 8443: "OmniCDN Management v3.1"},
        "vulns": ["TLS certificate chain not validated", "No HSTS", "Weak cipher suite (RC4 fallback)"],
        "data": {"lazarus_packets": "LAZARUS-tagged traffic samples", "routing_headers": "Internal routing metadata"},
        "lore": "OmniCorp CDN edge. Handles ~2.3 Tbps of traffic globally. The TLS misconfiguration is ironic given what they route.",
    },
    "omnicorp-legacy-auth": {
        "name": "OMNICORP-AUTH-LEGACY",
        "ip": "172.16.8.4",
        "type": "AUTH",
        "org": "OmniCorp Internal",
        "os": "RHEL 6.10 (EOL)",
        "ports": [22, 443, 8000],
        "sec_level": 2,
        "sec_label": "MEDIUM",
        "services": {22: "OpenSSH 6.6.1p1", 443: "Apache 2.2.15", 8000: "OmniAuth Daemon v2.3 (custom C)"},
        "vulns": ["Stack buffer overflow in OmniAuth session handler", "RHEL 6 EOL (no patches since 2020)", "Outdated OpenSSH"],
        "data": {"session_tokens": "Active admin session tokens", "auth_logs": "6 months auth history"},
        "lore": "Legacy authentication server that was 'scheduled for decommission in Q3 2020'. It's Q4 now. Of 2024.",
    },
    "omnicorp-hr": {
        "name": "OMNICORP-HRPORTAL",
        "ip": "172.16.10.22",
        "type": "HR",
        "org": "OmniCorp Human Resources",
        "os": "Windows Server 2019",
        "ports": [80, 443],
        "sec_level": 2,
        "sec_label": "MEDIUM",
        "services": {80: "IIS 10.0 (redirect)", 443: "IIS 10.0 TLS 1.3"},
        "vulns": ["No MFA on SSO login", "SPF record missing", "No DMARC policy"],
        "data": {"hr_db": "OmniCorp employee database including LAZARUS personnel", "sso_tokens": "SSO session tokens"},
        "lore": "HR portal. No MFA. SPF missing — emails can be spoofed from @omnicorp.com trivially. Priya finds this professionally offensive.",
    },
    "omnicorp-db-primary": {
        "name": "OMNICORP-DB-PRIMARY",
        "ip": "172.16.20.5",
        "type": "DB",
        "org": "OmniCorp Core Infrastructure",
        "os": "RHEL 8.5",
        "ports": [22, 5432],
        "sec_level": 3,
        "sec_label": "HIGH",
        "services": {22: "OpenSSH 8.0p1", 5432: "PostgreSQL 14.1"},
        "vulns": ["Kernel 5.15 vulnerable to CVE-2022-0847 (Dirty Pipe)", "Unsigned kernel modules accepted"],
        "data": {"lazarus_schema_ref": "Partial LAZARUS schema reference", "employee_records": "Full OmniCorp staff DB"},
        "lore": "Core OmniCorp database. Hardened, but the kernel hasn't been patched since September. Kai spotted this from a banner.",
    },
    "voss-hunting-team": {
        "name": "OBSIDIAN-C2-SERVER",
        "ip": "185.44.211.3",
        "type": "C2",
        "org": "Obsidian Group (Voss's private cyber team)",
        "os": "Kali Linux (ironic)",
        "ports": [443, 8443, 4444],
        "sec_level": 3,
        "sec_label": "HIGH",
        "services": {443: "Cobalt Strike Team Server", 8443: "Management interface", 4444: "Meterpreter listener"},
        "vulns": ["Cobalt Strike default malleable C2 profile (detectable)", "Management interface exposed on internet"],
        "data": {"nexus_intel": "What Obsidian knows about NEXUS", "operator_list": "Names of Obsidian operators"},
        "lore": "The hunters' own C2. The irony of an offensive security firm running Cobalt Strike with default configs is not lost on Vera.",
    },
    "lazarus-schema-server": {
        "name": "LAZARUS-SCHEMA-AIR",
        "ip": "10.0.0.1 (internal only)",
        "type": "AIRGAP",
        "org": "OmniCorp Classified",
        "os": "Fedora 36 (custom hardened)",
        "ports": [22],
        "sec_level": 4,
        "sec_label": "CRITICAL",
        "services": {22: "OpenSSH 9.0p1 (cert auth only)"},
        "vulns": ["Air gap bridged via shared backup drive with omnicorp-db-primary"],
        "data": {"lazarus_full_schema": "Complete LAZARUS network architecture diagram", "node_map": "All 847 LAZARUS nodes globally"},
        "lore": "Air-gapped. Theoretically unreachable. Someone attached a USB backup drive to both this and the primary DB server. Kai found it in a backup log.",
    },
    "lazarus-command-node": {
        "name": "LAZARUS-CMD-NODE",
        "ip": "classified",
        "type": "C2",
        "org": "OmniCorp Black Budget",
        "os": "Custom hardened Linux",
        "ports": [443, 9443],
        "sec_level": 4,
        "sec_label": "CRITICAL",
        "services": {443: "LAZARUS Control Plane v4.1", 9443: "IPC daemon v1.0 (custom C, unaudited)"},
        "vulns": ["CVE-0000-00000: Memory corruption in IPC daemon (Kai's 0-day)"],
        "data": {"launch_config": "LAZARUS launch configuration and target list", "activation_timer": "72-hour countdown"},
        "lore": "The heart of PROJECT LAZARUS. Custom everything. One unaudited daemon. One zero-day. That's all we need.",
    },
    "lazarus-auth-server": {
        "name": "LAZARUS-AUTH",
        "ip": "classified",
        "type": "AUTH",
        "org": "OmniCorp Black Budget",
        "os": "Custom hardened Linux + HSM",
        "ports": [443],
        "sec_level": 4,
        "sec_label": "CRITICAL",
        "services": {443: "LAZARUS Auth Service + Thales Luna HSM"},
        "vulns": ["Race condition in credential validation routine (timing attack)"],
        "data": {"launch_keys": "LAZARUS arming credentials", "key_ceremony_log": "Key generation audit trail"},
        "lore": "HSM is theoretically unbreakable. The software around it isn't.",
    },
    "voss-dead-mans-relay": {
        "name": "VOSS-DMR-01",
        "ip": "classified",
        "type": "RELAY",
        "org": "Private (Voss personal)",
        "os": "Alpine Linux",
        "ports": [443],
        "sec_level": 4,
        "sec_label": "CRITICAL",
        "services": {443: "Mutual TLS relay (client cert required)"},
        "vulns": ["Client certificate issued by OmniCorp internal CA (which we own)"],
        "data": {"dead_mans_trigger": "Automatic LAZARUS trigger if Voss goes offline"},
        "lore": "Voss's insurance policy. If he's taken offline, this fires LAZARUS automatically. We own the CA that issued its certificate.",
    },
}

# ─────────────────────────────────────────────
# ITEMS / UPGRADES
# ─────────────────────────────────────────────

ITEMS = {
    "proxy_chain_v1": {
        "name": "Proxy Chain v1",
        "desc": "Route traffic through 3 anonymous proxies. Reduces trace generation by 40%.",
        "type": "passive",
        "effect": {"trace_multiplier": 0.6},
        "icon": "🔗",
    },
    "keylogger_passive": {
        "name": "Passive Keylogger",
        "desc": "Silently captures keystrokes on compromised hosts. Useful for credential harvesting.",
        "type": "tool",
        "effect": {"unlock_tool": "keylog"},
        "icon": "⌨️",
    },
    "sqlmap_custom": {
        "name": "Custom SQLMap Build",
        "desc": "Optimised SQLi tool with OmniCorp-specific tampers. +25% success on their web apps.",
        "type": "tool",
        "effect": {"sql_bonus": 25},
        "icon": "💉",
    },
    "ssl_intercept_cert": {
        "name": "SSL Intercept Certificate",
        "desc": "Rogue intermediate CA cert. Required for TLS MITM on OmniCorp infrastructure.",
        "type": "key_item",
        "effect": {"unlock_mitm": True},
        "icon": "🔏",
    },
    "rop_chain_kit": {
        "name": "ROP Chain Toolkit",
        "desc": "Pre-built gadget chains for RHEL/Debian targets. Bypasses NX/DEP on buffer overflows.",
        "type": "tool",
        "effect": {"overflow_bonus": 30},
        "icon": "⛓️",
    },
    "sso_token_omnicorp": {
        "name": "OmniCorp SSO Token",
        "desc": "Valid SSO session token for omnicorp.com. Opens HR portal access.",
        "type": "key_item",
        "effect": {"unlock_target": "omnicorp-hr-internal"},
        "icon": "🎫",
    },
    "lkm_rootkit": {
        "name": "Nexus LKM Rootkit",
        "desc": "Kernel-level rootkit providing persistent hidden access. Survives reboots.",
        "type": "implant",
        "effect": {"persist_on": ["omnicorp-db-primary"]},
        "icon": "🦠",
    },
    "c2_intercept_data": {
        "name": "Obsidian C2 Intel",
        "desc": "Everything Voss's team knows about NEXUS. Critical operational intelligence.",
        "type": "intel",
        "effect": {"trace_reset": -20, "unlock_chapter": "ch4"},
        "icon": "📡",
    },
    "lazarus_schema": {
        "name": "LAZARUS Architecture Schema",
        "desc": "Complete diagram of all 847 LAZARUS nodes. The smoking gun.",
        "type": "evidence",
        "effect": {"story_progress": True},
        "icon": "🗺️",
    },
    "lazarus_config": {
        "name": "LAZARUS Launch Config",
        "desc": "The command configuration for LAZARUS activation. Priya needs this.",
        "type": "evidence",
        "effect": {"story_progress": True},
        "icon": "📋",
    },
    "lazarus_keys_null": {
        "name": "Nullified Launch Keys",
        "desc": "LAZARUS authentication credentials — invalidated. It cannot arm.",
        "type": "evidence",
        "effect": {"story_progress": True},
        "icon": "🔑",
    },
    "relay_disabled": {
        "name": "Dead Man's Switch: DISABLED",
        "desc": "Voss's automatic LAZARUS trigger has been deactivated.",
        "type": "evidence",
        "effect": {"story_progress": True},
        "icon": "🔴",
    },
}
