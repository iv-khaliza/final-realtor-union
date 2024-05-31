from app import app, db
from flask import render_template, flash, url_for, redirect, request
from flask_login import current_user, login_user, logout_user
from app.models import Company, Flat
from app.forms import LoginForm, RegistrationForm, EditProfileForm, AddOffer
import sqlalchemy as sa
from sqlalchemy.orm import Session

@app.route('/')
@app.route('/index')
def index():
    flats = db.session.scalars(sa.select(Flat).order_by(Flat.timestamp.desc()))
    # flats = db.session.scalars(sa.select(Flat).order_by(Flat.timestamp.desc()))
    # flats_s = db.session.scalars(sa.select(Flat_s).order_by(Flat_s.timestamp.desc()))
    return render_template('index.html', title='Main', flats=flats)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        name = db.session.scalar(sa.select(Company).where(Company.name == form.name.data))
        if name is None or not name.check_password(form.password.data):
            flash('Invalid name or password')
            return redirect(url_for('login'))
        login_user(name, remember=form.remember_me.data)
        if current_user.name == 'admin':
            return redirect(url_for('admin'))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        name = Company(name=form.name.data, email=form.email.data)
        name.set_password(form.password.data)
        db.session.add(name)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/company/<name>', methods=['GET', 'POST'])
def company(name):
    form = AddOffer()
    name = db.first_or_404(sa.select(Company).where(Company.name == name))

    if form.validate_on_submit():
        if form.offer_type.data == 're':
            flat = Flat(f_type=form.flat_type.data, order_type=form.offer_type.data, \
                        price=form.price.data, num_of_rooms=form.nor.data, address=form.address.data, \
                        square=form.square.data, body=form.body.data, img=form.img.data, author=current_user)
            db.session.add(flat)
            db.session.commit()
        elif form.offer_type.data == 'sa':
            flat = Flat(f_type=form.flat_type.data, order_type=form.offer_type.data, price=form.price.data, num_of_rooms=form.nor.data,
                        address=form.address.data, square=form.square.data, body=form.body.data, img=form.img.data,
                        author=current_user)
            db.session.add(flat)
            db.session.commit()
        else:
            print('None')

    flats = db.session.scalars(sa.select(Flat).where(Flat.author == name).order_by(Flat.timestamp.desc()))
    return render_template('company.html', title='Company', company=name, flats=flats, form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.body = form.body.data
        current_user.phone = form.phone.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.body.data = current_user.body
        form.phone.data = current_user.phone
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route('/offer/<id>', methods=['GET', 'POST'])
def offer(id):
    offer = Flat.query.get(int(id))
    flats = db.session.scalars(sa.select(Flat).order_by(Flat.timestamp.desc()))
    return render_template('offer.html', offer=offer, flats=flats, title='Offer')

@app.route('/delete/<fid>')
def delete_flat(fid):
    flat = Flat.query.get(int(fid))
    if flat:
        db.session.delete(flat)
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin')
def admin():
    if current_user.is_anonymous:
        flash('No no no Mr Fish')
        return redirect(url_for('index'))
    else:
        if current_user.name == 'admin':
            companies = Company.query.all()
            return render_template('admin_index.html', title="admin", companies=companies)
        else:
            return redirect(url_for('index'))

