from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Game:
    badge_id: int
    id: int
    name: str


@dataclass
class GamePlayed:
    game: Game
    time_played: str


@dataclass
class BloxboostProfile:
    balance: Optional[int] = None
    surveys_completed: Optional[int] = None
    invited_by: str = None
    referral_list: List[str] = field(default_factory=lambda: [])


@dataclass
class BloxearnProfile:
    website_id: int
    balance: int
    creation_date: str
    offers_completed_today: int


@dataclass
class RobloxProfile:
    games_played: List[GamePlayed]
    bloxboost_profile: BloxboostProfile
    bloxearn_profile: BloxearnProfile


class GamePlayedFactory:

    @staticmethod
    def create_game_played(game_data: dict) -> GamePlayed:
        return GamePlayed(
            game=Game(**game_data["game"]),
            time_played=game_data["time_played"]
        )


class RobloxProfileFactory:

    @staticmethod
    def create_profile(response_json: dict) -> RobloxProfile:
        return RobloxProfile(
            games_played=[
                GamePlayedFactory.create_game_played(game)
                for game in response_json["games_played"]
            ],
            bloxboost_profile=BloxboostProfile(
                **response_json["bloxboost"]
            ),
            bloxearn_profile=BloxearnProfile(
                **response_json["bloxearn"]
            )
        )
