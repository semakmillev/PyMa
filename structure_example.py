import lxml.etree as ET #.ElementTree as ET

from api import xml_element, MarshallingObject, xml_list, ALONE
from api.functions import unmarshall, marshall

text_xml = '<client>' \
           '<name>Semak</name>' \
           '<phones>' \
           '<phone>+79091570147</phone>' \
           '<phone>+79031077025</phone>' \
           '</phones>' \
           '<passport num="4608229176"/>' \
           '</client>'


@xml_element("phone")
class Phone(MarshallingObject):
    def __init__(self):
        super().__init__()
        self._value = None


@xml_element("phones")
class Phones(MarshallingObject):
    def __init__(self):
        super().__init__()
        self._phoneList = PhoneList()

    def get_phones(self):
        return self._phoneList

    def set_phones(self, val):
        self._phoneList = val

    phoneList = property(get_phones, set_phones)


@xml_list(Phone)
class PhoneList(list, MarshallingObject):
    pass
    # def __init__(self):
    #    self.value = []


@xml_element("name")
class Name(MarshallingObject):
    pass
    # def __init__(self):
    #    self._value = None


@xml_element("passport")
class Passport(MarshallingObject):

    def __init__(self):
        super().__init__()
        self._value = None
        self.num = None


# a = Name(ET.fromstring('<test/>'))

@xml_element("client")
class Client(MarshallingObject):
    def __init__(self):
        super().__init__()
        self.__type__ = ALONE
        self._name = Name()
        self._passport = Passport()
        self._phones = Phones()
        self._value = None

    def get_name(self):
        return self._name

    def set_name(self, v):
        self._name = v

    def get_passport(self):
        return self._passport

    def set_passport(self, passport):
        self._passport = passport

    def get_phones(self):
        return self._phones

    def set_phones(self, phones):
        self._phones = phones

    passport = property(get_passport, set_passport)
    name = property(get_name, set_name)
    phones = property(get_phones, set_phones)


c = Client()
xml = ET.fromstring(text_xml)



    # print(m_el.tag, xml.findall(m_el.tag))



#print(c.passport.num)
#print(c.phones.phoneList)
unmarshall(c, xml)
a = marshall(c)

print(ET.tostring(a))


#  c.fill(ET.fromstring(text_xml))
# print(c._name.value)
