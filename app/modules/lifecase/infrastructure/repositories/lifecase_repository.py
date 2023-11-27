from common.infarastructure.data_mappers import DataMapperInterface
from common.infarastructure.repositories import DjangoGenericRepository
from modules.lifecase.domain.entities import LifeCase
from modules.lifecase.domain.repositories import LifeCaseRepositoryInterface
from modules.lifecase.infrastructure.models.lifecase_model import LifeCaseModel
from modules.registration_number.domain.value_objects import RegistrationNumberValue


class LifeCaseDataMapper(DataMapperInterface[LifeCase, LifeCaseModel]):

    def entity_to_model(self, entity: LifeCase) -> LifeCaseModel:
        return LifeCaseModel(
            id=entity.id,
            registration_number=entity.registration_number,
            cito=entity.cito
        )

    def model_to_entity(self, instance: LifeCaseModel) -> LifeCase:
        return LifeCase(
            id=instance.id,
            registration_number=RegistrationNumberValue(instance.registration_number),
            cito=instance.cito
        )


class DjangoLifeCaseRepository(LifeCaseRepositoryInterface, DjangoGenericRepository):
    mapper_class = LifeCaseDataMapper
    model_class = LifeCaseModel
