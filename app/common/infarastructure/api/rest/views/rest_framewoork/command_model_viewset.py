from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CommandModelViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    repository_class = None
    command_create_class = None
    command_update_class = None
    command_delete_class = None

    def perform_create(self, serializer):
        # serializer.save()

        create_class = self.command_create_class()
        create_class.validated_data = serializer.validated_data
        create_class.repository = self.repository_class()
        create_class.handle()
