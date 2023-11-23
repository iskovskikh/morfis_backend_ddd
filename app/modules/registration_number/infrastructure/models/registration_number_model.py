from django.db import models

from common.infarastructure.models import BaseModel


class RegistrationNumberModel(BaseModel):
    number = models.CharField(
        max_length=255,
        verbose_name="Номер"
    )

    rent_expires_at_timestamp = models.DateTimeField(
        verbose_name='Время аренды номера'
    )
