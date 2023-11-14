from modules.example.infrastructure.api.rest.v1.views.example_command_viewset import ExampleCommandViewSet
from rest_framework.routers import DefaultRouter

from modules.example.infrastructure.api.rest.v1.views.example_query_viewset import ExampleQueryViewSet

router = DefaultRouter()
router.register('example', ExampleCommandViewSet, basename='example-command')
router.register('example-query', ExampleQueryViewSet, basename='example-query')

urlpatterns = router.urls

