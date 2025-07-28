from datetime import datetime
from typing import Literal

from . import ServerPacket, BaseModel


class Free(ServerPacket):
    __packet_key__ = "free"
    count: int
    delay: int


class ScreenChange(ServerPacket):
    __packet_key__ = "screen_change"
    name: Literal[
        "game_list", "options", "game_create", "shop_coins", "shop_points", "rules", "leaders", "main", "tour"]


class Alert(ServerPacket):
    __packet_key__ = "alert"
    text: dict[str, str]


class Message(ServerPacket):
    __packet_key__ = "message"
    text: dict[str, str]


class FunctionalIsUnavailable(ServerPacket):
    __packet_key__ = "functional_is_unavailable"
    until: datetime | str

class AdInfo(BaseModel):
    id: str
    state: bool

class AdNets(ServerPacket):
    __packet_key__ = "ad_nets"
    ids: list[AdInfo]