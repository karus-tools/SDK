import requests
from .utilities.errors import (
    InvalidRequestMethod
)

from .utilities.logger import create_logger

from .minecraft import MinecraftProfileFactory, MinecraftProfile
from .roblox import RobloxProfileFactory, RobloxProfile
from .twitch import TwitchProfileFactory, TwitchProfile


class Client:

    def __init__(self, logging_level=None):
        self.logging_level = logging_level
        self.base_url = "http://localhost:5000"
        self.session = requests.Session()
        self._logger = None
        self._factories = {
            "minecraft": MinecraftProfileFactory.create_profile,
            "roblox": RobloxProfileFactory.create_profile,
            "twitch": TwitchProfileFactory.create_profile
        }

    @property
    def logger(self):
        if self._logger is None:
            self._logger = create_logger(name="Client Logger", listen_type=self.logging_level)

        return self._logger

    def send_request(
        self,
        path: str,
        method: str,
        payload: dict = None
    ):

        url = f'{self.base_url}{path}'

        if method == "GET":
            self.logger.debug(f"Sent GET request to {url}.")
            return self.session.get(url=url)

        elif method == "POST":
            self.logger.debug(f"Sent POST request to {url} with payload: {payload}.")
            return self.session.post(url=url, json=payload)

        self.logger.error("Failed to send request because method is invalid.")
        raise InvalidRequestMethod(f"Invalid method {method}")

    def _make_lookup(self, lookup_name: str, args):
        self.logger.debug(f"Making Lookup for module: {lookup_name} with arguments {args}")
        response = self.send_request(
            path=f"/lookup/{lookup_name}",
            method="POST",
            payload=args
        )

        response_json = response.json()
        if response_json["success"]:
            return self._factories[lookup_name](response_json)

        else:
            return None

    def minecraft_lookup(self, username: str) -> MinecraftProfile | None:
        return self._make_lookup(
            lookup_name="minecraft",
            args={"minecraft_username": username}
        )

    def roblox_lookup(self, username: str) -> RobloxProfile | None:
        return self._make_lookup(
            lookup_name="roblox",
            args={"roblox_username": username}
        )

    def twitch_lookup(self, username: str) -> TwitchProfile | None:
        return self._make_lookup(
            lookup_name="twitch",
            args={"twitch_name": username}
        )
