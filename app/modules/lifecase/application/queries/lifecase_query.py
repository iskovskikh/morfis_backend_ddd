from common.application.query.query import Query
from modules.lifecase.domain.repositories import LifeCaseRepositoryInterface


class LifeCaseQuery(Query):

    def get_lifecases(self):
        ...
