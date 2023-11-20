from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Type

from common.domain.entity import Entity
from common.domain.value_object import EntityId

EntityType = TypeVar('EntityType', bound=Entity)
EntityIdType = TypeVar('EntityIdType', bound=EntityId)


class GenericRepository(Generic[EntityIdType, EntityType], metaclass=ABCMeta):

    @abstractmethod
    def add(self, entity: EntityType):
        raise NotImplementedError()

    @abstractmethod
    def remove(self, entity: EntityType):
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: EntityType):
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, entity_id: EntityIdType) -> EntityType:
        raise NotImplementedError()

    @staticmethod
    def next_id() -> EntityIdType:
        return EntityId.next_id()
