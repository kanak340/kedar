from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Dummy API base URL
API_BASE_URL = "https://a75b88a9-a538-4ec3-97f4-fbb29750e466.mock.pstmn.io"

@app.route('/')
def index():
    return render_template('secondaryMarket.html')
@app.route('/secondary-market')
def home():
    return render_template('secondaryMarket.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
