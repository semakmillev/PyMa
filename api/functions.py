from lxml.builder import ElementMaker

from api import ALONE


def unmarshall(cl, xml):
    cl.value = xml.text  # if cl.value is None else cl.value
    for m_el in (cl.get_element_list()):
        if m_el.type == ALONE:
            m_el_xml = xml.findall(m_el.tag)[0]
            m_el.value = xml.findall(m_el.tag)[0].text  # if m_el.value is None else m_el.value
            m_el.set_attributes(m_el_xml)

            new_xml = xml.xpath(m_el.tag) if m_el.namespace is None else xml.xpath('ns:' + m_el.tag,
                                                                                   namespaces={'ns': m_el.namespace})
            if len(new_xml) > 0:
                unmarshall(m_el, new_xml[0])
        else:
            searching_tag = m_el.child_tag
            searching_namespace = m_el.child_namespace
            new_xml = xml.xpath(searching_tag) if searching_namespace is None else xml.xpath('ns:' + searching_tag,
                                                                                   namespaces={'ns': m_el.namespace})
            for el in new_xml:
                new_el = m_el.child_cls()
                unmarshall(new_el, el)
                m_el.append(new_el)
    return cl


def marshall(cl):
    E = ElementMaker(namespace=cl.namespace)
    xml = E(cl.tag, cl.value)
    for k in cl.get_attribute_list():
        xml.attrib[k] = str(cl.get_attribute_list()[k])
    for m_el in (cl.get_element_list()):
        if m_el.type == ALONE:
            child_xml = marshall(m_el)
            xml.append(child_xml)
        else:
            # searching_tag = m_el.child_tag
            # print (m_el.child_tag)
            for el in m_el:
                # print(el.tag)
                child_xml = marshall(el)
                xml.append(child_xml)
    return xml
