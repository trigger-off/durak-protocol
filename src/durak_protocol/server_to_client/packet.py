from ..base import *


class ServerPacket(BasePacket):
    __direction__ = Direction.SERVER_TO_CLIENT

    @classmethod
    def deserialize(cls, data: bytes, direction: Direction = Direction.SERVER_TO_CLIENT) -> Self:
        return BasePacket.deserialize(data=data, direction=direction)
