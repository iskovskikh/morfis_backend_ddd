from dataclasses import dataclass
from datetime import datetime

from common.domain.entity import Entity
from common.domain.value_object import EntityId


class RegistrationNumberId(EntityId):
    pass


@dataclass
class RegistrationNumber(Entity):
    id: RegistrationNumberId
    number: str
    rent_timestamp: datetime

    @staticmethod
    def factory(
            id_: RegistrationNumberId,
            number: str,
            rent_timestamp: datetime
    ) -> 'RegistrationNumber':
        registration_number = RegistrationNumber(
            id=id_,
            number=number,
            rent_timestamp=rent_timestamp
        )

        return registration_number
