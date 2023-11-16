from datetime import timedelta

from config import cli
from modules.lifecase.application.services.counter_service import CounterService
from modules.lifecase.domain.models.counter import CounterValue
from modules.lifecase.domain.models.registration_number import RegistrationNumber, RegistrationNumberId
from modules.lifecase.infrastructure.persistance.models.registration_number_model import RegistrationNumberModel
from modules.lifecase.infrastructure.persistance.repository.registration_number_repository import \
    RegistrationNumberRepositiry


class RegistrationNumberService:
    registration_number_repository: RegistrationNumberRepositiry
    counter_service: CounterService
    template: str = cli.settings.MORFIS.REGISTRATION_NUMBER.REGISTRATION_NUMBER_TEMPLATE
    lifetime: timedelta = cli.settings.MORFIS.REGISTRATION_NUMBER.REGISTRATION_NUMBER_LIFETIME

    def __init__(self):
        self.counter_service = CounterService()

    def _format_number(self, counter_value: CounterValue) -> str:
        number = self.template.format(
            current_no=counter_value.current_no,
            yearly_current_no=counter_value.yearly_current_no,
            day=counter_value.day,
            month=counter_value.month,
            year=counter_value.year,
            day_of_week=counter_value.day_of_week,
            week_no=counter_value.week_no,
        )

        return number

    def _calc_rent_timestamp(self):
        return cli.now() + self.lifetime

    def _create_new_registration_number(self) -> RegistrationNumberModel:
        registration_number = RegistrationNumber.factory(
            id_=RegistrationNumberId.next_id(),
            number=self._format_number(self.counter_service.next()),
            rent_timestamp=self._calc_rent_timestamp()
        )
        number_model = self.registration_number_repository.create(registration_number)
        return number_model

    def get_registration_number(self) -> RegistrationNumber:
        number_model = self.registration_number_repository.get_expired_number()
        if number_model is None:
            number_model = self._create_new_registration_number()

        return number_model.to_domain()
