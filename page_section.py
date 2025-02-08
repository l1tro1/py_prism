from py_prism.page_meta_class import PageMetaclass

class PageSection(object, metaclass=PageMetaclass):
  def __init__(self, driver, base_element):
    self.driver = driver
    self.base_element = base_element

  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass