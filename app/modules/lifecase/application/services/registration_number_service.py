from datetime import timedelta

from config import utils
from config import morfis_config
from modules.lifecase.application.services.counter_service import CounterService
from modules.lifecase.domain.models.counter import CounterValue
from modules.lifecase.domain.models.registration_number import RegistrationNumber, RegistrationNumberId
from modules.lifecase.infrastructure.persistence.models.registration_number_model import RegistrationNumberModel
from modules.lifecase.infrastructure.persistence.repository.registration_number_repository import \
    RegistrationNumberRepository


class RegistrationNumberService:
    registration_number_repository: RegistrationNumberRepository
    counter_service: CounterService

    _template: str = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_LIFETIME']
    _lifetime: timedelta = morfis_config.MORFIS['REGISTRATION_NUMBER']['REGISTRATION_NUMBER_TEMPLATE']

    # def __init__(self):
    #     self._counter_service = CounterService()

    def _format_number(self, counter_value: CounterValue) -> str:
        number = self._template.format(
            current_no=counter_value.current_no,
            yearly_current_no=counter_value.yearly_current_no,
            day=counter_value.day,
            month=counter_value.month,
            year=counter_value.year,
            day_of_week=counter_value.day_of_week,
            week_no=counter_value.week_no,
        )

        return number

    @staticmethod
    def _calc_rent_timestamp():
        return cli.now() + RegistrationNumberService._lifetime

    def _create_new_registration_number(self) -> RegistrationNumberModel:
        registration_number = RegistrationNumber.factory(
            id_=RegistrationNumberId.next_id(),
            number=RegistrationNumberService._format_number(self.counter_service.next()),
            rent_timestamp=RegistrationNumberService._calc_rent_timestamp()
        )
        number_model = self.registration_number_repository.create(registration_number)
        return number_model

    def get_registration_number(self) -> RegistrationNumber:
        number_model = self.registration_number_repository.get_expired_number()
        print(number_model)
        if number_model is None:
            number_model = RegistrationNumberService._create_new_registration_number()
        print(number_model)
        return number_model.to_domain()
