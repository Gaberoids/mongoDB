import os
import pymongo
if os.path.exists("env.py"):
    import env
    # if this if statement returns an error, ignore. this is fine

# The captalized variables below are standard practice for python
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    # Try is meant to teste the code within try. if there is any error,
    # except will be printed
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")  # add empty line on top of menu
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


#  This is the first loop to make  sure it work
# def main_loop():
#     while True:
#         option = show_menu()
#         if option == "1":
#             print("You have selected option 1")
#         if option == "2":
#             print("You have selected option 2")
#         if option == "3":
#             print("You have selected option 3")
#         if option == "4":
#             print("You have selected option 4")
#         if option == "5":
#             conn.close()
#             break
#         else:
#             print("Invalid option")
#         print("")  # add a line after each option is choosen


def add_record():
    print("")
    # the following are variables
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth >")
    gender = input("Enter gender >")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

# the following is a dictionary
    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
            print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")  # add a line after each option is choosen


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
