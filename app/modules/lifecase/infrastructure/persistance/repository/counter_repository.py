from common.infarastructure.persistance.repository import Repository
from modules.lifecase.domain.models.counter import Counter
from modules.lifecase.infrastructure.persistance.models.counter_model import CounterModel
from django.utils import

class CounterRepository(Repository):
    def create(self, counter: Counter) -> CounterModel:
        counter_model = CounterModel.from_domain(counter)
        counter_model.save()
        return counter_model

    def get_or_create_counter_by_title(self, title: str) -> CounterModel:
        counter_model, created = CounterModel.objects.get_or_create(title=title)
        return counter_model

# class ExampleRepository(Repository):
#     def create(self, example: Example) -> ExampleModel:
#         print(example)
#         example_model = ExampleModel.from_domain(example)
#         example_model.save(force_insert=True)
#         return example_model
#
#     def update(self, example_model: ExampleModel, example: Example) -> ExampleModel:
#         example_model.title = example.title
#         example_model.status = example.status
#         example_model.is_hidden = example.is_hidden
#         example_model.save()
#         return example_model
#
#     def delete(self, example_model: ExampleModel):
#         example_model.delete()
