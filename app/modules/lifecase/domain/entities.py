from dataclasses import dataclass
from typing import Generic, TypeVar

from common.domain.entities import Entity
from modules.lifecase.domain.value_objects import LifeCaseId, RegistrationNumberVO, PatientVO, BiopsyVO, DiseaseVO, \
    OrganizationVO
from modules.registration_number.domain.value_objects import RegistrationNumberValue

LifeCaseIdType = TypeVar('LifeCaseIdType', bound=LifeCaseId)


@dataclass(kw_only=True)
class LifeCase(Entity, Generic[LifeCaseIdType]):
    registration_number: RegistrationNumberValue
    # patient: PatientVO
    # biopsy: BiopsyVO
    # disease: DiseaseVO
    # organization: OrganizationVO
    cito: bool = False

    # status

    @staticmethod
    def factory(
            registration_number: RegistrationNumberValue,
            # patient: PatientVO,
            # biopsy: BiopsyVO,
            # disease: DiseaseVO,
            # organization: OrganizationVO,
            cito: bool
    ) -> 'LifeCase':
        lifecase = LifeCase(
            id=LifeCaseId.next_id(),
            registration_number=registration_number,
            # patient=patient,
            # biopsy=biopsy,
            # disease=disease,
            # organization=organization,
            cito=cito
        )
        return lifecase
