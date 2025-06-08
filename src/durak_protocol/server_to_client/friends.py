from typing import Literal

from . import ServerPacket, types


class FriendListUpdate(ServerPacket):
    __packet_key__ = "fl_update"
    user: types.UserFind
    kind: Literal["REQUEST", "INVITE", "FRIEND"]
    new: bool


class FriendListDelete(ServerPacket):
    __packet_key__ = "fl_delete"
    id: int
