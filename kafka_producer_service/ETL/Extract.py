import requests


def create_response_dict(url: str="https://randomuser.me/api/?results=1") -> dict:
    
    response = requests.get(url)
    data = response.json()
    results = data["results"][0]

    return results
