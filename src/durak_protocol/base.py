from enum import Enum, auto
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from typing import ClassVar, Type, TypeVar, Unpack
from typing import Self


class Direction(Enum):
    CLIENT_TO_SERVER = auto()
    SERVER_TO_CLIENT = auto()


T = TypeVar("T", bound="BasePacket")


class BasePacket(BaseModel):
    TERMINATOR: ClassVar[str] = "\n"
    __packet_registry__: ClassVar[dict[tuple[str, Direction], Type["BasePacket"]]] = {}
    __packet_key__: ClassVar[str]
    __direction__: ClassVar[Direction]

    model_config = ConfigDict(extra="forbid", validate_by_name=True)  # Запрещаем лишние поля

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)
        if hasattr(cls, "__packet_key__") and hasattr(cls, "__direction__"):
            key = (cls.__packet_key__, cls.__direction__)
            if key in cls.__packet_registry__:
                raise ValueError(f"Packet {key} already registered")
            cls.__packet_registry__[key] = cls

    @classmethod
    def get_packet_key(cls) -> str:
        return cls.__packet_key__

    @classmethod
    def _find_packet_class(cls, key: str, direction: Direction) -> Type["BasePacket"]:
        try:
            return cls.__packet_registry__[(key, direction)]
        except KeyError:
            raise ValueError(f"Unknown packet type: {(key, direction)}") from None

    def to_text(self) -> str:
        if self.model_fields:
            json_data = self.model_dump_json(exclude_none=True, by_alias=True)
            return f"{self.get_packet_key()}{json_data}"
        return f"{self.get_packet_key()}"

    def serialize(self) -> bytes:
        return f"{self.to_text()}{self.TERMINATOR}".encode()

    @classmethod
    def deserialize(cls, data: bytes, direction: Direction) -> Self:
        try:
            decoded = data.decode().strip()
            if not decoded:
                raise ValueError("Empty packet data")

            # Разделяем ключ и данные
            if "{" in decoded:
                key, json_str = decoded.split("{", 1)
                json_str = "{" + json_str
            else:
                key, json_str = decoded, None

            packet_class = cls._find_packet_class(key, direction)

            if json_str is not None:
                # Для классов без полей разрешаем только пустой JSON
                if not packet_class.model_fields and json_str != "{}":
                    raise ValueError("Unexpected data for empty packet")
                return packet_class.model_validate_json(json_str)

            # Если данных нет, проверяем что пакет не ожидает данных
            if packet_class.model_fields:
                raise ValueError(f"Packet {key} requires data but none provided")
            return packet_class()

        except (ValueError, ValidationError) as e:
            raise ValueError(f"Invalid packet format: {e}") from e
