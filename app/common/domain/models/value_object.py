import uuid
from dataclasses import dataclass


class GenericUUID(uuid.UUID):
    @classmethod
    def next_id(cls):
        return cls(int=uuid.uuid4().int)


class EntityId(GenericUUID):
    pass


@dataclass(frozen=True)
class ValueObject:
    ...
