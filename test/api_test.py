import requests
import json 

def test_post_headers_body_json():
    url1 = 'http://data.fixer.io/api/latest?access_key=6ec43f7de51a0c404af0aedfc8cb1087'
    url2 = 'http://127.0.0.1:5000/'
    url_original = "https://reqres.in/api/users?page=2"

    headers = {'Content-Type': 'application/json'}

    payload = {'key1': 1, 'key2': 'value2'}

    response = requests.post(url2, headers=headers, data=json.dumps(payload, indent=4))

    assert response.status_code == 200
    response_body = response.json()
    assert response_body['url'] == url2

    print(response.text)

