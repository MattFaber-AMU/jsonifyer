from xml.etree import ElementTree as ET

def parse_xml(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
  
    for child in root: 
        print(child.tag, child.attrib)
    
parse_xml('C:\\Users\\mfaber\\Documents\\GitHub\\jsonifyer\\modules\\testfile.xml')

