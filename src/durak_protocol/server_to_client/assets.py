from . import ServerPacket, types
from ..shared.types import ASSET_GROUP_TYPE


class Achieves(ServerPacket):
    __packet_key__ = "achieves"
    items: list[types.Achieve]


class Collection(ServerPacket):
    __packet_key__ = "coll"
    smile_bear: types.CollectionAsset
    smile_gnome: types.CollectionAsset
    smile_lion: types.CollectionAsset
    smile_robot: types.CollectionAsset
    smile_unicorn: types.CollectionAsset
    smile_vampire: types.CollectionAsset
    smile_boar: types.CollectionAsset
    smile_bull: types.CollectionAsset
    smile_dog: types.CollectionAsset
    smile_dragon: types.CollectionAsset
    smile_goat: types.CollectionAsset
    smile_horse: types.CollectionAsset
    smile_monkey: types.CollectionAsset
    smile_rabbit: types.CollectionAsset
    smile_rat: types.CollectionAsset
    smile_rooster: types.CollectionAsset
    smile_snake: types.CollectionAsset
    smile_tiger: types.CollectionAsset
    shirt_rstyle: types.CollectionAsset
    shirt_bicycle: types.CollectionAsset


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
