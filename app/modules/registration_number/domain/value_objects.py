from dataclasses import dataclass

from common.domain.value_object import ValueObject


@dataclass(frozen=True)
class CounterValue(ValueObject):
    current_no: int
    yearly_current_no: int
    year: int
    month: int
    day: int
    week_no: int
    day_of_week: int
