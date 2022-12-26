from abc import ABC, abstractmethod


class HeaderProvider(ABC):
    @abstractmethod
    def get(self):
        pass


class AoCHeaderProvider(HeaderProvider):
    def get(self):
        header = "| Day | Link to description | Link to solution\n" + \
                 "|:---|:---|:---:|\n"
        return header
