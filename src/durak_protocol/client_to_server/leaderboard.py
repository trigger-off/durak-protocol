from ..shared import types as shared_types
from . import ClientPacket


class GetByPlaceBase(ClientPacket):
    type: shared_types.LEADERBOARD_TYPE
    place: int


class GetByUserBase(ClientPacket):
    type: shared_types.LEADERBOARD_TYPE
    user_id: int


class GetTopBase(ClientPacket):
    type: shared_types.LEADERBOARD_TYPE


class GetByPlaceUp(GetByPlaceBase):
    __packet_key__ = "lb_get_by_place_up"


class GetByPlaceDown(GetByPlaceBase):
    __packet_key__ = "lb_get_by_place_down"


class GetByPlaceUpOnSeason(GetByPlaceBase):
    __packet_key__ = "s_lb_get_by_place_up"


class GetByPlaceDownOnSeason(GetByPlaceBase):
    __packet_key__ = "s_lb_get_by_place_down"


class GetByUser(GetByUserBase):
    __packet_key__ = "lb_get_by_user"


class GetByUserOnSeason(GetByUserBase):
    __packet_key__ = "s_lb_get_by_user"


class GetTop(GetTopBase):
    __packet_key__ = "lb_get_top"


class GetTopOnSeason(GetTopBase):
    __packet_key__ = "s_lb_get_top"


class GetHallBronze(ClientPacket):
    __packet_key__ = "get_hall_bronze"


class GetHallSilver(ClientPacket):
    __packet_key__ = "get_hall_silver"


class GetHallGold(ClientPacket):
    __packet_key__ = "get_hall_gold"
