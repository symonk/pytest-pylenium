from __future__ import annotations

import os
from enum import Enum

from selenium.webdriver import DesiredCapabilities

# Pyleniums possible web element lookup strategy (by default)
from pylenium.utility.meta import Singleton


class FileDownloadMode(Enum):
    HTTP_GET = ("http_get",)
    PROXY = ("proxy",)


class Selector(Enum):
    CSS = "CSS"
    XPATH = "XPATH"
    ID = "ID"


# Pyleniums possible browser (by default)
class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


# Pyleniums page loading strategy (by default)
# This is basically how quickly Pylenium will attempt to proceed on page loads and click follow up actions
class PageLoadStrategy(Enum):
    NORMAL = "normal"
    FAST = "fast"
    EAGER = "eager"


class PyleniumConfig(metaclass=Singleton):

    _browser = os.getenv('pylenium_browser', BrowserType.CHROME)
    _headless = os.getenv('pylenium_headless', False)
    _remote = os.getenv('pylenium_remote', False)
    _browser_size = os.getenv('pylenium_browser_size', '1920x1080')
    _browser_version = os.getenv('pylenium_browser_version', None)
    _browser_position = os.getenv('pylenium_browser_position', None)
    _browser_maximized = os.getenv('pylenium_maximized', True)
    _wdm_enabled = os.getenv('pylenium_wdm_enabled', True)
    _browser_binary = os.getenv('pylenium_browser_binary', '')
    _page_load_strategy = os.getenv('pylenium_page_load_strategy', PageLoadStrategy.NORMAL)
    _desired_capabilities = DesiredCapabilities()
    _base_url = os.getenv('pylenium_base_url', 'http://localhost:8080/')
    _explicit_wait_timeout = os.getenv('pylenium_wait_timeout', 15)
    _polling_interval = os.getenv('pylenium_polling_interval', 200)
    _capture_screenshots = os.getenv('pylenium_screenshot', True)
    _capture_page_source = os.getenv('pylenium_pagesource', True)
    _click_with_javascript = os.getenv('pylenium_js_click', False)
    _selector_default = Selector.CSS
    _proxy_enabled = os.getenv('pylenium_proxy_on', False)
    _file_download = os.getenv('pylenium_file_download', FileDownloadMode.HTTP_GET)
    _reopen_browser = os.getenv('pylenium_reopen_browser', True)

    @property
    def reopen_browser(self) -> bool:
        return self._reopen_browser

    @reopen_browser.setter
    def reopen_browser(self, value: bool) -> PyleniumConfig:
        self._reopen_browser = value
        return self

    @property
    def proxy_enabled(self) -> bool:
        return self._proxy_enabled

    @proxy_enabled.setter
    def proxy_enabled(self, value: bool) -> PyleniumConfig:
        self._proxy_enabled = value
        return self

    @property
    def file_download(self) -> FileDownloadMode:
        return self._file_Download

    @proxy_enabled.setter
    def file_download(self, value: FileDownloadMode) -> PyleniumConfig:
        self.file_download = value
        return self

    @property
    def browser(self) -> BrowserType:
        return self._browser

    @browser.setter
    def browser(self, value: BrowserType) -> PyleniumConfig:
        self._browser = value
        return self

    @property
    def headless(self) -> bool:
        return self._headless

    @headless.setter
    def headless(self, value: bool) -> PyleniumConfig:
        self._headless = value
        return self

    @property
    def remote(self) -> bool:
        return self._remote

    @remote.setter
    def remote(self, value: bool) -> PyleniumConfig:
        self._remote = value
        return self

    @property
    def browser_size(self) -> str:
        return self._browser_size

    @browser_size.setter
    def browser_size(self, value: str) -> PyleniumConfig:
        self._browser_size = value
        return self

    @property
    def browser_version(self) -> str:
        return self._browser_version

    @browser_version.setter
    def browser_version(self, value: str) -> PyleniumConfig:
        self._browser_version = value
        return self

    @property
    def browser_position(self) -> str:
        return self._browser_position

    @browser_position.setter
    def browser_position(self, value: str) -> PyleniumConfig:
        self._browser_position = value
        return self

    @property
    def browser_maximized(self) -> bool:
        return self._browser_maximized

    @browser_maximized.setter
    def browser_maximized(self, value: bool) -> PyleniumConfig:
        self._browser_maximized = value
        return self

    @property
    def wdm_enabled(self) -> bool:
        return self._wdm_enabled

    @wdm_enabled.setter
    def wdm_enabled(self, value: bool) -> PyleniumConfig:
        self._wdm_enabled = value
        return self

    @property
    def browser_binary(self) -> str:
        return self._browser_binary

    @browser_binary.setter
    def browser_binary(self, value: str) -> PyleniumConfig:
        self._browser_binary = value
        return self

    @property
    def page_load_strategy(self) -> str:
        return self._page_load_strategy

    @page_load_strategy.setter
    def page_load_strategy(self, value: PageLoadStrategy) -> PyleniumConfig:
        self._page_load_strategy = value
        return self

    @property
    def desired_capabilities(self) -> DesiredCapabilities:
        return self._desired_capabilities

    @desired_capabilities.setter
    def desired_capabilities(self, value: DesiredCapabilities):
        self._desired_capabilities = value
        return self

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> PyleniumConfig:
        self._base_url = value
        return self

    @property
    def explicit_wait_timeout(self) -> int:
        return self._explicit_wait_timeout

    @explicit_wait_timeout.setter
    def explicit_wait_timeout(self, value: int) -> PyleniumConfig:
        self._explicit_wait_timeout = value
        return self

    @property
    def polling_timeout(self) -> int:
        return self._polling_timeout

    @polling_timeout.setter
    def polling_timeout(self, value: int) -> PyleniumConfig:
        self._polling_timeout = value
        return self

    @property
    def capture_screenshot(self) -> bool:
        return self._capture_screenshot

    @capture_screenshot.setter
    def capture_screenshot(self, value: bool) -> PyleniumConfig:
        self._capture_screenshot = value
        return self

    @property
    def capture_page_source(self) -> bool:
        return self._capture_pagesource

    @capture_page_source.setter
    def capture_page_source(self, value: bool) -> PyleniumConfig:
        self._capture_pagesource = value
        return self

    @property
    def javascript_clicking(self) -> bool:
        return self._javascript_clicking

    @javascript_clicking.setter
    def javascript_clicking(self, value: bool) -> PyleniumConfig:
        self._javascript_clicking = value
        return self

    @property
    def javascript_sendkeys(self) -> bool:
        return self._javascript_sendkeys

    @javascript_sendkeys.setter
    def javascript_sendkeys(self, value: bool) -> PyleniumConfig:
        self._javascript_sendkeys = value
        return self
