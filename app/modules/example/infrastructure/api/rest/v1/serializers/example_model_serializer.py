from rest_framework.serializers import SerializerMethodField, ReadOnlyField

from common.infarastructure.api.rest.serializers.rest_framework.model_serializer import ModelSerializer
from modules.example.infrastructure.models.example_model import ExampleModel


class ExampleModelSerializer(ModelSerializer):
    id = ReadOnlyField()
    formatted_title = SerializerMethodField()

    class Meta:
        model = ExampleModel
        fields = [
            'id',
            'title',
            'formatted_title',
            'status',
            'is_hidden',
        ]

    def get_formatted_title(self, instance):
        if isinstance(instance, ExampleModel):
            return instance.formatted_title()
