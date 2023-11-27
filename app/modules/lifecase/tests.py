from django.test import TestCase

from modules.lifecase.application.services.lifecase_service import DjangoLifeCaseService
from modules.registration_number.application.services.registration_number_service import DjangoRegistrationNumberService


class LifeCaseServiceTest(TestCase):

    def test_create_new_lifecase(self):
        registration_number_service = DjangoRegistrationNumberService()
        registration_number = registration_number_service.get_registration_number()

        lifecase_service = DjangoLifeCaseService()
        lifecase_service.create_new_lifecase(
            registration_number_id=registration_number.id,
            validated_data=
            {
                'cito': True
            }
        )

    def query_lifecases(self):
        lifecase_service = DjangoLifeCaseService()
        lifecase_service.query_lifecases()