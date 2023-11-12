from common.application.command.create import CommandCreate
from modules.example.domain.models.example import Example, ExampleId
from modules.example.infarastructure.persistence.models.example_model import ExampleModel
from modules.example.infarastructure.persistence.repository.example_repository import ExampleRepository


class CreateExample(CommandCreate):
    repository: ExampleRepository

    def handle(self) -> ExampleModel:
        example = Example.factory(
            id_=ExampleId.next_id(),
            title=self.validated_data['title'],
        )

        return self.repository.create(example)
