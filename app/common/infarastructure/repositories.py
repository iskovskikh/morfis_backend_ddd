from dataclasses import asdict
from typing import Any, TypeVar, Generic

from common.domain.entities import Entity
from common.domain.exceptions import EntityNotFoundException
from common.domain.repositories import GenericRepository
from common.domain.value_objects import EntityId
from common.infarastructure.data_mappers import DataMapper
from common.infarastructure.models import BaseModel
from django.core.exceptions import ObjectDoesNotExist


EntityType = TypeVar('EntityType', bound=Entity)
EntityIdType = TypeVar('EntityIdType', bound=EntityId)
ModelClassType = TypeVar('ModelClassType', bound=BaseModel)


class InMemoryRepository(GenericRepository[EntityIdType, EntityType]):

    def __init__(self) -> None:
        self.objects: dict[Any, Any] = {}

    def get_by_id(self, entity_id: EntityIdType) -> EntityType:
        try:
            return self.objects[entity_id]
        except KeyError:
            raise EntityNotFoundException(repository=self, entity_id=entity_id)

    def remove_by_id(self, entity_id: EntityIdType):
        try:
            del self.objects[entity_id]
        except KeyError:
            raise EntityNotFoundException(repository=self, entity_id=entity_id)

    def add(self, entity: EntityType):
        assert issubclass(entity.__class__, Entity)
        self.objects[entity.id] = entity

    def remove(self, entity: EntityType):
        del self.objects[entity.id]

    def count(self):
        return len(self.objects)


class DjangoGenericRepository(GenericRepository[EntityId, Entity], Generic[ModelClassType]):
    mapper_class: type[DataMapper[Entity, ModelClassType]]
    model_class: type[ModelClassType]

    def add(self, entity: Entity):
        instance = self.map_entity_to_model(entity)
        instance.save(force_insert=True)

    def remove(self, entity: Entity):
        instance = self.get_model_class().objects.get(id=entity.id)
        instance.delete()

    def update(self, entity: EntityType):
        try:
            instance = self.get_model_class().objects.get(id=entity.id)
        except ObjectDoesNotExist:
            raise EntityNotFoundException
        for key, value in asdict(entity).items():
            setattr(instance, key, value)
        instance.save()

    def get_by_id(self, entity_id: EntityIdType) -> EntityType:
        try:
            instance = self.get_model_class().objects.get(id=entity_id)
        except ObjectDoesNotExist:
            raise EntityNotFoundException

        return self.map_model_to_entity(instance)

    @property
    def data_mapper(self):
        return self.mapper_class()

    def map_entity_to_model(self, entity: EntityType):
        assert self.mapper_class, (
            f"No data_mapper attribute in {self.__class__.__name__}. "
            "Make sure to include `mapper_class = MyDataMapper` in the Repository class."
        )

        return self.data_mapper.entity_to_model(entity)

    def map_model_to_entity(self, instance) -> EntityType:
        assert self.data_mapper
        return self.data_mapper.model_to_entity(instance)

    def get_model_class(self):
        assert self.model_class is not None, (
            f"No model_class attribute in in {self.__class__.__name__}. "
            "Make sure to include `model_class = MyModel` in the class."
        )
        return self.model_class
