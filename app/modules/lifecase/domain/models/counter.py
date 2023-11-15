from dataclasses import dataclass, InitVar

from common.domain.models.value_object import ValueObject
from common.domain.repository import Entity
from config import cli


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
class CounterId(ValueObject):
    pass


@dataclass
class Counter(Entity):
    id: CounterId
    title: str
    current_no: InitVar[int]
    yearly_current_no: InitVar[int]

    def __post_init__(self,
                      current_no: int,
                      yearly_current_no: int):
        self._current_no = current_no
        self._yearly_current_no = yearly_current_no

    @property
    def current_no(self):
        return self._current_no

    @property
    def yearly_current_no(self):
        return self._yearly_current_no

    def next(self) -> CounterValue:
        self._current_no += 1
        self._yearly_current_no += 1
        return self.current()

    def current(self) -> CounterValue:
        now = cli.now()
        year, week_no, day_of_week = now.isocalendar()

        result = CounterValue(
            current_no=self._current_no,
            yearly_current_no=self._yearly_current_no,
            year=year,
            month=now.month,
            day=now.day,
            week_no=week_no,
            day_of_week=day_of_week
        )
        return result