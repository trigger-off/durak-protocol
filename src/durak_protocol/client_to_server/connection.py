from . import ClientPacket, Field
from typing import Literal
from datetime import datetime


class DeviceCPacket(ClientPacket):
    __packet_key__ = "c"
    pl: Literal["android", "rustore", "huawei", "ios", "ipad"]
    p: int
    t: datetime | None = None
    n: Literal["durak.android", "durak.rustore", "durak.huawei", "durak.ios"]
    v: str
    l: str
    d: str | None = None
    tz: str
    and_: int | None = Field(None, alias="and")
    ios: str | None = None


class Sign(ClientPacket):
    __packet_key__ = "sign"
    hash: str


class SendUserMsgCode(ClientPacket):
    __packet_key__ = "send_user_msg_code"
    code: str
    msg: str


class GetServer(ClientPacket):
    __packet_key__ = "get_server"
