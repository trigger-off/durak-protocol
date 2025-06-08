from . import ClientPacket


class VerifyPurchase(ClientPacket):
    __packet_key__ = "verify_purchase"
    purchase_data: str
    signature: str


class HuaweiVerifyPurchase(ClientPacket):
    __packet_key__ = "huawei_verify_purchase"
    purchase_data: str
    signature: str


class RustoreVerifyPurchase(ClientPacket):
    __packet_key__ = "rustore_verify_purchase"
    subscription_token: str


class FreePointsConfirm(ClientPacket):
    __packet_key__ = "free_points_confirm"
    free_points_code: str


class BuyPoints(ClientPacket):
    __packet_key__ = "buy_points"
    id: str


class BuyPremium(ClientPacket):
    __packet_key__ = "buy_prem"
    id: str


class BuyAsset(ClientPacket):
    __packet_key__ = "buy_asset"
    id: str


class GetHuaweiDeveloperPayload(ClientPacket):
    __packet_key__ = "get_huawei_developer_payload"


class GetAndroidPurchaseIds(ClientPacket):
    __packet_key__ = "get_android_purchase_ids"


class GetHuaweiPurchaseIds(ClientPacket):
    __packet_key__ = "get_huawei_purchase_ids"


class GetRustorePurchaseIds(ClientPacket):
    __packet_key__ = "get_rustore_purchase_ids"


class GetPointsPrice(ClientPacket):
    __packet_key__ = "get_point_price"


class GetValidateRW(ClientPacket):
    __packet_key__ = "get_validate_rw"


class GetPremiumPrice(ClientPacket):
    __packet_key__ = "get_prem_price"
