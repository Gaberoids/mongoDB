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


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

# insert many
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1984",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]
# coll.insert_many(new_docs)
# documents = coll.find()

# find everybody that the name is douglas
# documents = coll.find({"first": "douglas"})

# remove
# coll.remove({"first": "douglas"})
# documents = coll.find()

# update one
# coll.update_one({"nationality": "american", "$set": {"hair_color": "maroon"}})
# documents = coll.find({"nationality": "american"})

# update many
# coll.update_many({"nationality": "american", "$set": {"hair_color": "maroon"}})
# documents = coll.find({"nationality": "american"})


for doc in documents:
    print(doc)
