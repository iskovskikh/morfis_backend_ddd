from common.infarastructure.data_mapper import DataMapper
from common.infarastructure.repository import DjangoGenericRepository
from modules.lifecase.domain.models.registration_number import RegistrationNumber
from modules.lifecase.infrastructure.persistence.models.registration_number_model import RegistrationNumberModel


class RegistrationNumberDataMapper(DataMapper[RegistrationNumber, RegistrationNumberModel]):

    def model_to_entity(self, instance: RegistrationNumberModel) -> RegistrationNumber:
        return RegistrationNumber(
            id=instance.id,
            number=instance.number,
            rent_timestamp=instance.rent_timestamp
        )

    def entity_to_model(self, entity: RegistrationNumber) -> RegistrationNumberModel:
        return RegistrationNumberModel(
            id=entity.id,
            numbers=entity.number,
            rent_timestamp=entity.rent_timestamp
        )


class DjangoRegistrationNumberRepository(DjangoGenericRepository):
    mapper_class = RegistrationNumberDataMapper
    model_class = RegistrationNumber
