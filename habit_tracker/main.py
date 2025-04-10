import requests
from datetime import datetime
USERNAME = 'oluwafemi09'
TOKEN = 'gfge3ui4r0967ujvfdk'
pixela_endpoint = 'https://pixe.la/v1/users'
GRAPH_ID = "graph1"
date = datetime.now().date().strftime("%Y%m%d")
print(date)

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)       ## For creating user
# print(response.text)   ## commented out because user has been created, and you can't create same  user twice

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}       # For security

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Posting a pixel
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_params = {
    'date': date,
    'quantity': "25.0",
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

pixel23_endpoint = f"{pixel_endpoint}/20250303"

pixel23_dict = {
    "quantity": "65"
}

response23 = requests.put(url=pixel23_endpoint, json=pixel23_dict, headers=headers)
print(response23.text)