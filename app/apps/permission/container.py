from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import PermissionService
from .repo import PermissionRepo


class PermissionContainer(containers.DeclarativeContainer):
    """
        permission dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    permission_repo = providers.Singleton(PermissionRepo)
    permission_service = providers.Singleton(PermissionService, repo=permission_repo, logger=CoreContainer.app_logger)
