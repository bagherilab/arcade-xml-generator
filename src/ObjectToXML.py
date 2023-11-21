import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, order=True)
class xml_object:
    name: str
    self_closing: bool = False #True if < tag />
    attribute_dict: dict = field(default_factory=dict)
    children: List['xml_object'] = field(default_factory=list)
    parent: 'xml_object' = None  # Added parent attribute


    def __post_init__(self):
        # Set parent attribute for each child
        for child in self.children:
            child.parent = self

    def convert_to_element_tree(self):
        element = ET.Element(self.name, self.attribute_dict)
        for child in self.children:
            child_element = child.convert_to_element_tree()
            element.append(child_element)
        return element
    def save_XML(self, file_name):
        tree = ET.ElementTree(self.convert_to_element_tree())
        print(type(tree))
        ET.indent(tree, space="\t", level=0)
        tree.write(file_name, encoding="utf-8")
        



