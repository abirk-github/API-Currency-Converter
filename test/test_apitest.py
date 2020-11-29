import requests
import json
from test_api import test_currency_converter_api, get_header

url = 'http://127.0.0.1:5000/currency_converter'

# Testing url status code
def test_api_get():
    resp = requests.get(url)
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)

# Testing header, i.e. Content-Length specifically
def test_validate_header():
    resp = requests.get(url)
    header = get_header()
    if header == 162:
        return "OK"
    else:
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)


def main(amount, input_currency, output_currency):
    input_currency = 'NOK'
    output_currency = 'EUR'
    amount = int(100)
    resp = test_currency_converter_api(amount, input_currency, output_currency)
    print(json.dumps(resp if isinstance(resp, dict) else resp[0], indent=4))

input_currency = 'NOK'
output_currency = 'EUR'
amount = int(100)

if __name__ == "__main__":
    main(amount, input_currency, output_currency)