from dataclasses import dataclass, InitVar
from datetime import datetime
from typing import Generic, TypeVar

from common.domain.entity import Entity
from common.domain.value_object import EntityId
from config import utils
from modules.registration_number.domain.value_objects import CounterValue, RegistrationNumberValue


class ExampleAggregateId(EntityId):
    pass


ExampleAggregateIdType = TypeVar('ExampleAggregateIdType', bound=ExampleAggregateId)


class CounterId(EntityId):
    pass


#
# class UniqueValidator(Validator):
#     def hadle(self, *args)->bool:
#         ...


# invariant title Unique
# @invarian({'title', UniqueValidator})
# @invarian({'current_no', NonNegative})
@dataclass(kw_only=True)
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
        now = utils.now()
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


class RegistrationNumberId(EntityId):
    pass


RegistrationNumberIdType = TypeVar('RegistrationNumberIdType', bound=RegistrationNumberId)


@dataclass(kw_only=True)
class RegistrationNumber(Entity, Generic[RegistrationNumberIdType]):
    # id: RegistrationNumberId
    number: RegistrationNumberValue
    rent_expires_at_timestamp: datetime

# class PatientDictionaryAggregate(Entity, Generic[PatientDictionaryAggregateIdType]):
#     id: PatientDictionaryAggregateIdType
#     first_name: str
#     last_name: str
#     ...
#
# /// ========
#
# # class PatientLifecaseAggregate(Entity, Generic[PatientLifecaseAggregateIdType]):
# #     id: PatientLifecaseAggregateIdType
# #     first_name: str
#
#
# @dataclass(kw_only=True)
# class LifecaseAggregate(Entity, Generic[ExampleAggregateIdType]):
#     ...
#     #patient_1: PatientLifecase[Entity]
#     #patient_2: PatientLifecaseId[EntityId]
#     patient_3: PatientValueObject[ValueObject]
