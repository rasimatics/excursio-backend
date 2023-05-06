from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import AmentyService
from .repo import AmentyRepo


class AmentyContainer(containers.DeclarativeContainer):
    """
        Amenty dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    amenty_repo = providers.Singleton(AmentyRepo)
    amenty_service = providers.Singleton(AmentyService, repo=amenty_repo, logger=CoreContainer.app_logger)
