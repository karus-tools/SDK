from dataclasses import dataclass
from typing import List, Dict


@dataclass
class TwitchProfile:
    commands: List[Dict[str, str]]


class TwitchProfileFactory:

    @staticmethod
    def create_profile(data: dict) -> TwitchProfile:
        return TwitchProfile(
            commands=data["commands"]
        )
