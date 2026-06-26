#Standard json element composition
#{
# "Divers": [
#   {
#     "name": "",
#     "brand": "",
#     "ref": "",
#     "qnt": 0
#   }
# ]
#}
import json

from common import *
from categories import list_category

def management_element():
    check_clear();
    status = 1;
    category = "";

    while status:
        print("\nChosen category: \n", category);
        print("\nYou are now in the elemnent management section\nPlease choose an option:");
        print("\n\n1) Choose a category");
        print("2) Add one element to category");
        print("3) List all elements");
        print("4) Add multiple elements");
        print("5) Remove one element");
        print("0) Return");

        choice = input("\nInput: ");
        if not choice.isdigit():
            print("Invalid input!");
            check_clear();
            continue;
        #ADD CATEGORY CHECK TO ALL COMING FUNCTIONS
        ich = int(choice);

        match ich:
            case 1:
                category = choose_category();
            case 2:
                add_one_element(category);
            case 3:
                list_element(category);
            case 4:
                add_mult_element(category);
            case 5:
                remove_one_element(category);
            case 0:
                status = 0;
            case _:
                print("Number out of bound !");
        check_clear();

def remove_one_element(category):

    state = list_element(category);
    if state == 0:
        return None;

    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    choice = input("\nPlease enter the index of the element to remove: ");
    if not choice.isdigit():
        print("Invalid input!, try again!");
        return None;
    ich = int(choice);

    if ich > len(db[category]) - 1 or ich < 0:
        print("Input out of bound! try again!");
        return None;

    db[category].pop(ich);
    with open(DEF_DB_NAME, mode="w", encoding="utf-8") as f:
        json.dump(db, f);
    print("Element removed!");

def add_mult_element(category):
    choice = 1
    while(choice):
        ch = input("\nAdd new element ?([Enter] for yes, 0 for no): ");
        match ch:
            case "":
                add_one_element(category);
            case "0":
                choice = 0;
            case _:
                print("Invalid input");
                continue;

def list_element(category):
    #ADDING RETURN 0 OR 1 FOR VERIFICATION OF CATEGORY FOR THE remove_one_element(category); FUNCTION
    if category == "":
        print("No category is chosen! Choose a cotegory then try again!");
        return 0;

    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    print("Listing elements of the category:", category, "\n");

    for i in range(len(db[category])):
        print(i,"-",db[category][i]["name"],"|",db[category][i]["brand"],"|",db[category][i]["ref"],"|",db[category][i]["qnt"]);
    return 1;

def add_one_element(category):
    if category == "":
        print("No category is chosen! Choose a cotegory then try again!");
        return None

    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);
    print("\nPlease enter the item info\n");
    name = input("Please enter the name: ");
    brand = input("brand: ");
    ref = input("reference: ");
    qnt = input("quantity: ");
    if not(qnt.isdigit()):
        print("Invalid input!");
        return None;
    new_elem = fill_element(name, brand, ref, int(qnt));
    db[category].append(new_elem);

    with open(DEF_DB_NAME, mode="w", encoding="utf-8") as f:
        json.dump(db, f);
    print("\n[INFO]: Item added\n");

def choose_category():
    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    list_category();
    choice = input("\nPlease choose a category [index]: ");

    if not choice.isdigit():
        print("Invalid input!");
        return ""
    ich = int(choice);
    
    if ich > len(db) or ich < 0:
        print("Invalid index! Please try again.");
        return ""
    else:
        i = 0;
        keys = [];
        for string in db:
            keys.append(string);
            i += 1;
        name = keys[ich];
        print("[INFO]: Category found !")
        return name;

def fill_element(name, brand, ref, qnt):
    dic = {"name": name, "brand": brand, "ref": ref, "qnt": qnt};
    return dic
