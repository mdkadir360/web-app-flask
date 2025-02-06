from flask import Flask
from flask import request, render_template, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure! Flask App is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    @app.route('/about')
    def about():
        return "This is the about page."

    @app.route('/contact')
    def contact():
        return "This is the contact page."

    @app.route('/user/<username>')
    def show_user_profile(username):
        return f'User {username}'

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return f'Post {post_id}'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Add authentication logic here
            session['username'] = username
            return redirect(url_for('dashboard'))
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('home'))

    @app.route('/dashboard')
    def dashboard():
        if 'username' in session:
            return f"Welcome to your dashboard, {session['username']}!"
        return redirect(url_for('login'))