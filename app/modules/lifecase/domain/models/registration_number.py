from dataclasses import dataclass
from datetime import datetime

from common.domain.models.entity import Entity
from common.domain.models.value_object import EntityId


class RegistrationNumberId(EntityId):
    pass


@dataclass
class RegistrationNumber(Entity):
    id: RegistrationNumberId
    number: str
    rent_timestamp: datetime
