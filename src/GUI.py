import sys
import os
import tkinter as tk
import datetime
import EditXML
import XMLObject
def initiate_GUI (xml_files):
    root = tk.Tk()
    root.title("XML Editor")

    # Create a dropdown menu
    xml_dropdown = tk.StringVar()
    xml_dropdown.set("Select an XML file")

    menu = tk.OptionMenu(root, xml_dropdown, *xml_files.keys(), command=lambda _: select_xml_data(xml_dropdown.get(), xml_files))
    menu.pack()

    # Create a frame to hold the XML data
    global xml_frame
    xml_frame = tk.Frame(root)
    xml_frame.pack()

    # List to hold XML edit widgets for cleanup
    global xml_edit_widgets
    xml_edit_widgets = []

    root.mainloop()
def select_xml_data(selected_key, XML_trees):
    xml_tree = XML_trees[selected_key]
    
    # Clear previous widgets
    for widget in xml_edit_widgets:
        widget.destroy()
    xml_edit_widgets.clear()
    display_XMLObject(xml_tree.getroot())

def display_XMLObject(XMLObject):
    #NOT IMPLEMENTED
    print("Displaying XMLObject:")
    print(XMLObject)

if __name__ == "__main__":
    
    root_directory = 'arcade-xml-generator'
    subdirectory = 'xml_files'
    directories = EditXML.list_directories()
    xml_files = EditXML.find_and_store_parameter_files_as_XMLObject(directories, "parameter")
    print(directories)
    print(xml_files)
    initiate_GUI(xml_files)