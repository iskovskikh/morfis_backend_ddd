from django.contrib import admin
from modules.example.infrastructure.persistence.models.example_model import ExampleModel


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    pass
