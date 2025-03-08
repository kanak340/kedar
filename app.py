from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Dummy API base URL
API_BASE_URL = "https://a75b88a9-a538-4ec3-97f4-fbb29750e466.mock.pstmn.io"

@app.route('/')
def index():
    return render_template('/adminDashboard.html')

@app.route('/adminDashboard')
def adminDashboard():
    return render_template('adminDashboard.html')

@app.route('/secondary-market')
def home():
    return render_template('secondaryMarket.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/api/updateuser', methods=['POST'])
def update_user():
    data = request.get_json()
    uid = data.get('uid')
    username = data.get('username')
    password = data.get('password')
    
    try:
        response = requests.post(f"{API_BASE_URL}/updateuser", json={
            "uid": uid,
            "username": username,
            "password": password
        })
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({'message': 'User updated successfully'}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/adduser', methods=['POST'])
def add_user():
    data = request.get_json()
    uid = data.get('uid')
    username = data.get('username')
    password = data.get('password')
    
    try:
        response = requests.post(f"{API_BASE_URL}/adduser", json={
            "uid": uid,
            "username": username,
            "password": password
        })
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({'message': 'User added successfully'}), 201
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/deleteuser/<uid>', methods=['DELETE'])
def delete_user(uid):
    try:
        response = requests.delete(f"{API_BASE_URL}/deleteuser/{uid}")
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({'message': 'User deleted successfully'}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/user_reports')
def user_reports():
    return render_template('user_reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/api/users')
def get_users():
    response = requests.get(f"{API_BASE_URL}/getusers")
    return jsonify(response.json())



if __name__ == '__main__':
    app.run(debug=True)
