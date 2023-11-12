from common.domain.entity import AggregateRoot, Aggregate
from common.domain.value_objects import GenericUUID


class Counter(Aggregate[GenericUUID]):
    count: int


class RegisterNumber(Aggregate[GenericUUID]):
    number: Counter


class LifeCaseAggregate(AggregateRoot[GenericUUID]):
    register_number: RegisterNumber
    cito: bool
