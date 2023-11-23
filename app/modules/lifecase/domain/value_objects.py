from dataclasses import dataclass

from common.domain.value_objects import EntityId
from common.domain.value_objects import ValueObject


class LifeCaseId(EntityId):
    pass


@dataclass(frozen=True)
class RegistrationNumberVO(ValueObject):
    pass


@dataclass(frozen=True)
class PatientVO(ValueObject):
    pass


@dataclass(frozen=True)
class BiopsyVO(ValueObject):
    pass


@dataclass(frozen=True)
class DiseaseVO(ValueObject):
    pass


@dataclass(frozen=True)
class OrganizationVO(ValueObject):
    pass
