from abc import ABC, abstractmethod


class BaseQueue(ABC):

    @abstractmethod
    def publish(self):
        pass
