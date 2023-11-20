from modules.lifecase.domain.models.counter import CounterValue, Counter
from modules.lifecase.infrastructure.persistence.models.counter_model import CounterModel
from modules.lifecase.infrastructure.persistence.repository.counter_repository import CounterRepository


class CounterService:
    _repository: CounterRepository = CounterRepository()
    _counter_instance: CounterModel

    def __init__(self, title: str = 'default'):
        self._counter_instance = self._repository.get_or_create_counter_by_title(title)

    def current(self) -> CounterValue:
        counter: Counter = self._counter_instance.to_domain()
        return counter.current_value()

    def next(self) -> CounterValue:
        counter: Counter = self._counter_instance.to_domain()
        counter.next()
        self._counter_instance = self._repository.update(self._counter_instance, counter)
        return counter.current_value()

    def set_current_no(self, title):
        ...

    def set_yearly_current_no(self, title):
        ...
