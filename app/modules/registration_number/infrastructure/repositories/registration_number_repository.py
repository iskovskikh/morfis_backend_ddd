from common.domain.exceptions import EntityNotFoundException
from common.infarastructure.data_mappers import DataMapperInterface
from common.infarastructure.repositories import DjangoGenericRepository
from config.utils import now
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepositoryInterface
from modules.registration_number.domain.value_objects import RegistrationNumberValue
from modules.registration_number.infrastructure.models.registration_number_model import RegistrationNumberModel
from django.core.exceptions import ObjectDoesNotExist


class RegistrationNumberDataMapper(DataMapperInterface[RegistrationNumber, RegistrationNumberModel]):
    def entity_to_model(self, entity):
        return RegistrationNumberModel(
            id=entity.id,
            number=str(entity.number.value),
            rent_expires_at_timestamp=entity.rent_expires_at_timestamp
        )

    def model_to_entity(self, instance):
        return RegistrationNumber(
            id=instance.id,
            number=RegistrationNumberValue(value=instance.number),
            rent_expires_at_timestamp=instance.rent_expires_at_timestamp
        )


class DjangoRegistrationNumberRepository(RegistrationNumberRepositoryInterface, DjangoGenericRepository):
    mapper_class = RegistrationNumberDataMapper
    model_class = RegistrationNumberModel

    def update(self, entity: RegistrationNumber):
        try:
            instance = self.get_model_class().objects.get(id=entity.id)
        except ObjectDoesNotExist:
            raise EntityNotFoundException
        instance.rent_expires_at_timestamp = entity.rent_expires_at_timestamp
        instance.save()

    def get_expired_number(self):
        instance = self.get_model_class().objects \
            .filter(rent_expires_at_timestamp__lt=now()) \
            .order_by('rent_expires_at_timestamp')
        if instance:
            return self.map_model_to_entity(instance.first())

        return None
