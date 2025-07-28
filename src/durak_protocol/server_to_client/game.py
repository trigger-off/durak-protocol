from typing import Any

from pydantic import ConfigDict

from . import ServerPacket, Field, types


class Smile(ServerPacket):
    __packet_key__ = "smile"
    p: int = Field(..., description="Relative Player ID")
    id: int = Field(..., description="Smile ID")
    a: str = Field(..., description="Smile Asset ID")


class GameList(ServerPacket):
    __packet_key__ = "gl"
    g: list[types.Game]


class G(ServerPacket, types.Game):
    __packet_key__ = "g"


class Game(ServerPacket):
    __packet_key__ = "game"
    id: int
    players: int
    position: int
    deck: int
    timeout: int
    sw: bool
    ch: bool
    dr: bool
    nb: bool
    bet: int
    fast: bool
    password: str | None = None


class GameStatus(ServerPacket):
    __packet_key__ = "game_status"
    cards: dict[str, int]
    win: dict[str, int] | None = None
    off: dict[int, int] | None = None


class Features(ServerPacket):
    __packet_key__ = "features"
    hl: int
    dis: int
    cr: int


class Player(ServerPacket):
    __packet_key__ = "p"
    id: int
    shirt: types.Shirt | None = None
    user: types.UserFind | None = None
    swap: bool | None = None


class CPlayer(Player):
    __packet_key__ = "cp"


class PlayerPos(ServerPacket):
    __packet_key__ = "player_pos"
    id: int
    swap: bool | None = None


class PlayerSwapRequest(ServerPacket):
    __packet_key__ = "player_swap_request"
    id: int


class Order(ServerPacket):
    __packet_key__ = "order"
    ids: list[int]


class Turn(ServerPacket):
    __packet_key__ = "turn"
    deck: int
    trump: str
    discard: int
    table: dict | None = None  # unknown signature


class SwapCard(ServerPacket):
    __packet_key__ = "s"
    id: int
    c: str = Field(..., title="Swap Card")


class ThrowCard(ServerPacket):
    __packet_key__ = "t"
    id: int
    c: str = Field(..., title="Throw Card")


class FollowCard(ServerPacket):
    __packet_key__ = "f"
    id: int
    c: str = Field(..., title="Follow Card")


class BeatCard(ServerPacket):
    __packet_key__ = "b"
    id: int
    c: str = Field(..., title="Beaten Card")
    b: str = Field(..., title="Beating Card")


class ReturnThrowCard(ThrowCard):
    __packet_key__ = "rt"
    e: int | None = None


class ReturnFollowCard(ThrowCard):
    __packet_key__ = "rf"
    e: int | None = None


class ReturnSwapCard(ThrowCard):
    __packet_key__ = "rs"
    e: int | None = None


class ReturnBeatCard(BeatCard):
    __packet_key__ = "rb"
    p: int | None = None
    e: int | None = None


class ReturnCThrowCard(ThrowCard):
    __packet_key__ = "rct"
    p: int | None = None
    e: int | None = None


class ReturnCBeatCard(ThrowCard):
    __packet_key__ = "rcb"
    p: int | None = None
    e: int | None = None


class CheaterSwapCard(ThrowCard):
    __packet_key__ = "chs"
    ch: int | None = None
    sh: int | None = None
    c: dict | None = None


class Table(ServerPacket):
    __packet_key__ = "table"
    model_config = ConfigDict(extra='allow')


class Hands(ServerPacket):
    __packet_key__ = "hands"
    one: int = Field(..., alias="1")
    two: int = Field(..., alias="2")
    three: int = Field(..., alias="3")
    four: int = Field(..., alias="4")
    five: int = Field(..., alias="5")
    six: int = Field(..., alias="6")


class Bets(ServerPacket):
    __packet_key__ = "bets"


class Highlight(ServerPacket):
    __packet_key__ = "hl"
    c: list[str] | None = None


class Discard(ServerPacket):
    __packet_key__ = "discard"
    c: list[str] | None = None


class Win(ServerPacket):
    __packet_key__ = "win"
    id: int
    value: int


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


class Hand(ServerPacket):
    __packet_key__ = "hand"
    cards: list[str]


class ReadyOn(ServerPacket):
    __packet_key__ = "ready_on"
    id: int


class ReadyOff(ServerPacket):
    __packet_key__ = "ready_off"
    id: int


class PlayerOn(ServerPacket):
    __packet_key__ = "p_on"


class PlayerOff(ServerPacket):
    __packet_key__ = "p_off"


class BtnReadyOff(ServerPacket):
    __packet_key__ = "btn_ready_off"


class BtnReadyOn(ServerPacket):
    __packet_key__ = "btn_ready_on"


class GamePublic(ServerPacket):
    __packet_key__ = "game_public"


class GameReady(ServerPacket):
    __packet_key__ = "game_ready"


class GameStart(ServerPacket):
    __packet_key__ = "game_start"


class GameOver(ServerPacket):
    __packet_key__ = "game_over"


class GameReset(ServerPacket):
    __packet_key__ = "game_reset"


class EndTurn(ServerPacket):
    __packet_key__ = "end_turn"


class ReadyTimeout(ServerPacket):
    __packet_key__ = "ready_timeout"


class Surrender(ServerPacket):
    __packet_key__ = "surrender"


class Draw(ServerPacket):
    __packet_key__ = "draw"
