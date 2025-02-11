from flask import Flask, request, jsonify, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # passowrd for session

# Admin dummy DaTA
ADMINS = {
    'Zubair': 'nigeria',
    'Lahari': 'india',
    'Hassaan': 'pakistan'
}

# Set session timeOUT
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'error': 'Unsupported Media Type. Use application/json'}), 415
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in ADMINS and ADMINS[username] == password:
        session['username'] = username
        return jsonify({'message': 'Login successful', 'user': username}), 200
    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return jsonify({'message': 'Logout successful'}), 200
    return jsonify({'error': 'No active session'}), 400

if __name__ == '__main__':
    app.run(debug=True)