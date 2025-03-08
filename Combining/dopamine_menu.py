from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/menupage/')
def menupage():
    return render_template('menupage.html')