from django.contrib import admin
from modules.example.infrastructure.models.example_model import ExampleModel


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    pass
