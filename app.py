from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Dummy API base URL
API_BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/')
def home():
    return render_template('secondaryMarket.html')

@app.route('/api/bonds', methods=['GET'])
def get_bonds():
    try:
        response = requests.get(f"{API_BASE_URL}/posts")  # Simulating bond data retrieval
        response.raise_for_status()  # Raise an error for bad responses
        bond_data = response.json()
        # Transforming data to match the expected structure
        transformed_data = [
            {
                "securityName": bond["title"],
                "maturityDt": "12 JUL 2031",  # Dummy data
                "sMkt": "OD",  # Dummy data
                "bidAmt": "0.0800",  # Dummy data
                "bidYield": "6.3608",  # Dummy data
                "bidPrice": "98.1400",  # Dummy data
                "offerPrice": "98.1700",  # Dummy data
                "offerYield": "6.3565",  # Dummy data
                "offerAmt": "0.0030",  # Dummy data
                "ltp": "98.1400"  # Dummy data
            } for bond in bond_data
        ]
        return jsonify(transformed_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/order_book', methods=['GET'])
def get_order_book():
    try:
        response = requests.get(f"{API_BASE_URL}/comments")  # Simulating order book data retrieval
        response.raise_for_status()
        order_book_data = response.json()
        transformed_data = [
            {
                "securityName": order["name"],
                "ltp": "98.1400",  # Dummy data
                "price": "98.1400",  # Dummy data
                "bo": "Bid"  # Dummy data
            } for order in order_book_data
        ]
        return jsonify(transformed_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/profit_loss', methods=['GET'])
def get_profit_loss():
    # Simulating profit/loss data retrieval
    return jsonify({"summary": "Summary of financial performance."})

@app.route('/api/news', methods=['GET'])
def get_news():
    # Simulating news data retrieval
    return jsonify({"latest": "Latest news updates will be displayed here."})

if __name__ == '__main__':
    app.run(debug=True)