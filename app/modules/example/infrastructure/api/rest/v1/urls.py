from modules.example.infrastructure.api.rest.v1.views.example_command_viewset import ExampleCommandViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('example', ExampleCommandViewSet, basename='example')

urlpatterns = router.urls

