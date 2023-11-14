from common.infarastructure.repositories.repository import Repository
from modules.example.domain.models.example import Example
from modules.example.infrastructure.persistence.models.example_model import ExampleModel


class ExampleRepository(Repository):
    def create(self, example: Example) -> ExampleModel:
        print(example)
        example_model = ExampleModel.from_domain(example)
        example_model.save(force_insert=True)
        return example_model

    def update(self, example_model: ExampleModel, example: Example) -> ExampleModel:
        example_model.title = example.title
        example_model.status = example.status
        example_model.is_hidden = example.is_hidden
        example_model.save()
        return example_model

    def delete(self, example_model: ExampleModel):
        example_model.delete()
