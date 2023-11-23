from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.domain.services import RegistrationNumberServiceInterface
from modules.registration_number.infrastructure.repositories.registration_number_repository import \
    DjangoRegistrationNumberRepository


class RegistrationNumberService(RegistrationNumberServiceInterface):
    registration_number_repo = DjangoRegistrationNumberRepository()
    counter_service = CounterService()
