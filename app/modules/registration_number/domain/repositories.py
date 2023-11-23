from abc import ABC, abstractmethod

from common.domain.repositories import GenericRepository
from modules.registration_number.domain.entities import Counter, RegistrationNumber
from modules.registration_number.domain.value_objects import CounterId, RegistrationNumberId


class CounterRepositoryInterface(GenericRepository[CounterId, Counter], ABC):
    """RegistrationNumberRepository iface"""

    @abstractmethod
    def get_or_create_by_title(self, title: str) -> Counter:
        raise NotImplementedError


class RegistrationNumberRepositoryInterface(GenericRepository[RegistrationNumberId, RegistrationNumber], ABC):
    """RegistrationNumberRepository iface"""

    def get_expired_number(self) -> RegistrationNumber | None:
        raise NotImplementedError

    def update(self, entity: RegistrationNumber) -> None:
        raise NotImplementedError
