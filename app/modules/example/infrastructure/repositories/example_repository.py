
from modules.example.domain.entities.example import Example
from modules.example.infrastructure.models.example_model import ExampleModel


class ExampleRepository:
    def create(self, example: Example) -> ExampleModel:
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
