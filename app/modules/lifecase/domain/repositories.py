from abc import ABC

from common.domain.entity import Entity
from common.domain.repository import GenericRepository
from common.domain.value_object import EntityId


class CounterRepository(GenericRepository[EntityId, Entity], ABC):
    """RegistrationNumberRepository iface"""

class RegistrationNumberRepository(GenericRepository[EntityId, Entity], ABC):
    """RegistrationNumberRepository iface"""

