class Elements(object):
  def __init__(self, by, selector):
    self.by = by
    self.selector = selector

  def __get__(self, obj, klass):
    # obj - owner of current class
    if hasattr(obj, 'base_element') and obj.base_element is not None:
      return obj.base_element.find_elements(self.by, self.selector)
    else:
      return obj.driver.find_elements(self.by, self.selector)