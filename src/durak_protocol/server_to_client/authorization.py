from typing import Literal

from . import ServerPacket, types


class Authorized(ServerPacket):
    __packet_key__ = "authorized"
    id: int


class SetToken(ServerPacket):
    __packet_key__ = "set_token"
    token: str


class Captcha(ServerPacket):
    __packet_key__ = "captcha"
    url: str | None | Literal["null"] = None


class GetIntegrityToken(ServerPacket):
    __packet_key__ = "get_integrity_token"
    request_hash: str
    rt: Literal["st", "cl"] | None = None


class TokenFCM(ServerPacket):
    __packet_key__ = "token"
    uid: str
    platform: str
    accept: bool


class UsersByTokens(ServerPacket):
    __packet_key__ = "users_by_tokens"
    users: dict[str, types.UserData]


class AppleSignIn(ServerPacket):
    __packet_key__ = "apple_sign_in"
    id_token: str
    name: str


class HuaweiNeedRegistration(ServerPacket):
    __packet_key__ = "huawei_need_registration"
    id_token: str
    name: str | None = None
    picture: str | None = None


class DurakGoogleNeedRegistration(ServerPacket):
    __packet_key__ = "durak_google_need_registration"
    id_token: str
    name: str | None = None
    picture: str | None = None


class VkNeedRegistration(ServerPacket):
    __packet_key__ = "vk_need_registration"
    access_token: str
    name: str | None = None
    picture: str | None = None


class Migrate(ServerPacket):
    __packet_key__ = "migrate"


class MigrateInfo(ServerPacket):
    __packet_key__ = "migrate_info"
    text: dict[str, str]
    pin: str
    url: str


class DurakSetTokenSuccess(ServerPacket):
    __packet_key__ = "durak_set_tokens_success"


class HuaweiAuthSuccess(ServerPacket):
    __packet_key__ = "huawei_auth_success"


class DurakGoogleAuthSuccess(ServerPacket):
    __packet_key__ = "durak_google_auth_success"


class DurakGoogleRegisterSuccess(ServerPacket):
    __packet_key__ = "durak_google_register_success"


class VkAuthSuccess(ServerPacket):
    __packet_key__ = "vk_auth_success"


class AppleSignInSuccess(ServerPacket):
    __packet_key__ = "apple_sign_in_success"
