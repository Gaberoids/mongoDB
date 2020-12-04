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


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error connecting database (from get_record try)")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc
    
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


# this block goes with the get_record (define doc as well)
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":  # do not update the key id
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                # if nothing to update, keep the same value
                if update_doc[k] == "":
                    update_doc[k] = v

        # check if everything worked properly
        try:
            coll.update_one(doc, {"$set": update_doc})
            # we should be able to use doc instead...
            # ...of $set (not sure what $set is5)
            print("")
            print("Document updated")
        except:
            print("Error accessing the database. (From Edit_record)")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete:\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database. from delete_record()")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")  # add a line after each option is choosen


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
