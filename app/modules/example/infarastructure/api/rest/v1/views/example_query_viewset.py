from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from common.infarastructure.api.rest.views.rest_framewoork.query_model_viewset import QueryModelViewSet
from modules.example.infarastructure.persistance.models.example_model import ExampleModel
from modules.example.infarastructure.api.rest.v1.serializers.example_model_serializer import ExampleModelSerializer


class ExampleQueryPagination(PageNumberPagination):
    # page_size =
    pass


class ExampleQueryViewSet(QueryModelViewSet):
    queryset = ExampleModel.objects.filter().order_by()
    pagination_class = ExampleQueryPagination
    serializer_class = ExampleModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['status', 'is_hidden', ]
