from . import ClientPacket


class FriendRequest(ClientPacket):
    __packet_key__ = "friend_request"
    id: int | None = None


class FriendAccept(ClientPacket):
    __packet_key__ = "friend_accept"
    id: int | None = None


class FriendDecline(ClientPacket):
    __packet_key__ = "friend_decline"
    id: int | None = None


class FriendIgnore(ClientPacket):
    __packet_key__ = "friend_ignore"
    id: int | None = None


class FriendDeletion(ClientPacket):
    __packet_key__ = "friend_delete"
    id: int | None = None


class FriendList(ClientPacket):
    __packet_key__ = "friend_list"
