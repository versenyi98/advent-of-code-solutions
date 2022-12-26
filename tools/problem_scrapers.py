from abc import ABC, abstractmethod
from lxml import etree

import requests


class ProblemScraper(ABC):

    def __init__(self, url):
        self.url = url
        result = requests.get(url)
        self.tree = etree.HTML(result.text)

    @abstractmethod
    def get_testcases(self):
        pass

    @abstractmethod
    def get_problem_name(self):
        pass


class AoCProblemScraper(ProblemScraper):

    def get_testcases(self):
        pass

    def get_problem_name(self):
        xpath_expression = "//h2"
        return self.tree.xpath(xpath_expression)[0].text
