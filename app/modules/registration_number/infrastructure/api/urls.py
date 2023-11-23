from django.urls import path

from modules.registration_number.infrastructure.api.views.registration_number import RegistrationNumberRequestApi

urlpatterns = [
    path('registration-number/', RegistrationNumberRequestApi.as_view(), name='registration_number_request'),
]
