from abc import ABC

from common.application.services.services import Service
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.repositories import RegistrationNumberRepositoryInterface


from typing import TypeVar

from modules.registration_number.domain.entities import Counter
from modules.registration_number.domain.repositories import CounterRepositoryInterface
from modules.registration_number.domain.value_objects import CounterValue

RepositoryType = TypeVar('RepositoryType', bound=CounterRepositoryInterface)


class CounterServiceInterface(Service, ABC):
    title: str
    repository: RepositoryType

    def current(self) -> CounterValue:
        counter: Counter = self.repository.get_or_create_by_title(self.title)
        return counter.current_value()

    def next(self) -> CounterValue:
        counter: Counter = self.repository.get_or_create_by_title(self.title)
        counter.next()
        self.repository.update(counter)
        return counter.current_value()

    def set_current_no(self, title):
        ...

    def set_yearly_current_no(self, title):
        ...


class RegistrationNumberServiceInterface(Service, ABC):
    registration_number_repo: RegistrationNumberRepositoryInterface
    counter_service: CounterServiceInterface

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
