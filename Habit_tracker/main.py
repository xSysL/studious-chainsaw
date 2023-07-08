import requests

USERNAME = "subha"
TOKEN = "tokenforpixelabysubha"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/subha/graphs"

graph_config = {
    "id": "graph2",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Kolkata",


}

header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=graph_endpoint, json=graph_config, headers=header)
print(response.text)
