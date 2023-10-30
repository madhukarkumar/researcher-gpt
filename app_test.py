import requests

print (
    requests.post(
        "http://0.0.0.0:10000",
        json={
            "query": "Company - CollabNow with the website address https://collabnow.ai"
        }
    ).json()
)