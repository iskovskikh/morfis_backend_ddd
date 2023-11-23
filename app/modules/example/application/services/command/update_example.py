from dataclasses import dataclass

from common.application.commands.update import CommandUpdate
from modules.example.infrastructure.repositories.example_repository import ExampleRepository
from modules.example.infrastructure.models.example_model import ExampleModel
from modules.example.domain.entities.example import Example


@dataclass
class UpdateExample(CommandUpdate):
    repository: ExampleRepository
    instance: ExampleModel

    def handle(self) -> ExampleModel:
        example: Example = self.instance.to_domain()
        example.title = self.validated_data['title']

        return self.repository.update(self.instance, example)
