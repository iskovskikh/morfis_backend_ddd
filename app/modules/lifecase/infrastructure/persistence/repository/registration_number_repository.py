from django.db.models.query import Q

from common.infarastructure.persistence.repository import Repository
from config import utils
from modules.lifecase.domain.models.registration_number import RegistrationNumber
from modules.lifecase.infrastructure.persistence.models.registration_number_model import RegistrationNumberModel




class RegistrationNumberRepository(Repository):

    def create(
            self,
            registration_number: RegistrationNumber
    ) -> RegistrationNumberModel:
        registration_number_model = RegistrationNumberModel.from_domain(registration_number)
        registration_number_model.save(force_insert=True)
        return registration_number_model

    def update_rent_timestamp(
            self,
            registration_number: RegistrationNumber,
            registration_number_model: RegistrationNumberModel
    ) -> RegistrationNumberModel:
        registration_number_model.rent_timestamp = registration_number.rent_timestamp
        registration_number_model.save()
        return registration_number_model

    def delete(self,
               registration_number_model: RegistrationNumberModel
               ) -> None:
        registration_number_model.delete()

    def get_expired_number(self) -> RegistrationNumberModel | None:
        expired_query = Q(rent_timestamp__gt=cli.now())
        registration_number_model = RegistrationNumberModel.objects.filter(expired_query).order_by('rent_timestamp')
        return registration_number_model
