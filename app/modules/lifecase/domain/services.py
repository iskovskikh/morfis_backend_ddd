from abc import ABC

from modules.lifecase.domain.entities import LifeCase
from modules.lifecase.domain.repositories import LifeCaseRepositoryInterface
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepositoryInterface
from modules.registration_number.domain.services import RegistrationNumberServiceInterface
from modules.registration_number.domain.value_objects import RegistrationNumberId


class LifeCaseServiceInterface(ABC):
    lifecase_repo: LifeCaseRepositoryInterface
    registration_number_repo: RegistrationNumberRepositoryInterface
    registration_number_service: RegistrationNumberServiceInterface

    def create_new_lifecase(
            self,
            registration_number_id: RegistrationNumberId,
            validated_data: dict
    ):
        registration_number = self.registration_number_repo.get_by_id(entity_id=registration_number_id)

        lifecase = LifeCase.factory(
            registration_number=registration_number.number,
            # ...
            cito=validated_data['cito'],
        )
        self.lifecase_repo.add(lifecase)

        # todo: переделать на события
        self.registration_number_service.register_new_lifecase_with_this_registration_number(registration_number)

    def query_lifecases(
            self,
            specification
    ) -> list[RegistrationNumber]:


        return []
