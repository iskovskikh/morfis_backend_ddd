from django.db import models

from common.domain.repository import Entity
from common.infarastructure.persistence.model import BaseModel
from modules.lifecase.domain.models.registration_number import RegistrationNumber, RegistrationNumberId


class RegistrationNumberModel(BaseModel):

    number = models.CharField(
        max_length=64,
        verbose_name='Регистрационный номер'
    )

    rent_timestamp = models.DateTimeField(verbose_name='Дата аренды')

