import requests

def test_app():
    url = "http://localhost:8080"
    response = requests.get(url)

    assert response.status_code == 200
    assert "<h1>Hello App</h1>" in response.text
