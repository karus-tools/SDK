from dataclasses import dataclass, field
from typing import List


@dataclass
class MinecraftLogs:
    messages: List[str] = field(default_factory=lambda: [])


@dataclass
class PastUsername:
    date: str
    username: str


@dataclass
class MinecraftProfile:
    uuid: str = None
    language: str = None
    logs: MinecraftLogs = field(default_factory=lambda: MinecraftLogs(messages=[]))
    past_usernames: List[PastUsername] = field(default_factory=lambda: [])
    social_medias: List[str] = field(default_factory=lambda: [])


class MinecraftProfileFactory:

    @staticmethod
    def create_profile(response_json) -> MinecraftProfile:
        return MinecraftProfile(
            uuid=response_json["minecraft_uuid"],
            language=response_json["person_language"],
            logs=MinecraftLogs(
                messages=response_json["minecraft_logs_messages"]
            ),
            past_usernames=[
                PastUsername(
                    date=username_data["date"],
                    username=username_data["username"]
                )
                for username_data in response_json["minecraft_past_usernames"]
            ],
            social_medias=response_json["person_socialmedia_links"]
        )
