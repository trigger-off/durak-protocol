from ..base import *


class ClientPacket(BasePacket):
    __direction__ = Direction.CLIENT_TO_SERVER

    @classmethod
    def deserialize(
        cls, data: bytes, direction: Direction = Direction.CLIENT_TO_SERVER
    ) -> Self:
        return BasePacket.deserialize(data=data, direction=direction)
