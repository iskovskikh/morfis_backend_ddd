from django.test import TestCase

from modules.registration_number.application.services.counter_service import CounterService
from modules.registration_number.infrastructure.repositories.counter_repository import DjangoCounterRepository


class CounterServiceTest(TestCase):

    def test_create_counter(self):
        # print(DjangoCounterRepository.__mro__)
        counter_repo = DjangoCounterRepository()
        counter_service = CounterService(title='default', repository=counter_repo)
        data = counter_service.next()
        data = counter_service.next()
        print(data)
