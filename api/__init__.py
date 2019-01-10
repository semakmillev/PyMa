ALONE = 0
SEQUENCE = 1


def xml_element(tag, namespace=None):
    def real_decorator(cls):
        def wrapper(a=None):
            # print(a, tag)
            cls.__tag__ = tag
            cls.__namespace__ = namespace
            cls.__type__ = ALONE
            obj = cls()
            # obj.fill(xml)
            return obj

        return wrapper

    return real_decorator


def xml_list(child_cls):
    def real_decorator(cls):
        def wrapper():
            # cls.tag = None
            child_el = child_cls()
            cls.__child_tag__ = child_el.tag
            cls.__child_namespace__ = child_el.namespace
            cls.__child_cls__ = child_cls
            del child_el
            cls.__type__ = SEQUENCE
            obj = cls()
            # obj.fill(xml)
            return obj

        return wrapper

    return real_decorator


class MarshallingObject(object):

    def __init__(self):
        self._value = None

    def get_element_list(self):
        return [self.__dict__[k] for k in self.__dict__ if isinstance(self.__dict__[k], MarshallingObject)]

    def get_attribute_list(self):
        return {k: self.__dict__[k] for k in self.__dict__ if
                not isinstance(self.__dict__[k], MarshallingObject) and not k.startswith(
                    '_') and k != 'tag' and k != 'namespace'}
        #

    def get_value(self):
        return "" if self._value is None else self._value

    def set_value(self, val):
        self._value = val

    def set_attributes(self, xml):
        for attribute_name in xml.attrib:
            self.__dict__[attribute_name] = xml.attrib[attribute_name]

    def get_tag(self):
        return self.__tag__

    def get_namespace(self):
        return self.__namespace__

    def get_type(self):
        return self.__type__

    def get_child_tag(self):
        return self.__child_tag__

    def get_child_cls(self):
        return self.__child_cls__

    def get_child_namespace(self):
        return self.__child_namespace__


    value = property(get_value, set_value)
    tag = property(get_tag)
    namespace = property(get_namespace)
    type = property(get_type)
    child_tag = property(get_child_tag)
    child_cls = property(get_child_cls)
    child_namespace = property(get_child_namespace)