from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Multiple admin credentials
ADMINS = {
    'Zubair': 'nigeria',
    'Lahari': 'india',
    'Hassaan': 'pakistan'
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in ADMINS and ADMINS[username] == password:
            session['username'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Invalid Username or Password. Please try again."
    return render_template('login.html', error=error)

@app.route('/admin')
def admin_dashboard():
    if 'username' in session:
        admin = session['username']
        data = {
            'tasks': ['Review Reports', 'Manage Users', 'System Monitoring'],
            'messages': [
                {'from': 'Support Team', 'content': 'System maintenance scheduled for tonight.'},
                {'from': 'HR', 'content': 'Reminder: Submit monthly reports by Friday.'}
            ],
            'notifications': [
                'New user registered.',
                'Password reset request pending approval.'
            ]
        }
        return render_template('admin_dashboard.html', admin=admin, data=data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.before_request
def make_session_permanent():
    session.permanent = True

if __name__ == '__main__':
    app.run(debug=True)
