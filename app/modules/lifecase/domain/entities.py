from dataclasses import dataclass
from typing import Generic, TypeVar

from common.domain.entities import Entity
from common.domain.value_objects import ValueObject
from modules.lifecase.domain.value_objects import LifeCaseId

LifeCaseIdType = TypeVar('LifeCaseIdType', bound=LifeCaseId)


@dataclass(frozen=True)
class RegistrationNumberValue(ValueObject):
    pass


@dataclass(kw_only=True)
class LifeCase(Entity, Generic[LifeCaseIdType]):
    registration_number: RegistrationNumberValue
    # patient: ...
    # biopsy: ...
    # disease: ...
    # organization: ...
    cito: bool = False

    @staticmethod
    def factory(
            id_: LifeCaseIdType,
            registration_number: RegistrationNumberValue,
            cito: bool
    ) -> 'LifeCase':
        lifecase = LifeCase(
            id=id_,
            registration_number=registration_number,
            cito=cito
        )
        return lifecase
