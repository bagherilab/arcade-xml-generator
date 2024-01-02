import sys
import os
import tkinter as tk
from tkinter import ttk
import datetime
import EditXML
import XMLObject


def initiate_GUI(xml_files):
    root = tk.Tk()
    root.title("XML Editor")
    root.geometry("400x300")
    #Create a separator 
    separator = ttk.Separator(root, orient='vertical')
    separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)

    # Create a frame to hold the XML data
    xml_frame = tk.Frame(root)
    xml_frame.pack()

    # List to hold XML edit widgets for cleanup
    xml_edit_widgets = []

    # Additional menu with Exit and Save buttons
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Save", command=lambda: save_action())
    file_menu.add_separator()
    file_menu.add_command(label="Command Options", command=lambda: command_action(root))

    # Create a dropdown menu
    xml_dropdown = tk.StringVar()
    xml_dropdown.set("Select an XML file")

    option_menu = tk.OptionMenu(root, xml_dropdown, *xml_files.keys(), command=lambda selected_key: select_xml_data(selected_key, xml_files, xml_frame))
    option_menu.place(relx=0.5, rely=0.1, relheight=0.10, relwidth=0.4)

    root.mainloop()
def save_action():
    print("Save action executed")

def command_action(root):
    #root.destroy() 
    print("Checkboxes for commands")

def select_xml_data(selected_key, XML_trees, xml_frame):
    xml_object = XML_trees[selected_key]
    display_XMLObject(xml_object, xml_frame)

def display_XMLObject(xml_object, frame, indent=0):
    # Create a button for the current XmlObject
    button_text = f"{xml_object.tag} ({len(xml_object.children)})"  # Example button text
    button = tk.Button(frame, text=button_text, command=lambda: on_button_click(xml_object))

    # Adjust the row and column parameters
    button.grid(row=indent, column=2, sticky="w", padx=indent * 20)  # Column is set to 2

    # Recursively display children
    for i, child in enumerate(xml_object.children):
        display_XMLObject(child, frame, indent + 1)

def on_button_click(xml_object):
    # Example function to handle button click
    print(f"Button clicked for {xml_object.tag}")

if __name__ == "__main__":
    root_directory = 'arcade-xml-generator'
    subdirectory = 'xml_files'
    directories = EditXML.list_directories()
    xml_object = None
    xml_files = EditXML.find_and_store_parameter_files_as_XMLObject(directories, "parameter")
    initiate_GUI(xml_files)