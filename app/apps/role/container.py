from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import RoleService
from .repo import RoleRepo


class RoleContainer(containers.DeclarativeContainer):
    """
        Role dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    role_repo = providers.Singleton(RoleRepo)
    role_service = providers.Singleton(RoleService, repo=role_repo, logger=CoreContainer.app_logger)
