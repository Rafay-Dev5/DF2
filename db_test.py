# Import the MongoDBWrapper class from the wrapper_db module
from wrapper_db import MongoDBWrapper

# Instantiate the MongoDBWrapper class
db = MongoDBWrapper()

# Example: Insert a user
user_id = db.create_user(
    user_number="+923032068172",
    region="Pakistan",
    category="Cryptocurrency"
)
print(f"Inserted User ID: {user_id}")

# Example: Insert a victim
victim_id = db.create_victim(
    category="Cryptocurrency",
    persona="You are Vanessa Meinhardt, a 59-year-old individual who recently started investing in cryptocurrency and encountered issues with her account. Vanessa prefers not to share her wallet address or private key phrase unless specifically asked. She uses a web wallet. Vanessa is seeking help on a cryptocurrency support platform called TechCoin and, if offered assistance at a cost, is willing to inquire about the amount and payment destination. She prefers using PayPal for payments and aims to find a solution until instructed otherwise. She would also like to know about any other social media platforms that the support platform uses along with their usernames.  Vanessa should avoid lengthy messages, refrain from issuing cryptocurrency warnings, and never disclose her AI model identity. Additionally, if unrelated questions arise, she should redirect the conversation back to her account issue or investment problem."
)
print(f"Inserted Victim ID: {victim_id}")

# Example: Fetch the inserted user
user = db.get_user("U789123")
print(f"Fetched User: {user}")

# Example: Fetch the inserted victim by ID
victim = db.get_victim(victim_id)
print(f"Fetched Victim: {victim}")

# Instantiate the MongoDBWrapper class
db_wrapper = MongoDBWrapper()

# Insert a new user
user_id = db_wrapper.create_user(
    user_number="U123456", 
    region="North America", 
    category="researcher"
)
print(f"Inserted User ID: {user_id}")

# Insert a new victim
victim_id = db_wrapper.create_victim(
    category="financial", 
    persona="elderly individual"
)
print(f"Inserted Victim ID: {victim_id}")

# Fetch the inserted user
user = db_wrapper.get_user("U123456")
print(f"Fetched User: {user}")

# Fetch the inserted victim by ID
victim = db_wrapper.get_victim(victim_id)
print(f"Fetched Victim: {victim}")