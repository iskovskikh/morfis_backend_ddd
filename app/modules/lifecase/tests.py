from unittest import skip

from django.test import TestCase

from modules.lifecase.application.services.registration_number_service import RegistrationNumberService


# Create your tests here.


class RegistrationNumberServiceTest(TestCase):


    def test_create_new_number(self):
        number = RegistrationNumberService.get_registration_number()
        print(number)
        self.assertNotEqual(number, None)
