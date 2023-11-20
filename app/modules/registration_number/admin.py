from django.contrib import admin

from modules.registration_number.infrastructure.models.counter_model import CounterModel


# Register your models here.


@admin.register(CounterModel)
class CounterModelAdmin(admin.ModelAdmin):
    pass