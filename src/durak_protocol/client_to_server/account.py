from . import ClientPacket


class GetUsersByTokens(ClientPacket):
    __packet_key__ = "get_users_by_tokens"
    tokens: list[str]


class RecoverAccount(ClientPacket):
    __packet_key__ = "remove_deletion"
    token: str


class DeleteAccount(ClientPacket):
    __packet_key__ = "delete_account"
    token: str


class UpdateAvatar(ClientPacket):
    __packet_key__ = "update_avatar"
    base64: str


class UpdateName(ClientPacket):
    __packet_key__ = "update_name"
    value: str | None = None


class GetDeleteNotice(ClientPacket):
    __packet_key__ = "get_delete_notice"


class NewsReaded(ClientPacket):
    __packet_key__ = "news_readed"


class ProfileErase(ClientPacket):
    __packet_key__ = "profile_erase"
