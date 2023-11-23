from datetime import datetime, timedelta
from typing import TypeVar

from common.application.services.services import GenericService
from config import morfis_config
from config.utils import now
from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepository
from modules.registration_number.domain.value_objects import RegistrationNumberValue, CounterValue, RegistrationNumberId
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository

RepositoryType = TypeVar('RepositoryType', bound=RegistrationNumberRepository)


class RegistrationNumberService(GenericService):
    _repository: RepositoryType

    def __init__(self, repository: RepositoryType):
        self._repository = repository

    def _generate_new_number(self) -> RegistrationNumberValue:
        counter_repo = DjangoCounterRepository()
        counter = CounterService('title', repository=counter_repo)
        counter_value: CounterValue = counter.next()
        result = RegistrationNumberValue.format(counter_value)
        return result

    def get_registration_number(self) -> RegistrationNumberValue:
        registration_number = self._repository.get_expired_number()
        if registration_number is None:
            registration_number = RegistrationNumber(
                id=RegistrationNumberId.next_id(),
                number=self._generate_new_number(),
                rent_expires_at_timestamp=RegistrationNumber.calc_rent_timestamp()
            )
            self._repository.add(registration_number)

        return registration_number.number
