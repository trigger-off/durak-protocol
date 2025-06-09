from . import ClientPacket


class GetUserInfo(ClientPacket):
    __packet_key__ = "get_user_info"
    id: int


class UsersFind(ClientPacket):
    __packet_key__ = "users_find"
    name: str | None = None


class SaveNote(ClientPacket):
    __packet_key__ = "save_note"
    id: int
    color: str
    note: str


class Complaint(ClientPacket):
    __packet_key__ = "complaint"
    id: int | None = None
