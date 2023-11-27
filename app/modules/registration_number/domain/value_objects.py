from dataclasses import dataclass
from typing import ClassVar

from common.domain.value_objects import ValueObject, EntityId
from config import morfis_config


@dataclass(frozen=True)
class CounterValue(ValueObject):
    current_no: int
    yearly_current_no: int
    year: int
    month: int
    day: int
    week_no: int
    day_of_week: int


@dataclass(frozen=True)
class RegistrationNumberValue(ValueObject):
    _template: ClassVar[str] = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_TEMPLATE']

    value: str

    def __str__(self):
        return self.value

    @classmethod
    def format(cls, counter_value: CounterValue) -> 'RegistrationNumberValue':
        number = cls._template.format(
            current_no=counter_value.current_no,
            yearly_current_no=counter_value.yearly_current_no,
            day=counter_value.day,
            month=counter_value.month,
            year=counter_value.year,
            day_of_week=counter_value.day_of_week,
            week_no=counter_value.week_no,
        )
        return RegistrationNumberValue(number)


class CounterId(EntityId):
    pass


class RegistrationNumberId(EntityId):
    pass
