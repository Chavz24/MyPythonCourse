# A_Main.py

import AA_Package_example.A_Module
from AA_Package_example.C_SubPackage import C_Module

for person in C_Module.people:
    AA_Package_example.A_Module.greet(person)
    

