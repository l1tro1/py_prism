from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class SupportMethodGenerator(object):
  def __init__(self, timeout=10):
    self.timeout = timeout

  def wait_until_element_visible(self, by, selector):
    this = self
    def inner(self, timeout=this.timeout):
      wait = WebDriverWait(self.driver, timeout)
      wait.until(
        EC.visibility_of_element_located((by, selector))
      )
      return self.driver.find_element(by, selector)
    return inner

  def wait_until_element_invisible(self, by, selector):
    this = self
    def inner(self, timeout=this.timeout):
      wait = WebDriverWait(self.driver, timeout)
      wait.until(
        EC.invisibility_of_element_located((by, selector))
      )
      return None
    return inner

  def wait_until_element_to_be_clickable(self, by, selector):
    this = self
    def inner(self, timeout=this.timeout):
      wait = WebDriverWait(self.driver, timeout)
      wait.until(
        EC.element_to_be_clickable((by, selector))
      )
      return self.driver.find_element(by, selector)
    return inner

  def has_element(self, by, selector):
    this = self
    def inner(self):
      try:
        self.driver.find_element(by, selector)
        return True
      except NoSuchElementException:
        return False
    return inner

  def has_no_element(self, by, selector):
    this = self
    def inner(self):
      try:
        self.driver.find_element(by, selector)
        return False
      except NoSuchElementException:
        return True
    return inner

  def element_element(self, by, selector):
    this = self
    def inner(self):
      return self.driver.find_element(by, selector)
    return inner

  def element_elements(self, by, selector):
    this = self
    def inner(self):
      return self.driver.find_elements(by, selector)
    return inner