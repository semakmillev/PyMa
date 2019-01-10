# from xml import
# from main import text_xml

import xml.etree.ElementTree as ET

# text_xml = '<client><info><name>Semak</name></info><passport num="4608229176"/></client>'


text_xml = '<clients><client>Semak</client><client>Natasha</client></clients>'

xml = ET.fromstring(text_xml)
print(xml.findall('client'))
'''1
for el in list(xml): #xml.getchildren():
    if el.tag == 'info':
        print(list(el))
    print(el.tag, ':', el.text)
'''


class A:
    def __init__(self):
        self.n = None

a = A()
print (a.__dict__)


from lxml.builder import ElementMaker

E = ElementMaker(namespace="http://www.ya.ru")  # E(tag="a", "xmlns:ns"="{http://www.ya.ru}")
a = E(tag='a')
# E2 = ElementMaker(namespace="http://www.ya.ru")
b = E('b', '7')
a.append(b)

print(ET.tostring(a))
