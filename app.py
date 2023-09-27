from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/stock/<string:symbol>')
def get_stock_data(symbol):
    api_key = 'EJSN5Z5T92ZYHU05'
    api_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    try:
        response = requests.get(api_url)
        data = response.json()

        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            stock_info = {
                'symbol': stock_data['01. symbol'],
                'open': float(stock_data['02. open']),
                'high': float(stock_data['03. high']),
                'low': float(stock_data['04. low']),
                'price': float(stock_data['05. price']),
                'volume': int(stock_data['06. volume']),
                'latest_trading_day': stock_data['07. latest trading day'],
                'previous_close': float(stock_data['08. previous close']),
                'change': float(stock_data['09. change']),  
                'change_percent': stock_data['10. change percent'],
            }
            return jsonify(stock_info)
        elif 'Error Message' in data:
            return jsonify({'message': 'Stock symbol not found.'}), 404
        else:
            return jsonify({'message': 'Invalid response from the API.'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Failed to fetch stock data. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
