from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import RoomService
from .repo import RoomRepo, PhotoRepo, RoomAmenitiesRepo


class RoomContainer(containers.DeclarativeContainer):
    """
        Room dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])
    room_repo = providers.Singleton(RoomRepo)
    amenity_repo = providers.Singleton(RoomAmenitiesRepo)
    photo_repo = providers.Singleton(PhotoRepo)
    room_service = providers.Singleton(
        RoomService, 
        room_repo=room_repo, 
        amenity_repo=amenity_repo,
        photo_repo=photo_repo,
        logger=CoreContainer.app_logger
    )
