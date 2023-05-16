from dependency_injector import containers, providers

from ...core.dependency.containers import CoreContainer
from .service import ReviewService
from .repo import ReviewRepo


class ReviewContainer(containers.DeclarativeContainer):
    """
        Review dependencies
    """
    wiring_config = containers.WiringConfiguration(packages=["app.apps"])

    review_repo = providers.Singleton(ReviewRepo)
    review_service = providers.Singleton(ReviewService, repo=review_repo, logger=CoreContainer.app_logger)
