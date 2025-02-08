from time import sleep
import re
from uritemplate import expand as uriexpand
from py_prism.page_meta_class import PageMetaclass
from py_prism.log import *

class Page(object, metaclass=PageMetaclass):
  _url = None
  _url_matcher = None

  def __init__(self, driver):
    self.driver = driver

  @logged
  def load(self, **kwargs):
    if self._url:
      uri = uriexpand(self._url, **kwargs)
      self.driver.get(uri)
    else:
      raise Exception(f"Cant load. {self.__class__} has not _url parameter")

  @logged
  def is_loaded(self):
    if self._url_matcher:
      if re.fullmatch(self._url_matcher, self.current_url):
        return True
      else:
        return False
    elif self._url:
      if self._url == self.current_url:
        return True
      else:
        return False
    else:
      raise Exception(f"Cant load check. {self.__class__} has neither _url and _url_matcher parameter")

    if self._url_matcher is not None and re.fullmatch(self._url_matcher, self.current_url):
      return True
    else:
      return False

  @logged
  def assert_loaded(self):
    if self.is_loaded():
       return True
    else:
      raise Exception(f"Page {self.__class__} is not loaded.")

  @logged
  def wait_until_page_loaded(self, timeout=10):
    for i in range(1, timeout+1):
      logger.debug(f"checking page is loaded {i}/{timeout}")
      if self.is_loaded():
        logger.debug(f"page is loaded!")
        break
      sleep(1)
    else:
      raise Exception(f"Timeout loading Page {self.__class__}")

  @logged
  def wait_until_page_readystate_is_complete(self, timeout=10):
    for i in range(1, timeout+1):
      logger.debug(f"checking document.readyState {i}/{timeout}")
      if self.driver.execute_script("return document.readyState") == "complete":
        logger.debug(f"document.readyState is complete!")
        break
      sleep(1)
    else:
      raise Exception(f"Timeout loading Page {self.__class__}")

  @property
  def current_url(self):
    return self.driver.current_url