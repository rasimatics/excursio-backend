from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import RoomDetailService
from .repo import RoomDetailRepo


class RoomDetailContainer(containers.DeclarativeContainer):
    """
        RoomDetail dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    room_detail_repo = providers.Singleton(RoomDetailRepo)
    room_detail_service = providers.Singleton(RoomDetailService, repo=room_detail_repo, logger=CoreContainer.app_logger)
