from . import ClientPacket


class ImgMsg(ClientPacket):
    __packet_key__ = "img_msg"
    id: int
    payload: str


class GetConversation(ClientPacket):
    __packet_key__ = "get_conversation"
    id: int
    msg_id: int | None = None


class MsgReaded(ClientPacket):
    __packet_key__ = "msg_readed"
    id: int | None = None


class DeleteConversation(ClientPacket):
    __packet_key__ = "delete_conversation"
    friend_id: int


class BanToComplaint(ClientPacket):
    __packet_key__ = "ban2_complaint"
    id: int


class GetImg(ClientPacket):
    __packet_key__ = "get_img"
    id: str


class DeleteMsg(ClientPacket):
    __packet_key__ = "delete_msg"
    msg_id: int


class SendUserMsg(ClientPacket):
    __packet_key__ = "send_user_msg"
    to: int | None = None
    msg: str | None = None
