from typing import Generic, TypeVar
from common.domain.models.entity import Entity as DomainEntity
from common.domain.models.value_object import GenericUUID

Entity = TypeVar('Entity', bound=DomainEntity)
EntityIdType = TypeVar('EntityIdType', bound=GenericUUID)


class GenericRepository(Generic[Entity, EntityIdType]):
    ...
