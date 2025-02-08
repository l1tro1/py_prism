from py_prism import *

class PageMetaclass(type):
  def __new__(cls, name, bases, dict_):
    for k, v in list(dict_.items()):
      if isinstance(v, Element) or isinstance(v, Elements):
        smg = SupportMethodGenerator()
        dict_[f"wait_until_{k}_visible"] = smg.wait_until_element_visible(v.by, v.selector)
        dict_[f"wait_until_{k}_invisible"] = smg.wait_until_element_invisible(v.by, v.selector)
        dict_[f"wait_until_{k}_to_be_clickable"] = smg.wait_until_element_to_be_clickable(v.by, v.selector)
        # Elementsのときもfind_elementが使われるため、「少なくとも1つのelementがあるかどうか」が検査される
        dict_[f"has_{k}"] = smg.has_element(v.by, v.selector)
        dict_[f"has_no_{k}"] = smg.has_no_element(v.by, v.selector)

        if isinstance(v, Element):
          dict_[f"{k}_element"] = smg.element_element(v.by, v.selector)
        elif isinstance(v, Elements):
          dict_[f"{k}_elements"] = smg.element_elements(v.by, v.selector)

      if isinstance(v, Section) or isinstance(v, Sections) or isinstance(v, Iframe):
        smg = SupportMethodGenerator()
        dict_[f"wait_until_{k}_visible"] = smg.wait_until_element_visible(v.base_by, v.base_selector)
        dict_[f"wait_until_{k}_invisible"] = smg.wait_until_element_invisible(v.base_by, v.base_selector)
        # Sectionsのときもfind_elementが使われるため、「少なくとも1つのelementがあるかどうか」が検査される
        dict_[f"has_{k}"] = smg.has_element(v.base_by, v.base_selector)
        dict_[f"has_no_{k}"] = smg.has_no_element(v.base_by, v.base_selector)

        if isinstance(v, Section):
          dict_[f"{k}_element"] = smg.element_element(v.base_by, v.base_selector)
        elif isinstance(v, Sections):
          dict_[f"{k}_elements"] = smg.element_elements(v.base_by, v.base_selector)
        elif isinstance(v, Iframe):
          dict_[f"{k}_element"] = smg.element_element(v.base_by, v.base_selector)


    return type.__new__(cls, name, bases, dict_)