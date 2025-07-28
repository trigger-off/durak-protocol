from . import ServerPacket, types, Field


class Tournament(ServerPacket):
    __packet_key__ = "tour"
    data: types.TournamentData


class GiveTourReward(ServerPacket):
    __packet_key__ = "give_tour_reward"
    place: str
    amount: int


class TourStartTimer(ServerPacket):
    __packet_key__ = "tour_start_timer"
    timeout: int


class TourScore(ServerPacket):
    __packet_key__ = "tour_score"
    one: int | None = Field(None, alias="0")
    two: int | None = Field(None, alias="1")


class TourWin(ServerPacket):
    __packet_key__ = "tour_win"


class TourGameStart(ServerPacket):
    __packet_key__ = "tour_game_start"


class TourGameStop(ServerPacket):
    __packet_key__ = "tour_game_stop"
