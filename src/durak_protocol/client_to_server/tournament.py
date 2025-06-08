from . import ClientPacket


class TourCreate(ClientPacket):
    __packet_key__ = "tour_create"


class TourRegister(ClientPacket):
    __packet_key__ = "tour_register"


class GetHallBronze(ClientPacket):
    __packet_key__ = "tour_get_hall_bronze"


class GetHallSilver(ClientPacket):
    __packet_key__ = "tour_get_hall_silver"


class GetHallGold(ClientPacket):
    __packet_key__ = "tour_get_hall_gold"
