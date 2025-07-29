from datetime import datetime

from . import ServerPacket, types


class UsersFindResult(ServerPacket):
    __packet_key__ = "users_find_result"
    users: list[types.UserFind]


class UserInfo(ServerPacket):
    __packet_key__ = "user_info"
    id: int
    name: str
    avatar: str | None = None
    pw: int
    ach: list[int]
    achc: int
    t_bronze: int
    t_silver: int
    t_gold: int
    wins: int
    wins_s: int | None = None
    points_win: int
    points_win_s: int | None = None
    score: int
    score_s: int | None = None
    dtp: datetime
    frame: str | None = None
    assets: list[str]
    achieve: str | None = None
    achieves: list[str]
    coll: dict[str, types.CollectionAsset]
