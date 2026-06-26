import os

DEF_DB_NAME = "db.json" #Default db file name

def check_clear():
    input("\nPress Enter to continue");
    os.system('cls' if os.name == 'nt' else 'clear');
