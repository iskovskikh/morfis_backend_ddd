from dataclasses import dataclass, field
from typing import TypeVar, Generic

from common.domain.value_object import EntityId

EntityIdType = TypeVar("EntityIdType", bound=EntityId)


@dataclass
class Entity(Generic[EntityIdType]):
    id: EntityIdType = field(hash=True)

    @classmethod
    def next_id(cls) -> EntityIdType:
        return cls.next_id()


@dataclass(kw_only=True)
class AggregateRoot(Entity[EntityIdType]):
    # events: list = field(default_factory=list)
    pass
