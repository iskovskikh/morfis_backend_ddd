from dataclasses import dataclass, InitVar
from datetime import datetime, timedelta
from typing import Generic, TypeVar, ClassVar

from common.domain.entities import Entity
from config import morfis_config
from config.utils import now
from modules.registration_number.domain.value_objects import CounterValue, RegistrationNumberValue, CounterId, \
    RegistrationNumberId

CounterIdType = TypeVar('CounterIdType', bound=CounterId)


@dataclass(kw_only=True)
class Counter(Entity, Generic[CounterIdType]):
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

    def _next_current_no(self):
        self._current_no += 1

    def _new_year_check(self):
        # todo: проверка на новый год
        # if new_year:
        #     self._yearly_current_no = 0
        pass

    def _next_yearly_current_no(self):
        self._new_year_check()
        self._yearly_current_no += 1

    def next(self) -> None:
        self._next_current_no()
        self._next_yearly_current_no()

    def current_value(self) -> CounterValue:
        current = now()
        year, week_no, day_of_week = current.isocalendar()

        result = CounterValue(
            current_no=self._current_no,
            yearly_current_no=self._yearly_current_no,
            year=year,
            month=current.month,
            day=current.day,
            week_no=week_no,
            day_of_week=day_of_week
        )
        return result


RegistrationNumberIdType = TypeVar('RegistrationNumberIdType', bound=RegistrationNumberId)


@dataclass(kw_only=True)
class RegistrationNumber(Entity, Generic[RegistrationNumberIdType]):
    lifetime: ClassVar[timedelta] = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_LIFETIME']

    number: RegistrationNumberValue
    rent_expires_at_timestamp: datetime

    @staticmethod
    def factory( counter_value: CounterValue) -> 'RegistrationNumber':
        return RegistrationNumber(
            id=RegistrationNumberId.next_id(),
            number=RegistrationNumberValue.format(counter_value),
            rent_expires_at_timestamp=RegistrationNumber.calc_rent_timestamp()
        )

    @classmethod
    def calc_rent_timestamp(cls) -> datetime:
        return now() + cls.lifetime
