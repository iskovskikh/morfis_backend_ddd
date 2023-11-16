from common.infarastructure.persistance.repository import Repository
from modules.lifecase.domain.models.registration_number import RegistrationNumber
from modules.lifecase.infrastructure.persistance.models.registration_number_model import RegistrationNumberModel


class RegistrationNumberRepositiry(Repository):

    def create(
            self,
            registration_number: RegistrationNumber
    ) -> RegistrationNumberModel:
        ...

    def update(
            self,
            registration_number: RegistrationNumber,
            registration_number_model: RegistrationNumberModel
    ) -> RegistrationNumberModel:
        ...

    def delete(self,
               registration_number_model: RegistrationNumberModel
               ) -> None:
        registration_number_model.delete()

    def get_expired_number(self) -> RegistrationNumberModel:
        ...
