from modules.lifecase.domain.models.counter import CounterValue
from modules.lifecase.infrastructure.persistance.models.counter_model import CounterModel
from modules.lifecase.infrastructure.persistance.repository.counter_repository import CounterRepository


class CounterService:
    repository: CounterRepository
    title: str

    _counter: CounterModel

    def __init__(self, repository: CounterRepository, title: str):
        self._repository = repository
        self._counter = get_object_or_create()

    def _create_counter(self, title: str):
        ...

    def _get_counter_by_title(self, title: str):
        ...

    def current(self, title:str) -> CounterValue:
        ...

    def next(self, title:str) -> CounterValue:
        self.repository.get_counter_by_title(title)

    def set_current_no(self, title):
        ...

    def set_yearly_current_no(self, title):
        ...
