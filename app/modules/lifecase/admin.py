from django.contrib import admin

from modules.lifecase.infrastructure.persistence.models.counter_model import CounterModel
from modules.lifecase.infrastructure.persistence.models.registration_number_model import RegistrationNumberModel


@admin.register(CounterModel)
class CounterModelAdmin(admin.ModelAdmin):
    pass


@admin.register(RegistrationNumberModel)
class RegistrationNumberModelAdmin(admin.ModelAdmin):
    pass
