from . import ServerPacket

from datetime import datetime


class Sign(ServerPacket):
    __packet_key__ = "sign"
    key: str


class Server(ServerPacket):
    __packet_key__ = "server"
    time: datetime  # UTC
    id: str


class Error(ServerPacket):
    __packet_key__ = "err"
    code: str


class ChangeServer(ServerPacket):
    __packet_key__ = "change_server"
    id: str


class Confirmed(ServerPacket):
    __packet_key__ = "confirmed"
