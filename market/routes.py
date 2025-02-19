from market import app,db
from flask import render_template , redirect,url_for
from market.model import Item,User
from market.froms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username= form.username.data,emailid=form.emailid.data,password_hash=form.password1.data,budget=1000)
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()
        return redirect(url_for('market_page'))

    return render_template('register.html',form=form)
