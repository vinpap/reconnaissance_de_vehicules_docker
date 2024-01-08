import requests

url_local = "http://0.0.0.0:8000/predict"
url_azure = "https://apivincent.azurewebsites.net/predict"


headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}
data = {
    "sepal_length": 10.0,
    "sepal_width": 10.0,
    "petal_length": 10.0,
    "petal_width": 10.0
}
print(requests.get(url_azure, headers=headers, json=data).text)