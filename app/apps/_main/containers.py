from dependency_injector import providers, containers

from ..role.container import RoleContainer
from ..user.container import UserContainer


class ApplicationContainer(containers.DeclarativeContainer):
    """
        Register all application dependencies
    """
    role_provider = providers.Container(RoleContainer)
    user_provider = providers.Container(UserContainer)
