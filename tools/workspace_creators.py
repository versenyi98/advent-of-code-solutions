import json
import os

from pathlib import Path
from abc import ABC, abstractmethod

from problem_scrapers import AoCProblemScraper


class WorkspaceCreator(ABC):
    def __init__(self, url):
        self.problem_scraper = None
        self.base_path = Path(__file__).absolute().parent.parent
        self.url = url

    def create_workspace(self):
        self.create_directory()
        self.write_testcases()
        self.write_info_json()

    @abstractmethod
    def create_directory(self):
        pass

    @abstractmethod
    def write_testcases(self):
        pass

    @abstractmethod
    def write_info_json(self):
        pass


class NoWorkspaceCreator(WorkspaceCreator):
    def create_directory(self):
        pass

    def write_testcases(self):
        pass

    def write_info_json(self):
        pass


class AocWorkspaceCreator(WorkspaceCreator):
    def __init__(self, url):
        super().__init__(url)
        self.problem_scraper = AoCProblemScraper(url)
        self.solutions_dir = self.base_path / "solutions"
        self.problem_dir = None

    def create_directory(self):
        year_dir = self.url.split('/')[-3]
        problem_dir = self.problem_scraper.get_problem_name()
        problem_dir = problem_dir.replace("-", "").strip().replace(":", " -")
        problem_dir_split = problem_dir.split()
        if len(problem_dir_split[1]) == 1:
            problem_dir_split[1] = "0" + problem_dir_split[1]
        problem_dir = " ".join(problem_dir_split)
        self.problem_dir = self.solutions_dir / year_dir / problem_dir

        if not os.path.exists(self.problem_dir):
            os.makedirs(os.path.dirname(self.problem_dir), exist_ok=True)
            os.mkdir(self.problem_dir)

    def write_testcases(self):
        pass

    def write_info_json(self):
        problem_name = self.problem_scraper.get_problem_name()
        problem_name = problem_name.replace("-", "").split(":")[-1].strip()

        year = self.url.split('/')[-3]
        day = self.url.split('/')[-1]

        info = {
            "Name": problem_name,
            "URL": self.url,
            "Year": year,
            "Day": day
        }

        with open(self.problem_dir / "info.json", "w") as json_handle:
            json.dump(info, json_handle, indent=4)
