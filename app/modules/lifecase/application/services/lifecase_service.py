from modules.lifecase.domain.services import LifeCaseServiceInterface
from modules.lifecase.infrastructure.repositories.lifecase_repository import DjangoLifeCaseRepository
from modules.registration_number.application.services.registration_number_service import \
    DjangoRegistrationNumberService
from modules.registration_number.infrastructure.repositories.registration_number_repository import \
    DjangoRegistrationNumberRepository


class DjangoLifeCaseService(LifeCaseServiceInterface):
    lifecase_repo = DjangoLifeCaseRepository()
    registration_number_repo = DjangoRegistrationNumberRepository()
    registration_number_service = DjangoRegistrationNumberService()
