class Iframe(object):
  def __init__(self, klass, base_by, base_selector):
    self.klass = klass
    self.base_by = base_by
    self.base_selector = base_selector

  def __get__(self, obj, klass):
    iframe_element = obj.driver.find_element(self.base_by, self.base_selector)
    return self.klass(obj.driver, iframe_element=iframe_element)