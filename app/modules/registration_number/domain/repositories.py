from abc import ABC, abstractmethod

from common.domain.repository import GenericRepository
from modules.registration_number.domain.entities import CounterId, Counter


class CounterRepository(GenericRepository[CounterId, Counter], ABC):
    """RegistrationNumberRepository iface"""

    @abstractmethod
    def get_or_create_by_title(self, title: str) -> Counter:
        raise NotImplementedError

# class RegistrationNumberRepository(GenericRepository[EntityId, Entity], ABC):
#     """RegistrationNumberRepository iface"""
