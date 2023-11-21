from typing import Generic

from common.infarastructure.data_mapper import DataMapper
from common.infarastructure.repository import DjangoGenericRepository
from config.utils import now
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepository
from modules.registration_number.domain.value_objects import RegistrationNumberValue
from modules.registration_number.infrastructure.models.registration_number_model import RegistrationNumberModel


class RegistrationNumberDataMapper(DataMapper[RegistrationNumber, RegistrationNumberModel]):
    def entity_to_model(self, entity):
        return RegistrationNumberModel(
            id=entity.id,
            number=str(entity.number.number),
            rent_expires_at_timestamp=entity.rent_expires_at_timestamp
        )

    def model_to_entity(self, instance):
        return RegistrationNumber(
            id=instance.id,
            number=RegistrationNumberValue(number=instance.number),
            rent_expires_at_timestamp=instance.rent_expires_at_timestamp
        )


class DjangoRegistrationNumberRepository(RegistrationNumberRepository, DjangoGenericRepository):
    mapper_class = RegistrationNumberDataMapper
    model_class = RegistrationNumberModel

    def get_expired_number(self) -> RegistrationNumber | None:
        instance = self.get_model_class().objects \
            .filter(rent_expires_at_timestamp__lt=now()) \
            .order_by('-rent_expires_at_timestamp') \
            .first()

        if instance:
            return self.map_model_to_entity(instance)

        return None
