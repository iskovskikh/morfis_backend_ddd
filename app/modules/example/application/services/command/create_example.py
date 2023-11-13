from common.application.services.command.create import CommandCreate
from modules.example.domain.models.example import Example, ExampleId
from modules.example.infrastructure.persistence.models.example_model import ExampleModel
from modules.example.infrastructure.persistence.repository.example_repository import ExampleRepository


class CreateExample(CommandCreate):
    repository: ExampleRepository

    def handle(self) -> ExampleModel:
        example = Example.factory(
            id_=ExampleId.next_id(),
            title=self.validated_data['title'],
        )

        return self.repository.create(example)
