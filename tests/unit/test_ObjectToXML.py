import unittest
import sys
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))
relative_path_to_xml_object = os.path.normpath(os.path.join(current_script_path, '../../src/'))
sys.path.append(relative_path_to_xml_object)
from ObjectToXML import xml_object

output ="""
<population id="C" init="100" class="cancer_stem">
                    <population.parameter id="DIVISION_POTENTIAL" value="3" />
                    <population.parameter id="COMPRESSION_TOLERANCE" value="8.7" />
                    <population.parameter id="SYNTHESIS_DURATION" module="proliferation" value="10" />
                    <population.parameter id="meta_pref" scale="1.5" />
                    <population.parameter id="migra_threshold" scale="0.5" />
                    <population.parameter id="CELL_VOLUME_MEAN" scale="0.58" />
                    <population.process id="METABOLISM" version="complex" />
                    <population.process id="SIGNALING" version="complex" />
                    <population.parameter id="MIGRA_PROB" process="signaling" value="0" />
                    <population.process id="SIGNALING" version="complex" />
                    <population.parameter id="DIVISION_POTENTIAL" value="20" />
                    <population.parameter id="MIGRATION_RATE" module="migration" value="2" />
                </population>
"""

class TestObjectCreation(unittest.TestCase):
    """Test the class xml_object creation method"""

    def setUp_nochildren_noparent(self):
        self.population_simple = xml_object(name = 'population', attribute_dict = {'id':'C', 'init':'100', 'class':'cancer'}, self_closing = False)
    def setUp_children(self):
        """
        populations
        |-population
            |-population parameter
            |-population process
            |-population process
        """
        self.tree_with_children = xml_object(name = 'populations', self_closing = False)
        self.tree_with_children.children.append(xml_object(name = 'population', attribute_dict = {'id':'C', 'init':'100', 'class':'cancer'}, self_closing = False))
        self.tree_with_children.children[0].children.append(xml_object(name = 'population.parameter', attribute_dict = {'id':'DIVISION_POTENTIAL', 'value':'3'}, self_closing = True))
        self.tree_with_children.children[0].children.append(xml_object(name = 'population.process', attribute_dict = {'id':'METABOLISM', 'version':'complex'}, self_closing = True))
        self.tree_with_children.children[0].children.append(xml_object(name = 'population.process', attribute_dict = {'id':'SIGNALING', 'version':'complex'}, self_closing = True) )
        
        print(self)
        print("olaf")
        print(self)

    def test_to_convert_to_element_tree_simple(self):
        self.setUp_nochildren_noparent()
        root_element = xml_object.convert_to_element_tree(self.population_simple)
        self.assertEqual(root_element.tag, 'population')
        self.assertEqual(root_element.attrib, {'id':'C', 'init':'100', 'class':'cancer'})
        xml_object.save_XML(self.population_simple, "simpleTest.xml")  

    def test_to_convert_to_element_tree_children(self):
        self.setUp_children()
        root_element = xml_object.convert_to_element_tree(self.tree_with_children)
        
        self.assertEqual(root_element.tag, 'populations')
        self.assertEqual(root_element[0].tag, 'population')
        self.assertEqual(root_element[0].attrib, {'id':'C', 'init':'100', 'class':'cancer'})

        children_elements = list(root_element[0])
        
        self.assertEqual(children_elements[0].tag, 'population.parameter')
        self.assertEqual(children_elements[0].attrib, {'id':'DIVISION_POTENTIAL', 'value':'3'})

        self.assertEqual(children_elements[1].tag, 'population.process')
        self.assertEqual(children_elements[1].attrib, {'id':'METABOLISM', 'version':'complex'})
        
        self.assertEqual(children_elements[2].tag, 'population.process')
        self.assertEqual(children_elements[2].attrib, {'id':'SIGNALING', 'version':'complex'})

        xml_object.save_XML(self.tree_with_children, "childrenTest.xml") 



if __name__ == "__main__":
    unittest.main()
