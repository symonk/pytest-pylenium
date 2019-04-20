from __future__ import annotations

import logging
from typing import Union

from selenium.webdriver.remote import webdriver

from config.config import PyleniumConfig
from core.elements import PyElement
from core.locators import PyLocator
from drivers.pylenium_driver import PyleniumDriver
from page_objects.page_object import PyPage

log = logging.getLogger('pylenium')
log.setLevel(logging.INFO)

# global config object
config = PyleniumConfig()


def start(entry_point: Union[str, PyPage]) -> Union[PyleniumDriver, PyPage]:
    return PyleniumDriver().maximize().goto(PyleniumConfig().base_url + entry_point)


def terminate() -> None:
    PyleniumDriver().quit()


def get_driver() -> PyleniumDriver:
    return PyleniumDriver()


def get_wrapped_driver() -> webdriver:
    return PyleniumDriver().driver


def find(locator: PyLocator) -> PyElement:
    return PyleniumDriver().find(locator)
