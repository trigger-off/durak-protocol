from typing import Any

from . import ServerPacket


class UserUpdate(ServerPacket):
    __packet_key__ = "uu"
    k: str
    v: Any | None = None


class DeleteNotice(ServerPacket):
    __packet_key__ = "delete_notice"
    token: str


class DeleteAccount(ServerPacket):
    __packet_key__ = "delete_account"
    token: str


class RemoveDeletion(ServerPacket):
    __packet_key__ = "remove_deletion"
    token: str
