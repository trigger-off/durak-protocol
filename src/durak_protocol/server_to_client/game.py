from . import ServerPacket, Field, types


class Smile(ServerPacket):
    __packet_key__ = "smile"
    p: int = Field(..., description="Relative Player ID")
    id: int = Field(..., description="Smile ID")
    a: str = Field(..., description="Smile Asset ID")


class GameList(ServerPacket):
    __packet_key__ = "gl"
    g: list[types.Game]


class Game(ServerPacket, types.Game):
    __packet_key__ = "g"


class GameDelete(ServerPacket):
    __packet_key__ = "gd"
    id: int


class Bets(ServerPacket):
    __packet_key__ = "bets"
    v: list[int]


class InviteToGame(ServerPacket):
    __packet_key__ = "invite_to_game"
    alert: str
    game_id: int
    password: str | None = None
    server: str
