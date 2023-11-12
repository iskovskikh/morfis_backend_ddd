from dataclasses import dataclass, InitVar
from enum import IntEnum

from common.domain.models.entity import AggregateRoot
from common.domain.models.value_object import EntityId


class Status(IntEnum):
    INACTIVE = 0, 'Неактивен'
    ACTIVE = 1, 'Активен'


class ExampleId(EntityId):
    pass


@dataclass(kw_only=True)
class Example(AggregateRoot):
    id: ExampleId
    title: str
    status: InitVar[Status]
    is_hidden: bool = None

    def __post_init__(self, status: Status):
        # super(Example, self).__post_init__()
        self._status = status

    @staticmethod
    def factory(
            id_: ExampleId,
            title: str,
    ) -> 'Example':

        example_entity = Example(
            id=id_,
            title=title,
            status=Status.ACTIVE,
        )

        example_entity.allow_for_show_check()
        #  do something with example_entity

        return example_entity

    @property
    def title(self):
        return self._title

    # noinspection PyAttributeOutsideInit
    @title.setter
    def title(self, title):
        self._title = title
        self.allow_for_show_check()

    @property
    def status(self):
        return self._status

    # noinspection PyAttributeOutsideInit
    @status.setter
    def status(self, status):
        self._status = status
        self.allow_for_show_check()

    def allow_for_show_check(self):
        self.is_hidden = (self._title == '') or self._status != Status.ACTIVE
