from django.contrib import admin

from modules.registration_number.infrastructure.models.counter_model import CounterModel
from modules.registration_number.infrastructure.models.registration_number_model import RegistrationNumberModel


# Register your models here.


@admin.register(CounterModel)
class CounterModelAdmin(admin.ModelAdmin):
    pass


@admin.register(RegistrationNumberModel)
class RegistrationNumberModelAdmin(admin.ModelAdmin):
    pass