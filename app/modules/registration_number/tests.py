from django.test import TestCase

from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.application.services.registration_number_service import DjangoRegistrationNumberService
from modules.registration_number.domain.entities import RegistrationNumber
from modules.registration_number.domain.value_objects import CounterValue


class CounterServiceTest(TestCase):

    def test_create_counter(self):
        counter_service = CounterService()
        counter_1 = counter_service.next()
        # print(data1)
        self.assertIsInstance(counter_1, CounterValue)
        counter_2 = counter_service.next()
        # print(data2)
        self.assertIsInstance(counter_2, CounterValue)
        self.assertEqual(counter_1.current_no + 1, counter_2.current_no)


class RegistrationNumberServiceTest(TestCase):

    def test_registration_number_generator(self):
        registration_number_service = DjangoRegistrationNumberService()
        registration_number_1 = registration_number_service.get_registration_number()
        # print(data1)
        self.assertIsInstance(registration_number_1, RegistrationNumber)
        registration_number_2 = registration_number_service.get_registration_number()
        # print(data2)
        self.assertIsInstance(registration_number_2, RegistrationNumber)
