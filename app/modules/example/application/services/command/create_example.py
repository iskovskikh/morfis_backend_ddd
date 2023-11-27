from common.application.command.create import CommandCreate
from modules.example.domain.entities.example import Example, ExampleId
from modules.example.infrastructure.models.example_model import ExampleModel
from modules.example.infrastructure.repositories.example_repository import ExampleRepository


class CreateExample(CommandCreate):
    repository: ExampleRepository

    def handle(self) -> ExampleModel:
        example = Example.factory(
            id_=ExampleId.next_id(),
            title=self.validated_data['title'],
        )

        return self.repository.create(example)
