import requests
from flask import Flask, request
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('amount')
parser.add_argument('input_currency')
parser.add_argument('output_currency')

#@app.route('/api/currency_converter', methods= ['GET', "POST"])
@app.route('/currency_converter/', methods= ["GET", "POST"])
def currency_converter(amount, input_currency, output_currency):
    input_currency = input_currency.upper().strip()
    output_currency = output_currency.upper().strip()

    if not input_currency:
        return {'Error': 'Input currency required'}, 400
    if not output_currency:
        return {'Error': 'Output currency required'}, 400
    if not amount:
        return {'Error': 'Invalid amount'}, 400

    amount = float(amount)

    if amount <= 0:
        return {'Bad request': 'Error 400'}

    url = 'http://data.fixer.io/api/latest?access_key=6ec43f7de51a0c404af0aedfc8cb1087'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return {'Error': "Remote API server error"}, response.status_code

    def currency_converter(currency_from, currency_to, amount):
        rate = response.json()['rates'][currency_from]
        amount_currency_from = amount/rate
        result = amount_currency_from * (response.json()['rates'][currency_to])
        return result 

    if input_currency and input_currency not in data['rates']:
        return {'Error': 'Invalid input currency'}, 400

    elif output_currency and output_currency not in data['rates']:
        return {'Error': 'Invalid output currency'}, 400

    else: 
            return {
            "Input": {
                'Currency 1': input_currency,
                'Currency 2': output_currency,
                "amount": amount,
            },
            "Output": {
                output_currency: currency_converter(input_currency, output_currency, amount),
            }
        }

class CurrencyConverter(Resource):
    def get(self):

        args = parser.parse_args()

        amount = args.get('amount')
        input_currency = args.get('input_currency')
        output_currency = args.get('output_currency')
        return currency_converter(amount, input_currency, output_currency)


api.add_resource(CurrencyConverter, '/currency_converter')

if __name__ == '__main__':
    app.run(debug=True)