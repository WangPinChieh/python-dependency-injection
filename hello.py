import requests
import googleService
import w3schoolsService
from abstractService import IApiFetcher
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    apiFetcher = providers.Singleton(
        googleService.ApiFetcher
    )


def main(apiFetcher: IApiFetcher = Provide[Container.apiFetcher]):
    result={}
    apiFetcher.print()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
