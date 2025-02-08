class Sections(object):
    previous_elements = ''

    def __init__(self, klass, base_by, base_selector):
        self.klass = klass
        self.base_by = base_by
        self.base_selector = base_selector

    def __get__(self, obj, klass):

        # region saves full xpath from prev sections if they have xpath
        # xpath for concatenation  must start with dot
        element = obj.driver
        if hasattr(klass, 'previous_elements'):
            element = klass.previous_elements
        if hasattr(klass, 'previous_element'):
            element = klass.previous_element
        # endregion

        base_elements = element.find_elements(self.base_by, self.base_selector)
        self.klass.previous_elements = base_elements
        return [self.klass(obj.driver, base_element=base_element) for base_element in base_elements]