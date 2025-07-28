from . import ServerPacket, types
from ..shared.types import ASSET_GROUP_TYPE


class Achieves(ServerPacket):
    __packet_key__ = "achieves"
    items: list[types.Achieve]


class Collection(ServerPacket):
    __packet_key__ = "coll"
    smile_bear: types.CollectionAsset | None = None
    smile_gnome: types.CollectionAsset | None = None
    smile_lion: types.CollectionAsset | None = None
    smile_robot: types.CollectionAsset | None = None
    smile_unicorn: types.CollectionAsset | None = None
    smile_vampire: types.CollectionAsset | None = None
    smile_boar: types.CollectionAsset | None = None
    smile_bull: types.CollectionAsset | None = None
    smile_dog: types.CollectionAsset | None = None
    smile_dragon: types.CollectionAsset | None = None
    smile_goat: types.CollectionAsset | None = None
    smile_horse: types.CollectionAsset | None = None
    smile_monkey: types.CollectionAsset | None = None
    smile_rabbit: types.CollectionAsset | None = None
    smile_rat: types.CollectionAsset | None = None
    smile_rooster: types.CollectionAsset | None = None
    smile_snake: types.CollectionAsset | None = None
    smile_tiger: types.CollectionAsset | None = None
    shirt_rstyle: types.CollectionAsset | None = None
    shirt_bicycle: types.CollectionAsset | None = None


class UserCollection(Collection):
    __packet_key__ = "user_coll"


class Assets(ServerPacket):
    __packet_key__ = "assets"
    smile: list[types.Asset]
    shirt: list[types.Asset]
    frame: list[types.Asset]


class GiveAsset(ServerPacket):
    __packet_key__ = "give_asset"
    id: str
    name: dict[str, str]


class GiveAchieve(ServerPacket):
    __packet_key__ = "give_achieve"
    id: str
    name: dict[str, str]


class GiveCollItem(ServerPacket):
    __packet_key__ = "give_coll_item"
    coll_id: str
    item_id: int
    group: ASSET_GROUP_TYPE
