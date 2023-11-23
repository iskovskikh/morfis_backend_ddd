from typing import TypeVar

from modules.registration_number.domain.entities import Counter
from modules.registration_number.domain.repositories import CounterRepositoryInterface
from modules.registration_number.domain.value_objects import CounterValue

RepositoryType = TypeVar('RepositoryType', bound=CounterRepositoryInterface)


class CounterService:
    _title: str
    _repository: RepositoryType

    def __init__(self, title: str, repository: RepositoryType):
        self._title = title
        self._repository = repository

    def current(self) -> CounterValue:
        counter: Counter = self._repository.get_or_create_by_title(self._title)
        return counter.current_value()

    def next(self) -> CounterValue:
        counter: Counter = self._repository.get_or_create_by_title(self._title)
        counter.next()
        self._repository.update(counter)
        return counter.current_value()

    def set_current_no(self, title):
        ...

    def set_yearly_current_no(self, title):
        ...
