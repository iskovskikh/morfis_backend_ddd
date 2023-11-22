from django.test import TestCase

from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.application.services.registration_number_service import RegistrationNumberService
from modules.registration_number.domain.value_objects import CounterValue, RegistrationNumberValue
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository
from modules.registration_number.infrastructure.repositories.registration_number_repository import \
    DjangoRegistrationNumberRepository


class CounterServiceTest(TestCase):

    def test_create_counter(self):
        counter_repo = DjangoCounterRepository()
        counter_service = CounterService(title='default', repository=counter_repo)
        data1 = counter_service.next()
        # print(data1)
        self.assertIsInstance(data1, CounterValue)
        data2 = counter_service.next()
        # print(data2)
        self.assertIsInstance(data2, CounterValue)
        self.assertEqual(data1.current_no+1, data2.current_no)


class RegistrationNumberServiceTest(TestCase):

    def test_registration_number_generator(self):
        registration_number_repo = DjangoRegistrationNumberRepository()
        registration_number_service = RegistrationNumberService(repository=registration_number_repo)
        data1 = registration_number_service.get_registration_number()
        # print(data1)
        self.assertIsInstance(data1, RegistrationNumberValue)
        data2 = registration_number_service.get_registration_number()
        # print(data2)
        self.assertIsInstance(data2, RegistrationNumberValue)
