from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Guest
from flask_login import login_user, logout_user, current_user



@app.route('/')
def index():
    print("Current Guest:", current_user)
    print("Active User:", current_user.is_active)
    print("Anonymous User:", current_user.is_anonymous)
    print("Authenticated User:", current_user.is_authenticated)
    print("ID of User:", current_user.get_id)
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        r = request.form
        if r.get('confirm_password') == r.get('password'):
            data = {
                'fake_name': r.get('fake_name'),
                'fake_email': r.get('fake_email'),
                'password': r.get('password')
                }
            print(data)
            g = Guest(fake_name=data['fake_name'], fake_email=data['fake_email'], password=data['password'])
            g.hash_password(g.password)
            db.session.add(g)
            db.session.commit()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        r = request.form
        guest = Guest.query.filter_by(fake_email=r.get('fake_email')).first()
        if guest is None or not guest.check_password(r.get('password')):
            return redirect(url_for('login'))
        login_user(guest, remember=r.get('remember_me'))
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))