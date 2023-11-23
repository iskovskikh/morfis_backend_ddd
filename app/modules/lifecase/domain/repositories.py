from abc import ABC

from common.domain.repositories import GenericRepository
from modules.lifecase.domain.entities import LifeCase
from modules.lifecase.domain.value_objects import LifeCaseId


class LifeCaseRepositoryInterface(GenericRepository[LifeCaseId, LifeCase], ABC):
    ...
