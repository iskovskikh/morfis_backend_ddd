from common.infarastructure.api.rest.views.rest_framewoork.command_model_viewset import CommandModelViewSet
from modules.example.application.services.command.create_example import CreateExample
from modules.example.application.services.command.update_example import UpdateExample
from modules.example.infrastructure.api.rest.v1.serializers.example_model_serializer import ExampleModelSerializer
from modules.example.infrastructure.persistence.models.example_model import ExampleModel
from modules.example.infrastructure.persistence.repository.example_repository import ExampleRepository


class ExampleCommandViewSet(CommandModelViewSet):
    queryset = ExampleModel.objects.filter()
    repository_class = ExampleRepository
    # event_store_repository_class = ...
    command_create_class = CreateExample
    command_update_class = UpdateExample
    # command_delete_class = DeleteExample
    serializer_class = ExampleModelSerializer
