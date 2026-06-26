import json
import os
from datetime import date

#local files
from common import *

def management_category():
    check_clear();

    status = 1

    while status:
        print("You are now in the category management section\nPlease choose an option:");
        print("\n\n1)Add a new categories");
        print("2)Remove a categorie");
        print("3)List all categories");
        print("4)Generate default categories (This will delete the current categories and elements)");
        print("5)Back up database by date");
        print("0)Return");

        choice = input("\nInput: ");
        if not(choice.isdigit()):
            print("Invalid input!");
            check_clear();
            continue;
        ich = int(choice)

        match ich:
            case 1:
                add_to_category();
            case 2:
                del_from_category();
            case 3:
                list_category();
            case 4:
                gen_default_category();
            case 5:
                back_up_category();
            case 0:
                status = 0;
            case _:
                print("Number out of bound!");
        check_clear();


def del_from_category():
    found = 0
    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    list_category()
    name = input("\nEnter the category name to delete: ");
    
    #Error management
    for categ in db:
        if name == categ:
            found = 1
    
    if found == 1:
        del db[name]
        with open(DEF_DB_NAME, mode="w", encoding="utf-8") as db_f:
            json.dump(db, db_f);

        print("[INFO]: db updated!");
    else:
        print("Category name not found in the db! Please try again.");
     

def back_up_category():
    today = date.today();
    name = input("Input the back up name(leave empty for date only):");
    if name != "":
        name += "-";name +=str(today);name += ".json"
    else:
        name += str(today);name+=".json";
    print(name);
    
    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);
    
    with open(name, mode="w", encoding="utf-8") as f:
        json.dump(db, f, indent=2);

    print("[INFO]: db backed-up!");


def add_to_category():
    inp = input("\nEnter the name of the new category: "); 
    inp = inp.replace(" ","");
    if inp == "":
        print("The space or void category is not allowed, please choose a name.")
    else:
        with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
            db = json.load(db_f);

        add_category = {inp: []}
        db.update(add_category);
 
        with open(DEF_DB_NAME, mode="w", encoding="utf-8") as db_f:
            json.dump(db, db_f);

        print("[INFO]: Element added to the db!");

def gen_default_category():
    def_category = {"Divers": []}

    with open(DEF_DB_NAME, mode="w", encoding="utf-8") as db_f:
        json.dump(def_category, db_f);

    print("[INFO]: Generated default category db!");

def list_category():
    with open(DEF_DB_NAME, mode="r", encoding="utf-8") as db_f:
        db = json.load(db_f);

    catg_num = len(db);
    print("There are", catg_num, " categories:\n");

    j = 0;
    for i in db:
        print(j,"-",i);
        j = j + 1;


