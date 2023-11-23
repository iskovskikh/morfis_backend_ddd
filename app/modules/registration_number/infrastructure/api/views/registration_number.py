from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework import views, status
from rest_framework.response import Response

from modules.registration_number.application.use_case.commands import RegistrationNumberCommandUseCase


@extend_schema(tags=["lifecase"])
class RegistrationNumberRequestApi(views.APIView):
    class RegistrationNumberRequestSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        number = serializers.CharField(source='number.value')
        rent_expires_at_timestamp = serializers.DateTimeField()

    @extend_schema(
        summary="Сгенерировать новый регистрационный номер",
        description="Генерирует новый номер и ставит его в аренду",
        request=None,
        responses={201: RegistrationNumberRequestSerializer}
    )
    def put(self, request):
        registration_number_use_case = RegistrationNumberCommandUseCase()
        registration_number = registration_number_use_case.get_registration_number()
        serializer = self.RegistrationNumberRequestSerializer(registration_number)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
