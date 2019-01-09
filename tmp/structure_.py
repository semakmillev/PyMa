import xml.etree.ElementTree as ET

text_xml = '<client><name>Semak</name><passport num="4608229176"/></client>'


def child_decorator(tag):
    def real_decorator(cls):
        def wrapper():
            # funny_stuff()
            # x = v + argument
            # something_with_argument(argument)
            # result = function(x)
            # more_funny_stuff()
            cls.tag = tag
            obj = cls()
            # obj.fill(xml)
            return obj

        return wrapper

    return real_decorator

    '''
    def real_decorator(func):
        #print (tag)
        def wrapper(cls, *args):
            print (args, cur_cls)
            # funny_stuff()
            # x = v + argument
            # something_with_argument(argument)
            # result = function(x)
            # more_funny_stuff()
            cls.tag = tag

            # xml.findall(tag)[0]
            obj = cur_cls()
            # obj.fill(xml)
            return func(obj)

        return wrapper

    return real_decorator
    '''


class Marshaller(object):
    def get_element_list(self):
        return [self.__dict__[k] for k in self.__dict__ if isinstance(self.__dict__[k], Marshaller)]


@child_decorator("name")
class Name(Marshaller):
    def __init__(self):
        self._value = None

    def set_attributes(self, xml):
        for attribute_name in xml.attrib:
            self.__dict__[attribute_name] = xml.attrib[attribute_name]

    def get_value(self):
        return self._value

    def set_value(self, val):
        self._value = val

    value = property(get_value, set_value)


@child_decorator("passport")
class Passport(Marshaller):
    def __init__(self):
        self._value = None
        self.num = None

    def set_attributes(self, xml):
        for attribute_name in xml.attrib:
            self.__dict__[attribute_name] = xml.attrib[attribute_name]

    def get_value(self):
        return self._value

    def set_value(self, val):
        self._value = val

    value = property(get_value, set_value)


# a = Name(ET.fromstring('<test/>'))


class Client(Marshaller):
    def __init__(self):
        self._name = Name()
        self._passport = Passport()
        self._value = None

    def fill(self, xml):
        self.name = xml
        # self._value = xml
        # l = [self.__dict__[k] for k in self.__dict__ if isinstance(self.__dict__[k], Marshaller)]
        i = 0
        # for f in list(xml):

        # fET.fromstring(text_xml)or el in list(xml):  # xml.getchildren():
        #    l[i] = type(l[i])(el)
        #    i += 1
        # print(el.tag, ':', el.text)
        pass

    def get_name(self):
        return self._name

    def set_name(self, v):
        self._name = v

    def get_passport(self):
        return self._passport

    def set_passport(self, passport):
        self._passport = passport

    def get_value(self):
        return self._value

    def set_value(self, val):
        self._value = val

    passport = property(get_passport, set_passport)
    name = property(get_name, set_name)
    value = property(get_value, set_value)


c = Client()
xml = ET.fromstring(text_xml)


def unmarshall(cl, xml):
    cl.value = xml.text
    for m_el in (cl.get_element_list()):
        m_el_xml = xml.findall(m_el.tag)[0]
        m_el.value = xml.findall(m_el.tag)[0].text
        m_el.set_attributes(m_el_xml)
        unmarshall(m_el, xml.findall(m_el.tag)[0])
    return cl
    # print(m_el.tag, xml.findall(m_el.tag))


unmarshall(c, xml)
print (c.passport.nu)
# c.fill(ET.fromstring(text_xml))
# print(c._name.value)
