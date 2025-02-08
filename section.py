class Section(object):
    """ Class finds element of web page which have object of Element's class"""
    previous_element = ''

    def __init__(self, klass, base_by, base_selector):
        self.klass = klass
        self.base_by = base_by
        self.base_selector = base_selector

    def __get__(self, obj, klass):

        # region saves full xpath from prev sections if they have xpath
        # xpath for concatenation  must start with dot
        element = obj.driver
        if hasattr(klass, 'previous_element'):
            element = klass.previous_element
        # endregion

        base_element = element.find_element(self.base_by, self.base_selector)
        self.klass.previous_element = base_element
        return self.klass(obj.driver, base_element=base_element)