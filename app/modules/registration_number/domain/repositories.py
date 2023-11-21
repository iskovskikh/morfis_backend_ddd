from abc import ABC, abstractmethod

from common.domain.repository import GenericRepository
from modules.registration_number.domain.entities import CounterId, Counter, RegistrationNumber, RegistrationNumberId


class CounterRepository(GenericRepository[CounterId, Counter], ABC):
    """RegistrationNumberRepository iface"""

    @abstractmethod
    def get_or_create_by_title(self, title: str) -> Counter:
        raise NotImplementedError


class RegistrationNumberRepository(GenericRepository[RegistrationNumberId, RegistrationNumber], ABC):
    """RegistrationNumberRepository iface"""

    def get_expired_number(self) -> RegistrationNumber | None:
        raise NotImplementedError
