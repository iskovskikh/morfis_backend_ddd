import uuid
from dataclasses import dataclass


class EntityId(uuid.UUID):
    @classmethod
    def next_id(cls):
        # return cls(int=uuid.uuid4().int)
        return cls(str(uuid.uuid4()))


# class EntityId(GenericUUID):
#     pass


@dataclass(frozen=True)
class ValueObject:
    ...
