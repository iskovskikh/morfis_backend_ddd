from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.settings import api_settings


class CommandCreateModelMixin(mixins.CreateModelMixin):
    command_create_class = None
    repository_class = None

    def perform_create(self, serializer):
        create_class = self.command_create_class()
        create_class.validated_data = serializer.validated_data
        create_class.repository = self.repository_class()
        create_class.handle()


class CommandUpdateModelMixin(mixins.UpdateModelMixin):
    command_update_class = None
    repository_class = None

    def perform_update(self, serializer):
        update_class = self.command_update_class()
        update_class.validated_data = serializer.validated_data
        update_class.repository = self.repository_class()
        update_class.handle()




class CommandModelViewSet(CommandCreateModelMixin,
                          CommandUpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet
                          ):
    repository_class = None
    command_delete_class = None

# class CommandModelViewSet(
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     GenericViewSet,
#
# ):
#
#
#     repository_class = None
#     command_create_class = None
#     command_update_class = None
#     command_delete_class = None
#
#     def perform_create(self, serializer):
#         # serializer.save()
#
#         create_class = self.command_create_class()
#         create_class.validated_data = serializer.validated_data
#         create_class.repository = self.repository_class()
#         create_class.handle()
