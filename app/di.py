from dependency_injector import containers, providers

from .apps._main.containers import ApplicationContainer
from .core.dependency.containers import CoreContainer


class AllContainers(containers.DeclarativeContainer):
    core_containers = providers.Container(CoreContainer)
    application_containers = providers.Container(ApplicationContainer)
