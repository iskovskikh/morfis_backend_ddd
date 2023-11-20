from django.db import models

from common.infarastructure.persistence.model import BaseModel
from modules.lifecase.domain.models.counter import Counter, CounterId


class CounterModel(BaseModel):
    title = models.CharField(
        max_length=32,
        unique=True,
        verbose_name='Название счетчика'
    )

    current_no = models.IntegerField(
        verbose_name='Сквозной номер'
    )

    yearly_current_no = models.IntegerField(
        verbose_name='Сквозной номер за год'
    )

    def to_domain(self) -> Counter:
        return Counter(
            id=CounterId(self.id),
            title=self.title,
            current_no=self.current_no,
            yearly_current_no=self.yearly_current_no
        )

    @classmethod
    def from_domain(cls, counter: Counter) -> 'CounterModel':
        return CounterModel(
            id=counter.id,
            title=counter.title,
            current_no=counter.current_no,
            yearly_current_no=counter.yearly_current_no
        )
