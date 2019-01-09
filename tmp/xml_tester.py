# from xml import
#from main import text_xml

import xml.etree.ElementTree as ET

text_xml = '<client><info><name>Semak</name></info><passport num="4608229176"/></client>'
xml = ET.fromstring(text_xml)
print(xml.findall('passport')[0].attrib)
'''1
for el in list(xml): #xml.getchildren():
    if el.tag == 'info':
        print(list(el))
    print(el.tag, ':', el.text)
'''





