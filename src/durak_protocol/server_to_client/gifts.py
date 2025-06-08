from . import ServerPacket, types


class GiftAssets(ServerPacket):
    __packet_key__ = "gift_assets"
    smile: None | list[types.Asset] = None
    shirt: None | list[types.Asset] = None
    frame: None | list[types.Asset] = None


# user_coll
class UserCollection(ServerPacket):
    __packet_key__ = "user_coll"


class GiftCollItemSuccess(ServerPacket):
    __packet_key__ = "gift_coll_item_success"


class GiftAssetSuccess(ServerPacket):
    __packet_key__ = "gift_asset_success"


class PresentConfirm(ServerPacket):
    __packet_key__ = "present_confirm"
