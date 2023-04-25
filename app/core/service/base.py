from typing import TypeVar, Generic, Type
from logging import Logger
from ..repo.base import BaseRepo


class BaseService:
    pass


RepoType = TypeVar("RepoType", bound=BaseRepo)


class BaseSqlAlchemyService(BaseService, Generic[RepoType]):
    def __init__(self, repo: Type[RepoType]):
        self.repo = repo


class BaseSqlAlchemyServiceWithLogging(BaseSqlAlchemyService[RepoType]):
    def __init__(self, repo, logger):
        self.logger = logger
        super().__init__(repo)

