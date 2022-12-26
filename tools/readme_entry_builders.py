import constants

from urllib.parse import quote
from abc import ABC, abstractmethod


class EntryBuilder(ABC):
    def __init__(self):
        self.entry = ""

    def get(self):
        return self.entry

    @abstractmethod
    def build(self, data):
        pass


class AoCEntryBuilder(EntryBuilder):
    def build(self, data):
        name = data["Name"]
        day = data["Day"]
        year = data["Year"]
        url = data["URL"]

        day = "%02d" % int(day)

        path_to_solution = f"{constants.GITHUB_MASTER_BRANCH}/{quote(f'Advent of Code/{year}/Day {day} - {name}')}"

        self.entry = f"| {day} | [{name}]({url}) | [Solution]({path_to_solution})|\n"
        return self
