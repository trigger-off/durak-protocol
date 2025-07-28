from datetime import datetime
from typing import Literal
from ..shared.types import ASSET_GROUP_TYPE
from pydantic import BaseModel, Field


class UserData(BaseModel):
    name: str
    avatar: str | None = None
    rid: str
    news: bool
    pw: int
    friends_count: int
    new_msg: bool
    assets: list[int]
    assel: list[int]
    frame: str | None = None
    smile: str | None = None
    shirt: str | None = None
    ach: list[int]
    achc: int
    achsel: list[int]
    achieve: str | None = None
    t_tour_stage: int
    t_player_status: int
    t_bronze: int
    t_silver: int
    t_gold: int
    coins: int
    wins: int
    wins_s: int | None = None
    points_win: int
    points_win_s: int | None = None
    points: int
    score: int
    score_s: int | None = None
    dtp: datetime
    dtfp: datetime


class UserFind(BaseModel):
    id: int
    name: str
    score: int
    dtp: datetime
    avatar: str | None = None
    frame: str | None = None
    achieve: str | None = None
    pw: int


class LeaderboardUser(UserFind):
    id: int = Field(..., alias="user_id")
    count: int
    place: int


class HallUser(UserFind):
    count: int


class HallItem(BaseModel):
    place: int
    user: HallUser


class TournamentParams(BaseModel):
    sw: bool
    deck: int
    players: int
    fast: bool
    ch: bool
    nb: bool


class TournamentData(BaseModel):
    name: dict[str, str]
    description: dict[str, str]
    dta: datetime
    dts: datetime
    dtf: datetime
    price: int
    reward: dict[Literal["bronze", "silver", "gold"], int]
    params: TournamentParams
    start_stage: int
    wins_count: int
    server_id: str


class Game(BaseModel):
    id: int
    p: int
    cp: int
    pr: bool
    name: str
    bet: int
    pc: int
    deck: int
    nb: bool
    dr: bool
    sw: bool
    ch: bool
    fast: bool


class Achieve(BaseModel):
    id: int
    index: int
    mask: int
    level: int
    name: dict[str, str]
    desc: dict[str, str] | None = None


class Asset(BaseModel):
    id: int
    index: int
    mask: int
    level: int
    price: int | None = None
    name: dict[str, str]
    desc: dict[str, str] | None = None
    hidden: bool
    group: ASSET_GROUP_TYPE


class CollectionAsset(BaseModel):
    group: ASSET_GROUP_TYPE
    items: dict[str, int]


class PointsPrice(BaseModel):
    price: int
    quantity: int
    id: str


class PremiumPrice(BaseModel):
    price: int
    quantity: int
    id: str


class Shirt(BaseModel):
    id: str
    lvl: int