from django.test import TestCase

from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.domain.value_objects import CounterValue
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository


class CounterServiceTest(TestCase):

    def test_create_counter(self):
        counter_repo = DjangoCounterRepository()
        counter_service = CounterService(title='default', repository=counter_repo)
        data1 = counter_service.next()
        # print(data1)
        self.assertIsInstance(data1, CounterValue)
        data2 = counter_service.next()
        # print(data2)
        self.assertIsInstance(data1, CounterValue)
        self.assertEqual(data1.current_no+1, data2.current_no)
