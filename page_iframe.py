from py_prism.page_meta_class import PageMetaclass

class PageIframe(object, metaclass=PageMetaclass):
  def __init__(self, driver, iframe_element):
    self.driver = driver
    self.iframe_element = iframe_element

  def __enter__(self):
    self.driver.switch_to_frame(self.iframe_element)
    return self

  def __exit__(self, *args):
    self.driver.switch_to.default_content()