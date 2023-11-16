from typing import Generic, TypeVar

from common.domain.models.entity import Entity as DomainEntity
from common.domain.models.value_object import EntityId

Entity = TypeVar('Entity', bound=DomainEntity)
# EntityIdType = TypeVar('EntityIdType', bound=GenericUUID)
EntityIdType = TypeVar('EntityIdType', bound=EntityId)


class GenericRepository(Generic[Entity, EntityIdType]):
    ...
