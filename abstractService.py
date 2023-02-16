from abc import ABC, abstractmethod
class IApiFetcher(ABC):
    @abstractmethod
    def print(self):
        pass