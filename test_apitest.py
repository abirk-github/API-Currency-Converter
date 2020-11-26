import requests

url1 = 'http://data.fixer.io/api/latest?access_key=6ec43f7de51a0c404af0aedfc8cb1087'
url2 = 'http://127.0.0.1:5000/currency_converter'
url_original = "https://reqres.in/api/users?page=2"

def test_api_get():
    resp = requests.get(url2)
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 4:
            assert record['first_name'] == "Eve",\
                "Data not matched! Expected : Eve, but found : " + str(record['first_name'])
            assert record['last_name'] == "Holt",\
                "Data not matched! Expected : Holt, but found : " + str(record['last_name'])

def test_api_post():
    data = {'name': 'John',
            'job': 'QA'}
    resp = requests.post(url=url2, data=data)
    data = resp.json()
    assert (resp.status_code == 201), "Status code is not 201. Rather found : "\
        + str(resp.status_code)
    assert data['name'] == "John", "User created with wrong name. \
        Expected : John, but found : " + str(data['name'])
    assert data['job'] == "QA", "User created with wrong job. \
        Expected : QA, but found : " + str(data['name'])