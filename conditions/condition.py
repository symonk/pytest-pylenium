from __future__ import annotations
from abc import abstractmethod, ABC

from core.web_elements import PyElement


class PyCondition(ABC):

    @abstractmethod
    def evaluate(self, py_element: PyElement) -> PyElement:
        pass


class Text(PyCondition):
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element: PyElement) -> PyElement:
        assert py_element.text == self.expected
        return py_element