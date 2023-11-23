from dataclasses import dataclass
from typing import Generic, TypeVar

from common.domain.entities import Entity
from modules.lifecase.domain.value_objects import LifeCaseId, RegistrationNumberVO, PatientVO, BiopsyVO, DiseaseVO, \
    OrganizationVO

LifeCaseIdType = TypeVar('LifeCaseIdType', bound=LifeCaseId)


@dataclass(kw_only=True)
class LifeCase(Entity, Generic[LifeCaseIdType]):
    registration_number: RegistrationNumberVO
    patient: PatientVO
    biopsy: BiopsyVO
    disease: DiseaseVO
    organization: OrganizationVO
    cito: bool = False
    # status

    @staticmethod
    def factory(
            id_: LifeCaseIdType,
            registration_number: RegistrationNumberVO,
            patient: PatientVO,
            biopsy: BiopsyVO,
            disease: DiseaseVO,
            organization: OrganizationVO,
            cito: bool
    ) -> 'LifeCase':
        lifecase = LifeCase(
            id=id_,
            registration_number=registration_number,
            patient=patient,
            biopsy=biopsy,
            disease=disease,
            organization=organization,
            cito=cito
        )
        return lifecase
