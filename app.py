from flask import Flask, render_template, jsonify, request
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# API base URL
API_BASE_URL = "https://a75b88a9-a538-4ec3-97f4-fbb29750e466.mock.pstmn.io"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/adminDashboard')
def adminDashboard():
    return render_template('adminDashboard.html')

@app.route('/secondaryMarket')
def home():
    return render_template('secondaryMarket.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/updateuser', methods=['POST'])
def update_user():
    data = request.get_json()
    logging.debug(f"User login request data: {data}")
    
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
        logging.debug(f"User login response: {response.json()}")
        return jsonify({'message': 'User updated successfully'}), 200
    except requests.exceptions.RequestException as e:
        logging.error(f"User login error: {str(e)}")
        return jsonify({'error': 'Internal server error during user login'}), 500

@app.route('/api/adduser', methods=['POST'])
def add_user():
    data = request.get_json()
    logging.debug(f"Admin login request data: {data}")
    
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
        logging.debug(f"Admin login response: {response.json()}")
        return jsonify({'message': 'User added successfully'}), 201
    except requests.exceptions.RequestException as e:
        logging.error(f"Admin login error: {str(e)}")
        return jsonify({'error': 'Internal server error during admin login'}), 500

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

@app.route('/api/getreports', methods=['PUT'])
def get_reports():
    data = request.get_json()
    uid = data.get('uid')
    
    try:
        response = requests.get(f"{API_BASE_URL}/getreports/{uid}")
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500



@app.route('/api/userlogin', methods=['POST'])
def user_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Validate the username and password using an API call
    try:
        response = requests.post(f"{API_BASE_URL}/userlogin", json={
            "username": username,
            "password": password
        })
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({'message': 'Login successful'}), 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Login error: {str(e)}")
        return jsonify({'error': 'Invalid credentials'}), 401
    
@app.route('/api/users')
def get_users():
    response = requests.get(f"{API_BASE_URL}/getusers")
    return jsonify(response.json())

@app.route('/api/adminlogin', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Validate the username and password using an API call
    try:
        response = requests.post(f"{API_BASE_URL}/adminlogin", json={
            "username": username,
            "password": password
        })
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({'message': 'Login successful'}), 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Login error: {str(e)}")
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
