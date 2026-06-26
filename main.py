import json
import os

#local files
from categories import *
from common import *
from element import *
from pdfgen import *

status = 1
choice = -1


while status:
    print(r"""
  /$$$$$$  /$$       /$$             /$$    
 /$$__  $$| $$      |__/            | $$    
| $$  \__/| $$       /$$  /$$$$$$$ /$$$$$$  
| $$ /$$$$| $$      | $$ /$$_____/|_  $$_/  
| $$|_  $$| $$      | $$|  $$$$$$   | $$    
| $$  \ $$| $$      | $$ \____  $$  | $$ /$$
|  $$$$$$/| $$$$$$$$| $$ /$$$$$$$/  |  $$$$/
 \______/ |________/|__/|_______/    \___/  
    """)

    print("\nPlease choose one of these options:");
    print("\n\n1) Category management");
    print("2) Element (list)  management");
    print("3) Generate the final PDF")
    print("0) Quit");
    
    choice = input("\nInput: ");
    if not(choice.isdigit()):
        print("Invalid input!");
        check_clear();
        continue;
    ich = int(choice) #int choice -> ich

    match ich:
        case 1:
            management_category();
            continue;
        case 2:
            management_element();
            continue;
        case 3:
            pdf_generation_all();
            continue;
        case 0:
            status = 0;
        case _:
            print("Number out of bound!");
    check_clear();
