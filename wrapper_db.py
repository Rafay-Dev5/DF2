from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBWrapper:
    def __init__(self, db_name="study_db", host="localhost", port=27017):
        # Connect to MongoDB
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        
        # Define collections
        self.user_collection = self.db["users"]
        self.victim_collection = self.db["victims"]
        
        # Create indexes for efficient querying and scaling
        self.user_collection.create_index("user_number", unique=True)
        self.user_collection.create_index("region")
        self.user_collection.create_index("category")
        
        self.victim_collection.create_index("category")
        
    # Create a new user
    def create_user(self, user_number, region, category):
        user_data = {
            "user_number": user_number,
            "region": region,
            "category": category
        }
        return self.user_collection.insert_one(user_data).inserted_id

    # Create a new victim
    def create_victim(self, category, persona):
        victim_data = {
            "category": category,
            "persona": persona
        }
        return self.victim_collection.insert_one(victim_data).inserted_id
    
    # Read a user by user_number
    def get_user(self, user_number):
        return self.user_collection.find_one({"user_number": user_number})
    
    # Read a victim by id
    def get_victim(self, victim_id):
        return self.victim_collection.find_one({"_id": ObjectId(victim_id)})

    # Update a user's region or category
    def update_user(self, user_number, updated_data):
        return self.user_collection.update_one(
            {"user_number": user_number}, 
            {"$set": updated_data}
        )

    # Update a victim's persona or category
    def update_victim(self, victim_id, updated_data):
        return self.victim_collection.update_one(
            {"_id": ObjectId(victim_id)}, 
            {"$set": updated_data}
        )

    # Delete a user by user_number
    def delete_user(self, user_number):
        return self.user_collection.delete_one({"user_number": user_number})
    
    # Delete a victim by id
    def delete_victim(self, victim_id):
        return self.victim_collection.delete_one({"_id": ObjectId(victim_id)})

    # Custom query for large-scale filtering
    def get_users_by_region_category(self, region=None, category=None):
        query = {}
        if region:
            query["region"] = region
        if category:
            query["category"] = category
        return list(self.user_collection.find(query))

    def get_victims_by_category(self, category=None):
        query = {}
        if category:
            query["category"] = category
        return list(self.victim_collection.find(query))
