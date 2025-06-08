from typing import Literal
from ..shared import types as shared_types
from . import ServerPacket, types


class Hall(ServerPacket):
    __packet_key__ = "hall"
    type: Literal["bronze", "silver", "gold"]
    desc: dict[str, dict[str, str]]
    items: dict[str, list[types.HallItem]]


class Leaderboard(ServerPacket):
    __packet_key__ = "lb"
    type: shared_types.LEADERBOARD_TYPE
    kind: Literal["user", "top", "up", "down"]
    rows: list[types.LeaderboardUser]
