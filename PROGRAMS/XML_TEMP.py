import xml.etree.ElementTree as ET

# GET XML FILE DATA
stream = open('sample.xml','r')

# PARSE THE DATA INTO ElementTree OBJECT
xml = ET.parse(stream)

# GET THE 'root' ELEMENT OBJECT FROM THE ElementTree
root = xml.getroot()

# ITERATE THROUGH EACH ITEM OF THE root  ELEMENT
for e in root:
	print(ET.tostring(e))
	print("")
	print(e.get("id"))



