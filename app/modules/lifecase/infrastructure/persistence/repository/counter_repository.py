from common.infarastructure.persistence.repository import Repository
from common.infarastructure.persistence.utils import get_object_or_none
from modules.lifecase.domain.models.counter import Counter, CounterId
from modules.lifecase.infrastructure.persistence.models.counter_model import CounterModel


class CounterRepository(Repository):

    @staticmethod
    def create(counter: Counter) -> CounterModel:
        counter_model = CounterModel.from_domain(counter)
        counter_model.save(force_insert=True)
        return counter_model

    @staticmethod
    def update(counter_model: CounterModel, counter: Counter) -> CounterModel:
        counter_model.current_no = counter.current_no
        counter_model.yearly_current_no = counter.yearly_current_no
        counter_model.save()
        return counter_model

    @staticmethod
    def get_counter_by_title(title: str) -> CounterModel | None:
        counter_model = get_object_or_none(CounterModel, title=title)
        return counter_model

    @staticmethod
    def get_or_create_counter_by_title(title: str) -> CounterModel:
        counter_model = CounterRepository.get_counter_by_title(title)
        if not counter_model:
            counter_model = CounterRepository.create(Counter(
                id=CounterId.next_id(),
                title=title,
                current_no=0,
                yearly_current_no=0
            ))
        return counter_model
