from xml.etree import ElementTree as ET

def parsexmlfile(filepath):
    i = 0
    xml = ET.parse(filepath)
    root = xml.getroot()
    for child in root: 
        print(root.attrib, child.attrib)
       
        




parsexmlfile('C:\\Users\\mfaber\\Documents\\GitHub\\jsonifyer\\modules\\testfile.xml')

