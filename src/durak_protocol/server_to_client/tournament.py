from . import ServerPacket, types


class Tournament(ServerPacket):
    __packet_key__ = "tour"
    data: types.TournamentData


class GiveTourReward(ServerPacket):
    __packet_key__ = "give_tour_reward"
    place: str
    amount: int
