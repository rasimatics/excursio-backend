from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import ReservationService
from .repo import ReservationRepo


class ReservationContainer(containers.DeclarativeContainer):
    """
        Reservation dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    reservation_repo = providers.Singleton(ReservationRepo)
    reservation_service = providers.Singleton(ReservationService, repo=reservation_repo, logger=CoreContainer.app_logger)
