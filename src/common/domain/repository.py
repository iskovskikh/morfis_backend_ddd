from typing import Generic, TypeVar
from common.domain.entity import Entity as DomainEntity
from common.domain.value_objects import GenericUUID

Entity = TypeVar('Entity', bound=DomainEntity)
EntityId = TypeVar('EntityId', bound=GenericUUID)


class GenericRepository(Generic[Entity, EntityId]):
    ...
