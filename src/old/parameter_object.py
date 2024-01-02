
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, order=True)
class parameter_object:
    wrapper_register_or_given_id: str = None
    class_wrapper: str = None
    subcategory: str = None #e.g. migration module
    modified = False
    tag: str
    attribute_dict: dict = field(default_factory=dict)
    description: {} = None #found in some parameter attributes


@dataclass(frozen=True, order=True)
class parameters:
    set: parameter_object
    series: [parameter_object]
    model_type: str #no options given in xml 
    model_type_parameter: [parameter_object] = None #needs wrapper based on file name

    agents: parameter_object(tag = "agents", attribute_dict=None)
    agents: parameter_object(tag = "populations", attribute_dict=None)
    population: parameter_object #no options given in xml
    population_parameters: [parameter_object]
    
    layers: [parameter_object] #Needs environment, layers, and ID wrapper
    actions: [parameter_object]
    components: [parameter_object]

    set.name = 

# AUTOADDS EQUIVALENT:
# def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
#     self.name = name
#     self.unit_price = unit_price
#     self.quantity_on_hand = quantity_on_hand
        
