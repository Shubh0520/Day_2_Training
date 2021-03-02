import xml.etree.ElementTree as element_tree

xml_parse = element_tree.parse("E:/Shubham_Work_Docs/25-02-2021/test_file.xml")
xml_root = xml_parse.getroot()
print(xml_root.tag)
print(xml_root.attrib)
items = []

# Accessing children tags
for child_elements in xml_root:
    print(child_elements.tag, child_elements.attrib)

print(child_elements[0].text)
