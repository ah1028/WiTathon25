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

@app.route('/baking-brownies')
def baking_brownies():
    return render_template('bakingbrownies.html')

@app.route('/new-activity/', methods=('GET', 'POST'))
def new_activity():
    if request.method == 'POST':
        image = request.form['image']
        lat = request.form['latitude']
        lon = request.form['longitude']
        time = request.form['duration']
        title = request.form['title']
        desc = request.form['description']
        exp = request.form['expense']
        tod = request.form['tod'] # This is value A, B4, AD
        mini = request.form['mini']
        maxi = request.form['maxi']
        tags = request.form.getlist('exercise') + request.form.getlist('art') + request.form.getlist('mindfullness')
        if not title:
            flash('Title is required!')
        else:
            db.add_activity(title, desc, image, exp, tod, time, lon, lat, mini, maxi, tags)
            return redirect(url_for('menupage'))
    return render_template('new-activity.html')

@app.route('/images/<id>.jpg')
def images(image_id):
    return db.activity_pic(image_id)
