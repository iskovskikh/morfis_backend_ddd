from dataclasses import dataclass
from typing import TypeVar, Generic

from common.domain.value_objects import GenericUUID

EntityId = TypeVar("EntityId", bound=GenericUUID)


@dataclass
class Entity(Generic[EntityId]):

    @classmethod
    def next_id(cls):
        return cls.next_id()


class Aggregate(Entity[EntityId]):
    ...


class AggregateRoot(Aggregate[EntityId]):
    ...
