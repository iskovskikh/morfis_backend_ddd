from django.db import models

from common.infarastructure.models import BaseModel


class LifeCaseModel(BaseModel):
    registration_number = models.CharField(
        max_length=64,
        verbose_name='Регистрационный номер ПЖИ'
    )

    cito = models.BooleanField(
        verbose_name='Срочность'
    )
