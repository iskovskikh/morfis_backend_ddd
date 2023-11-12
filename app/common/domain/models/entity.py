from dataclasses import dataclass
from typing import TypeVar, Generic

from common.domain.models.value_object import GenericUUID

EntityIdType = TypeVar("EntityIdType", bound=GenericUUID)


@dataclass
class Entity(Generic[EntityIdType]):
    @classmethod
    def next_id(cls) -> EntityIdType:
        return cls.next_id()


@dataclass(kw_only=True)
class AggregateRoot(Entity[EntityIdType]):
    # events: list = field(default_factory=list)
    ...
