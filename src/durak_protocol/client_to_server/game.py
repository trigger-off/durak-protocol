from typing import Literal

from . import ClientPacket, Field


class Join(ClientPacket):
    __packet_key__ = "join"
    id: int
    password: str | None = None


class Rejoin(ClientPacket):
    __packet_key__ = "rejoin"
    id: int
    p: int


class Create(ClientPacket):
    __packet_key__ = "create"
    bet: int
    players: int
    deck: int
    sw: bool
    nb: bool
    ch: bool
    dr: bool | None = None
    fast: bool
    password: str | None = None


class InviteToGame(ClientPacket):
    __packet_key__ = "invite_to_game"
    user_id: int


class PlayerSwap(ClientPacket):
    __packet_key__ = "player_swap"
    id: int


class Leave(ClientPacket):
    __packet_key__ = "leave"
    id: int


class SwapCard(ClientPacket):
    __packet_key__ = "s"
    c: str = Field(..., title="Swap Card")


class ThrowCard(ClientPacket):
    __packet_key__ = "t"
    c: str = Field(..., title="Throw Card")


class FollowCard(ClientPacket):
    __packet_key__ = "f"
    c: str = Field(..., title="Follow Card")


class BeatCard(ClientPacket):
    __packet_key__ = "b"
    c: str = Field(..., title="Beaten Card")
    b: str = Field(..., title="Beating Card")


class CheatThrowCard(ClientPacket):
    __packet_key__ = "cht"
    c: str = Field(..., title="Cheated Throw Card")


class CheatBeatCard(ClientPacket):
    __packet_key__ = "chb"
    c: str = Field(..., title="Cheated Beaten Card")
    b: str = Field(..., title="Cheated Beating Card")


class SendSmile(ClientPacket):
    __packet_key__ = "smile"
    id: int | None = None


class LookupStart(ClientPacket):
    __packet_key__ = "lookup_start"
    betMin: int | None = None
    betMax: int | None = None
    players: list[int] | None = None
    deck: list[int] | None = None
    sw: list[bool] | None = None
    nb: list[bool] | None = None
    ch: list[bool] | None = None
    dr: list[bool] | None = None
    fast: list[bool] | None = None
    pr: list[bool]
    status: Literal["open"]


class GetBets(ClientPacket):
    __packet_key__ = "gb"


class GetTable(ClientPacket):
    __packet_key__ = "get_table"


class GetHands(ClientPacket):
    __packet_key__ = "get_hands"


class GamePublish(ClientPacket):
    __packet_key__ = "game_publish"


class Surrender(ClientPacket):
    __packet_key__ = "surrender"


class Ready(ClientPacket):
    __packet_key__ = "ready"


class Pass(ClientPacket):
    __packet_key__ = "pass"


class Done(ClientPacket):
    __packet_key__ = "done"


class Take(ClientPacket):
    __packet_key__ = "take"


class Confirm(ClientPacket):
    __packet_key__ = "confirm"


# Features

class CardReturn(ClientPacket):
    __packet_key__ = "card_return"


class Highlight(ClientPacket):
    __packet_key__ = "highlight"


class ShowDiscard(ClientPacket):
    __packet_key__ = "show_discard"


class QuickGame(ClientPacket):
    __packet_key__ = "quick_game"


class LookupStop(ClientPacket):
    __packet_key__ = "lookup_stop"
