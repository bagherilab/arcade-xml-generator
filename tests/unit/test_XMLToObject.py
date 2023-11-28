import sys
import os
import unittest
import xml.etree.ElementTree as ET

current_script_path = os.path.dirname(os.path.abspath(__file__))
relative_path_to_XMLObject = os.path.normpath(os.path.join(current_script_path, '../../src/'))
sys.path.append(relative_path_to_XMLObject)
from XMLObject import XMLObject
import EditXML 

def compare_xml_files(file1, file2):
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # Get the root elements
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # Compare the XML content
    return ET.tostring(root1) == ET.tostring(root2)
class TestXMLToObject(unittest.TestCase):
    def test_convert_xml_to_object(self):
       tree_with_children = EditXML.load_xml('childrenTest.xml')
       XMLObject.save_XML(tree_with_children, 'childrenTest_converted.xml') 
       self.assertTrue(compare_xml_files('childrenTest.xml', 'childrenTest_converted.xml'))

    #def check_load_xml_selection(self):
        # intialize GUI
        # Check if XML selection == loaded XML
if __name__ == "__main__":
    unittest.main()
