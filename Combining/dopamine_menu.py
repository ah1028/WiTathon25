from flask import Flask, render_template, request, url_for, flash, redirect, abort, session
import db_functions as db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if db.login(username, password):
        session['user'] = username 
        return redirect(url_for('menupage'))
    else:
        flash("Invalid username or password", "danger")
        return redirect(url_for('index'))  # Reload login page with flash message

@app.route('/menupage/')
def menupage():
    return render_template('menupage.html')