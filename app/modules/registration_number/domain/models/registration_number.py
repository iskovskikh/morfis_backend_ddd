from dataclasses import dataclass

from common.domain.models.entity import AggregateRoot
from common.domain.models.value_object import EntityId


class RegistrationNumberId(EntityId):
    pass


@dataclass
class RegistrationNumber(AggregateRoot):
    id: RegistrationNumberId
    number: str
