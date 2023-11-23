from dataclasses import dataclass, InitVar, field
from enum import Enum

from common.domain.entities import AggregateRoot
from common.domain.value_objects import EntityId


# class MyIntEnum(Enum):
#
#     @classmethod
#     def choices(cls):
#         result = [(status.value[0], status.value[1]) for status in cls]
#         return result


# class Status(models.IntegerChoices):
# class Status(IntEnum):
# class Status(MyIntEnum):
#     INACTIVE = (0, 'Неактивен')
#     ACTIVE = (1, 'Активен')

class Status(Enum):
    INACTIVE = ('INACTIVE', 'Неактивен')
    ACTIVE = ('ACTIVE', 'Активен')

    @classmethod
    def choices(cls):
        result = [(status.value[0], status.value[1]) for status in cls]
        return result


class ExampleId(EntityId):
    pass


@dataclass(kw_only=True)
class Example(AggregateRoot):
    id: ExampleId
    title: str
    status: InitVar[Status]
    # _status: Status = field(init=False)
    is_hidden: bool = None

    def __post_init__(self, status: Status):
        print('post_init')
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
        self.is_hidden = (self._title == '')  # or self._status != Status.ACTIVE
