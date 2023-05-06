from dependency_injector import providers, containers

from ..role.container import RoleContainer
from ..user.container import UserContainer
from ..amenty.container import AmentyContainer
from ..detail.container import RoomDetailContainer
from ..category.container import CategoryContainer


class ApplicationContainer(containers.DeclarativeContainer):
    """
        Register all application dependencies
    """
    role_provider = providers.Container(RoleContainer)
    user_provider = providers.Container(UserContainer)
    amenty_provider = providers.Container(AmentyContainer)
    detail_provider = providers.Container(RoomDetailContainer)
    category_provider = providers.Container(CategoryContainer)
