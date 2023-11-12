from common.infarastructure.api.rest.views.rest_framewoork.command_model_viewset import CommandModelViewSet
from modules.example.application.command.create_example import CreateExample
from modules.example.infarastructure.persistance.repository.example_repository import ExampleRepository
from modules.example.infarastructure.persistance.models.example_model import ExampleModel
from modules.example.application.command.update_example import UpdateExample
from modules.example.infarastructure.api.rest.v1.serializers.example_model_serializer import ExampleModelSerializer


class ExampleCommandViewSet(CommandModelViewSet):
    queryset = ExampleModel.objects.filter()
    repository_class = ExampleRepository
    # event_store_repository_class = ...
    command_create_class = CreateExample
    command_update_class = UpdateExample
    # command_delete_class = DeleteExample
    serializer_class = ExampleModelSerializer