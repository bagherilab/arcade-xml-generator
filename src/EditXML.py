import tkinter as tk
import xml.etree.ElementTree as ET
import sys
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))
relative_path_to_XMLObject = os.path.normpath(os.path.join(current_script_path, '../../src/'))
sys.path.append(relative_path_to_XMLObject)
from XMLObject import XMLObject


def list_directories():
    directoryList =[]
    directoryTuples = os.walk(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    for x in directoryTuples:
        directoryList.append(x[0])
    return directoryList

def find_and_store_parameter_files_as_XMLObject(directories, keyword):
    xml_files = {}
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.endswith(".xml") and keyword in filename:
                file_path = os.path.join(directory, filename)
                key = "_".join([os.path.basename(directory.rstrip('/')), os.path.splitext(filename)[0]])#drops extension
                xml_files[key] = load_xml(file_path)
    return xml_files

def load_xml(file_name):
    tree = ET.parse(file_name)
    root_element = tree.getroot()
    return element_to_xml_object(root_element)

def element_to_xml_object(element, parent=None):
    xml_object = XMLObject(
        name=element.tag,
        attribute_dict=element.attrib,
        parent=parent
    )
    for child_element in element:
        child_xml_object = element_to_xml_object(child_element, parent=xml_object)
        xml_object.children.append(child_xml_object)
    return xml_object

    
# list = [

# ]

# def create_new_population():
#     raise error NotImplemented

# def modify_population():