from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import CategoryService
from .repo import CategoryRepo


class CategoryContainer(containers.DeclarativeContainer):
    """
        Category dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    category_repo = providers.Singleton(CategoryRepo)
    category_service = providers.Singleton(CategoryService, repo=category_repo, logger=CoreContainer.app_logger)
