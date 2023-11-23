from datetime import datetime, timedelta
from typing import TypeVar

from common.application.services.services import Service
from config import morfis_config
from config.utils import now
from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepository
from modules.registration_number.domain.value_objects import RegistrationNumberValue
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository
from modules.registration_number.infrastructure.repositories.registration_number_repository import \
    DjangoRegistrationNumberRepository

RepositoryType = TypeVar('RepositoryType', bound=RegistrationNumberRepository)


class RegistrationNumberService(Service):
    registration_number_repo: RegistrationNumberRepository = DjangoRegistrationNumberRepository()
    counter_service: CounterService = CounterService(title='lifecase_counter', repository=DjangoCounterRepository())

    def get_registration_number(self) -> RegistrationNumber:
        registration_number = self.registration_number_repo.get_expired_number()
        if registration_number is None:
            registration_number = RegistrationNumber.factory(self.counter_service.next())
            self.registration_number_repo.add(registration_number)
        else:
            registration_number.rent_expires_at_timestamp = RegistrationNumber.calc_rent_timestamp()
            self.registration_number_repo.update(registration_number)

        return registration_number

    def extend_registration_number(self):
        ...

    def invalidate_registration_number(self):
        ...

    def register_new_lifecase_with_this_number(self):
        ...
