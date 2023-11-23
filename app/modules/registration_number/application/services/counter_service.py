from modules.registration_number.domain.services import CounterServiceInterface
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository


class CounterService(CounterServiceInterface):
    title = 'lifecase_counter'
    repository = DjangoCounterRepository()
