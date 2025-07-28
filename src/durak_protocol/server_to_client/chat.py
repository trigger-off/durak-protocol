from datetime import datetime
from typing import Literal

from . import ServerPacket, types
from pydantic import BaseModel, Field

MessageKind = Literal["image", "user", "up", "present", "asset", "coll_item", "down"]


class Message(BaseModel):
    id: int
    kind: MessageKind | None = None
    msg: str | None = None
    payload: str | None = None
    dtc: datetime
    from_: int = Field(..., alias="from")
    to: int = Field(..., alias="to")


class DeleteConversationSuccess(ServerPacket):
    __packet_key__ = "delete_conversation_success"
    friend_id: int


class ImgMsgPrice(ServerPacket):
    __packet_key__ = "img_msg_price"
    v: int


class Conversation(ServerPacket):
    __packet_key__ = "conversation"
    id: int
    begin: bool
    users: dict[str, types.UserFind]
    data: list[Message]


class UserMsg(ServerPacket):
    __packet_key__ = "user_msg"
    dtc: datetime
    id: int
    from_: int = Field(..., alias="from")
    to: int
    name: str
    avatar: str | None = None
    kind: MessageKind | None = None
    payload: str | None = None


class Image(ServerPacket):
    __packet_key__ = "img"
    id: int
    data: str | None = None


class Ban2ComplaintSuccess(ServerPacket):
    __packet_key__ = "ban2_complaint_success"
