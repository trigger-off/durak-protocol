from . import ClientPacket


class DurakGoogleAuth(ClientPacket):
    __packet_key__ = "durak_google_auth"
    id_token: str


class HuaweiAuth(ClientPacket):
    __packet_key__ = "huawei_auth"
    id_token: str


class VkAuth(ClientPacket):
    __packet_key__ = "vk_auth"
    access_token: str


class AppleSignIn(ClientPacket):
    __packet_key__ = "apple_sign_in"
    id_token: str
    name: str


class DeviceCheck(ClientPacket):
    __packet_key__ = "device_check"
    token: str


class AppleSetTokens(ClientPacket):
    __packet_key__ = "apple_set_tokens"
    id_token: str
    tokens: str


class AppleRegistration(ClientPacket):
    __packet_key__ = "register"
    name: str
    captcha: str | None = None


class AppleRegisterConfirm(ClientPacket):
    __packet_key__ = "register_confirm"
    register_code: str


class HuaweiRegistration(ClientPacket):
    __packet_key__ = "huawei_register"
    id_token: str
    gavatar: bool
    captcha: str | None = None
    name: str


class DurakGoogleRegister(ClientPacket):
    __packet_key__ = "durak_google_register"
    id_token: str
    gavatar: bool
    captcha: str | None = None
    name: str


class VkRegister(ClientPacket):
    __packet_key__ = "vk_register"
    access_token: str
    gavatar: bool
    captcha: str | None = None
    name: str


class Auth(ClientPacket):
    __packet_key__ = "auth"
    token: str


class TokenFCM(ClientPacket):
    __packet_key__ = "token"
    uid: str
    platform: str


class MigrateTokens(ClientPacket):
    __packet_key__ = "migrate_tokens"
    tokens: list[str]


class PlayIntegrity(ClientPacket):
    __packet_key__ = "play_integrity"
    it: str


class GetCaptcha(ClientPacket):
    __packet_key__ = "get_captcha"
