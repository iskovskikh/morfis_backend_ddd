import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def handle(self):
        raise NotImplementedError
