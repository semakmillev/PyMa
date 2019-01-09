def XmlElement(tag):
    def real_decorator(cls):
        def wrapper():
            cls.tag = tag
            obj = cls()
            # obj.fill(xml)
            return obj

        return wrapper

    return real_decorator


def XmlArray(child_cls):
    def real_decorator(cls):
        def wrapper():
            cls.tag = tag
            obj = cls()
            # obj.fill(xml)
            return obj

        return wrapper

    return real_decorator

class MarshallingObject(object):

    # def __init__(self):
    #    self.__value = None

    def get_element_list(self):
        return [self.__dict__[k] for k in self.__dict__ if isinstance(self.__dict__[k], MarshallingObject)]

    # def get_value(self):
    #    return self.__value

    def set_value(self, val):
        self.__value = val

    value = property(get_value, set_value)
