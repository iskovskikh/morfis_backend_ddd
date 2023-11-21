from django.db import models

from common.infarastructure.persistence.model import BaseModel
from modules.lifecase.domain.models.counter import Counter, CounterId


class CounterModel(BaseModel):
    title = models.CharField(
        max_length=32,
        unique=True,
        # validators=[
        #     UniqueValidator,
        # ]
        verbose_name='Название счетчика'
    )

    current_no = models.IntegerField(
        verbose_name='Сквозной номер'
    )

    yearly_current_no = models.IntegerField(
        verbose_name='Сквозной номер за год'
    )