from common.infarastructure.api.rest.serializers.rest_framework.model_serializer import ModelSerializer
from modules.example.infrastructure.persistence.models.example_model import ExampleModel
from rest_framework.serializers import SerializerMethodField


class ExampleModelSerializer(ModelSerializer):
    formatted_title = SerializerMethodField()

    class Meta:
        model = ExampleModel
        fields = [
            'id',
            'title',
            'formatted_title',
        ]

    def get_formatted_title(self, instance):
        if isinstance(instance, ExampleModel):
            return instance.formatted_title()