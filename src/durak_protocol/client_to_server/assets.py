from . import ClientPacket


class GetAchieves(ClientPacket):
    __packet_key__ = "get_achieves"


class GetAssets(ClientPacket):
    __packet_key__ = "get_assets"


class GetUserColl(ClientPacket):
    __packet_key__ = "get_user_coll"


class AssetSelect(ClientPacket):
    __packet_key__ = "asset_select"
    id: str


class AchieveSelect(ClientPacket):
    __packet_key__ = "achieve_select"
    id: str
