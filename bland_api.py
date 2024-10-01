import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()



# Headers
headers = {
   'Authorization': os.getenv("BLAND_AUTH")
}

# Data
data = {
  "phone_number": "+96899186488",
  "from": None,
  "task": "You are a salesman for TechShoe, a company which makes shoes. You are trying to convince the customer to buy the latest AI-Assisted shoes for long walks.",
  "model": "enhanced",
  "language": "en",
  "voice": "nat",
  "voice_settings": {},
  "local_dialing": False,
  "max_duration": 12,
  "answered_by_enabled": False,
  "wait_for_greeting": False,
  "record": True,
  "amd": False,
  "interruption_threshold": 100,
  "voicemail_message": None,
  "temperature": None,
  "transfer_list": {},
  "metadata": {},
  "pronunciation_guide": [],
  "start_time": None,
  "request_data": {},
  "tools": [],
  "webhook": None,
  "calendly": {}
}

# API request 
requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)