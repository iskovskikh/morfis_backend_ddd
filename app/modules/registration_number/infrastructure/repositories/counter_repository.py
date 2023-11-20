from common.infarastructure.data_mapper import DataMapper
from common.infarastructure.repository import DjangoGenericRepository
from modules.registration_number.domain.entities import Counter, CounterId
from modules.registration_number.domain.repositories import CounterRepository
from modules.registration_number.infrastructure.models.counter_model import CounterModel

from django.core.exceptions import ObjectDoesNotExist

class DjangoCounterDataMapper(DataMapper[Counter, CounterModel]):

    def model_to_entity(self, instance: CounterModel) -> Counter:
        return Counter(
            id=CounterId(instance.id),
            title=instance.title,
            current_no=instance.current_no,
            yearly_current_no=instance.yearly_current_no
        )

    def entity_to_model(self, entity: Counter) -> CounterModel:
        return CounterModel(
            id=entity.id,
            title=entity.title,
            current_no=entity.current_no,
            yearly_current_no=entity.yearly_current_no
        )


class DjangoCounterRepository(CounterRepository, DjangoGenericRepository):
    mapper_class = DjangoCounterDataMapper
    model_class = CounterModel

    # def get_by_title(self, title: str) -> Counter:
    #     ...

    def get_or_create_by_title(self, title: str) -> Counter:
        try:
            instance = self.model_class.objects.get(title=title)
            counter = self.map_model_to_entity(instance)
        except ObjectDoesNotExist:
            counter = Counter(
                id=self.next_id(),
                title=title,
                current_no=0,
                yearly_current_no=0
            )
            self.add(counter)

        return counter
