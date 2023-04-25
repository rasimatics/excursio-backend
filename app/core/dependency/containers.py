from dependency_injector import providers, containers
from ..logging.logger import get_app_logger


class CoreContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.apps", "app.core.exceptions"])

    app_logger = providers.Object(get_app_logger())
