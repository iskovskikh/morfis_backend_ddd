from django.contrib import admin

from modules.lifecase.infrastructure.models.lifecase_model import LifeCaseModel


@admin.register(LifeCaseModel)
class LifeCaseModelAdmin(admin.ModelAdmin):
    pass
