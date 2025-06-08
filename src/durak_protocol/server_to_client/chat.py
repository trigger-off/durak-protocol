from . import ServerPacket


class DeleteConversationSuccess(ServerPacket):
    __packet_key__ = "delete_conversation_success"
    friend_id: int


class ImgMsgPrice(ServerPacket):
    __packet_key__ = "img_msg_price"
    v: int
