from dependency_injector import containers, providers

from app.core.dependency.containers import CoreContainer
from ..permission.container import PermissionContainer
from .service import UserService
from .repo import UserRepo


class UserContainer(containers.DeclarativeContainer):
    """
        User dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    user_repo = providers.Singleton(UserRepo)
    user_service = providers.Singleton(
        UserService, 
        repo=user_repo, 
        permission_service=PermissionContainer.permission_service,
        logger=CoreContainer.app_logger,
    )
