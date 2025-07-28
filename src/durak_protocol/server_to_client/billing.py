from . import ServerPacket, types


class AndroidPurchaseIds(ServerPacket):
    __packet_key__ = "android_purchase_ids"
    ids: list[str]
    shop_ids: list[dict] | None = None


class HuaweiPurchaseIds(ServerPacket):
    __packet_key__ = "huawei_purchase_ids"
    ids: list[str]


class RustorePurchaseIds(ServerPacket):
    __packet_key__ = "rustore_purchase_ids"
    ids: list[str]


class DeveloperPayload(ServerPacket):
    __packet_key__ = "developer_payload"
    dp: str


class HuaweiDeveloperPayload(ServerPacket):
    __packet_key__ = "huawei_developer_payload"
    dp: str


class VerifyPurchaseSuccess(ServerPacket):
    __packet_key__ = "verify_purchase_success"
    order_id: str


class HuaweiVerifyPurchaseSuccess(ServerPacket):
    __packet_key__ = "huawei_verify_purchase_success"
    order_id: str


class RustoreVerifyPurchaseSuccess(ServerPacket):
    __packet_key__ = "rustore_verify_purchase_success"
    subscription_token: str


class ValidateRW(ServerPacket):
    __packet_key__ = "validate_rw"
    time: str
    count: int


class PointsPrice(ServerPacket):
    __packet_key__ = "points_price"
    ids: list[types.PointsPrice]


class PremiumPrice(ServerPacket):
    __packet_key__ = "premium_price"
    ids: list[types.PremiumPrice]


class DayBonus(ServerPacket):
    __packet_key__ = "day_bonus"
    k: int


class NotEnoughCoins(ServerPacket):
    __packet_key__ = "not_enough_coins"
    feature: str | None = None


class BuyPointsSuccess(ServerPacket):
    __packet_key__ = "buy_points_success"
