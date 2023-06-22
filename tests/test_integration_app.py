import requests

def test_app():
    url = "http://localhost:8080"
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)

    # Check if the expected content is present in the response
    expected_content = "<h1>Hello App</h1>"
    assert expected_content in response.text, "Expected content '{}' not found in response".format(expected_content)

    # Check if the response contains the logo image
    logo_url = "{}/static/logo.png".format(url)
    logo_response = requests.get(logo_url)
    assert logo_response.status_code == 200, "Failed to load logo image"

    # Check if the response contains the CSS file
    css_url = "{}/static/styles.css".format(url)
    css_response = requests.get(css_url)
    assert css_response.status_code == 200, "Failed to load CSS file"
