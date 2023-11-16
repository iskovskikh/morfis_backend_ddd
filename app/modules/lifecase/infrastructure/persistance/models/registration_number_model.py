from django.db import models

from common.domain.repository import Entity
from modules.lifecase.domain.models.registration_number import RegistrationNumber, RegistrationNumberId


class RegistrationNumberModel(Entity):

    number = models.CharField(
        max_length=64,
        verbose_name='Регистрационный номер'
    )

    rent_timestamp = models.DateTimeField(verbose_name='Дата аренды')

    def to_domain(self) -> RegistrationNumber:
        return RegistrationNumber(
            id=RegistrationNumberId.next_id(),
            number=self.number,
            rent_timestamp=self.rent_timestamp
        )

    @staticmethod
    def from_domain(registration_number: RegistrationNumber) -> 'RegistrationNumberModel':
        return RegistrationNumberModel(
            id=registration_number.id,
            numbers=registration_number.number,
            rent_timestamp=registration_number.rent_timestamp
        )
