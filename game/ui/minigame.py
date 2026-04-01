"""NEXUS — Minigame Controller"""


class MinigameController:
    """
    Manages which minigame to run for each exploit type.
    Returns a score 0.0–1.0 that feeds into exploit success probability.
    """

    # Map exploit category -> minigame type
    GAME_MAP = {
        "portscan":         "port_mapper",
        "recon":            "port_mapper",
        "bruteforce":       "cipher_decoder",
        "sshcrack":         "cipher_decoder",
        "sqlinject":        "cipher_decoder",
        "overflow":         "firewall_bypass",
        "shellcode":        "firewall_bypass",
        "mitm":             "port_mapper",
        "arp_spoof":        "port_mapper",
        "ssl_strip":        "cipher_decoder",
        "implant":          "firewall_bypass",
        "persist":          "firewall_bypass",
        "exfil":            "port_mapper",
        "lkm_compile":      "firewall_bypass",
        "kernel_inject":    "firewall_bypass",
        "syscall_hook":     "cipher_decoder",
        "osint":            "port_mapper",
        "craft_phish":      "cipher_decoder",
        "credential_harvest": "cipher_decoder",
        "c2_recon":         "port_mapper",
        "lateral_move":     "firewall_bypass",
        "c2_access":        "firewall_bypass",
        "internal_recon":   "port_mapper",
        "lateral_pivot":    "firewall_bypass",
        "airgap_bridge":    "firewall_bypass",
        "schema_extract":   "port_mapper",
        "zeroday_prep":     "firewall_bypass",
        "ipc_corrupt":      "firewall_bypass",
        "config_extract":   "port_mapper",
        "clean_exit":       "port_mapper",
        "timing_analysis":  "cipher_decoder",
        "race_exploit":     "firewall_bypass",
        "key_invalidate":   "cipher_decoder",
        "ca_access":        "cipher_decoder",
        "forge_cert":       "cipher_decoder",
        "relay_auth":       "firewall_bypass",
        "relay_disable":    "firewall_bypass",
        "token_extract":    "port_mapper",
        "verify_hidden":    "port_mapper",
        # Malware analysis exploits
        "file_extract":     "port_mapper",
        "static_analysis":  "cipher_decoder",
        "string_dump":      "cipher_decoder",
        "ioc_extract":      "cipher_decoder",
        "sandbox_prep":     "firewall_bypass",
        "detonate":         "firewall_bypass",
        "behaviour_log":    "port_mapper",
        "network_capture":  "port_mapper",
        "report_iocs":      "cipher_decoder",
    }

    def get_game_type(self, exploit_id: str) -> str:
        return self.GAME_MAP.get(exploit_id, "port_mapper")
