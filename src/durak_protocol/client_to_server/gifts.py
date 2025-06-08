from . import ClientPacket


class PresentConfirm(ClientPacket):
    __packet_key__ = "present_confirm"
    pin: str
    verify_code: str


class GetGiftAssets(ClientPacket):
    __packet_key__ = "get_gift_assets"
    id: int


class GiftAsset(ClientPacket):
    __packet_key__ = "gift_asset"
    to_id: int
    asset_id: str


class GiftCollItem(ClientPacket):
    __packet_key__ = "gift_coll_item"
    coll_id: str
    item_id: int
    to_id: int


class Present(ClientPacket):
    __packet_key__ = "present"
    id: int
    amount: int
    verify_code: str
