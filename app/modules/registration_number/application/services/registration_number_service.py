from datetime import datetime, timedelta
from typing import TypeVar

from common.application.services.service import GenericService
from config import morfis_config
from config.utils import now
from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.domain.entities import RegistrationNumber, RegistrationNumberId
from modules.registration_number.domain.repositories import RegistrationNumberRepository
from modules.registration_number.domain.value_objects import RegistrationNumberValue, CounterValue
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository

RepositoryType = TypeVar('RepositoryType', bound=RegistrationNumberRepository)


class RegistrationNumberService(GenericService):
    _repository: RepositoryType
    _template: str = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_TEMPLATE']
    _lifetime: timedelta = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_LIFETIME']

    def __init__(self, repository: RepositoryType):
        self._repository = repository

    def _format_number(self, counter_value: CounterValue) -> str:
        number = self._template.format(
            current_no=counter_value.current_no,
            yearly_current_no=counter_value.yearly_current_no,
            day=counter_value.day,
            month=counter_value.month,
            year=counter_value.year,
            day_of_week=counter_value.day_of_week,
            week_no=counter_value.week_no,
        )

        return number

    def _generate_new_number(self) -> RegistrationNumberValue:
        counter_repo = DjangoCounterRepository()
        counter = CounterService('title', repository=counter_repo)
        counter_value: CounterValue = counter.next()
        result = self._format_number(counter_value)
        return RegistrationNumberValue(result)

    @staticmethod
    def _calc_rent_timestamp() -> datetime:
        return now() + RegistrationNumberService._lifetime

    def get_registration_number(self) -> RegistrationNumberValue:
        registration_number = self._repository.get_expired_number()
        if registration_number is None:
            registration_number = RegistrationNumber(
                id=RegistrationNumberId.next_id(),
                number=self._generate_new_number(),
                rent_expires_at_timestamp=RegistrationNumberService._calc_rent_timestamp()
            )
            self._repository.add(registration_number)

        return registration_number.number
