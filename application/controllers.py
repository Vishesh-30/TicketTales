from flask import render_template, request, redirect, url_for
from main import app, db, Base_url, api
from flask import current_app as app
from application.models import *
import requests
from application.graphs import *
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64







@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_email = request.form.get('Email')
        user_password = request.form.get('Password')
        valid = users.query.filter_by(user_email=user_email, user_password=user_password).first()
        if valid:
            return redirect('/user_home')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        user_name = request.form.get('Name')
        user_email = request.form.get('Email')
        user_password = request.form.get('Password')
        valid = users.query.filter_by(user_name = user_name, user_email=user_email, user_password=user_password).first()
        if valid:
            error = 'User already exists, Please login.'
        else:
            reg = users(user_name=user_name, user_email=user_email, user_password=user_password)
            db.session.add(reg)
            db.session.commit()
            return redirect('/user_home')
    return render_template('register.html', error=error)



@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    error = None
    if request.method == 'POST':
        admin_name = request.form.get('Name')
        admin_email = request.form.get('Email')
        admin_password = request.form.get('Password')
        valid = admins.query.filter_by(admin_name = admin_name, admin_email=admin_email, admin_password=admin_password).first()
        if valid is not None:
            error = 'Admin already exists, Please login.'
        else:
            reg = admins(admin_name=admin_name, admin_email=admin_email, admin_password=admin_password)
            db.session.add(reg)
            db.session.commit()
            return redirect('/admin_home')
    return render_template('admin_register.html', error=error)


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        admin_email = request.form.get('Email')
        admin_password = request.form.get('Password')
        valid = admins.query.filter_by(admin_email=admin_email, admin_password=admin_password).first()
        if valid is not None:
            return redirect('/admin_home')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('admin_login.html', error=error)


@app.route('/user_home', methods=['GET', 'POST'])
def user_home():
    venue = venues.query.all()
    return render_template('user_home.html',venue = venue)


@app.route('/admin_home', methods=['GET', 'POST'])
def admin_home():
    venue = venues.query.all()
    return render_template('admin_home.html', venue=venue)

@app.route('/admin_venue/<int:venue_id>', methods=['GET', 'POST'])
def admin_venue(venue_id):
    venue = requests.get(Base_url + '/api/venue/' + str(venue_id)).json()
    show = shows.query.filter_by(show_venue = venue_id).all()
    return render_template('admin_venue.html', venue=venue, show=show)

@app.route('/venue/<int:venue_id>', methods=['GET', 'POST'])
def user_venue(venue_id):
    venue = requests.get(Base_url + '/api/venue/' + str(venue_id)).json()
    show = shows.query.filter_by(show_venue = venue_id).all()
    return render_template('venue.html', venue=venue, show=show)

@app.route('/edit_venue/<int:venue_id>', methods=['GET', 'POST'])
def edit_venue(venue_id):
    venues = requests.get(Base_url + '/api/venue/' + str(venue_id)).json()
    if request.method == 'POST':
        venue_name = request.form.get('venue_name')
        venue_place = request.form.get('place')
        venue_location = request.form.get('location')
        venue_capacity = request.form.get('capacity')
        updated_venue = { 'venue_name' : venue_name, 'venue_place' : venue_place, 'venue_location' : venue_location, 'venue_capacity' : venue_capacity }
        venue = requests.put(Base_url + '/api/venue/' + str(venue_id), json=updated_venue).json()
        return redirect('/admin_home')
    return render_template('edit_venue.html', venues=venues)


@app.route('/add_venue', methods=['GET', 'POST'])
def add_venue():
    alert = None
    if request.method == 'POST' :
        venue_name = request.form.get('venue_name')
        venue_place = request.form.get('place')
        venue_location = request.form.get('location')
        venue_capacity = request.form.get('capacity')
        valid = venues.query.filter_by(venue_name=venue_name, venue_place=venue_place, venue_location=venue_location, venue_capacity=venue_capacity).first()
        if valid is not None:
            alert = 'Venue already exists.'
        else:
            venue = venues(venue_name=venue_name, venue_place=venue_place, venue_location=venue_location, venue_capacity=venue_capacity)
            db.session.add(venue)
            db.session.commit()
            alert = 'Venue added successfully.'
            return redirect('/admin_home')
    return render_template('add_venue.html', alert=alert)

@app.route('/delete_venue/<int:venue_id>', methods=['GET', 'POST'])
def delete_venue(venue_id):
    venue = requests.delete(Base_url + '/api/venue/' + str(venue_id)).json()
    return redirect('/admin_home')

@app.route('/add_show', methods=['GET', 'POST'])
def add_show():
    alert = None
    if request.method == 'POST':
        show_name = request.form.get('show_name')
        show_date = request.form.get('show_date')
        show_time = request.form.get('show_time')
        show_tag = request.form.get('show_tag')
        show_rating = request.form.get('show_rating')
        show_price = request.form.get('show_price')
        show_venue = request.form.get('show_venue')
        valid = shows.query.filter_by(show_name=show_name, show_date=show_date, show_time=show_time, show_tag=show_tag, show_rating=show_rating, show_price=show_price, show_venue=show_venue).first()
        if valid is not None:
            alert = 'Show already exists.'
        else:
            show = shows(show_name=show_name, show_date=show_date, show_time=show_time, show_tag=show_tag, show_rating=show_rating, show_price=show_price, show_venue=show_venue)
            db.session.add(show)
            db.session.commit()
            alert = 'Show added successfully.'
            return redirect('/admin_home')
    return render_template('add_show.html', alert=alert)

@app.route('/edit_show/<int:show_id>', methods=['GET', 'POST'])
def edit_show(show_id):
    shows = requests.get(Base_url + '/api/show/' + str(show_id)).json()
    if request.method == 'POST':
        show_name = request.form.get('show_name')
        show_date = request.form.get('show_date')
        show_time = request.form.get('show_time')
        show_tag = request.form.get('show_tag')
        show_rating = request.form.get('show_rating')
        show_price = request.form.get('show_price')
        show_venue = request.form.get('show_venue')
        updated_show = { 'show_name' : show_name, 'show_date' : show_date, 'show_time' : show_time, 'show_tag' : show_tag, 'show_rating' : show_rating, 'show_price' : show_price, 'show_venue' : show_venue }
        show = requests.put(Base_url + '/api/show/' + str(show_id), json=updated_show).json()
        return redirect('/admin_home')
    return render_template('edit_show.html', shows=shows)

@app.route('/delete_show/<int:show_id>', methods=['GET', 'POST'])
def delete_show(show_id):
    show = requests.delete(Base_url + '/api/show/' + str(show_id)).json()
    return redirect('/admin_home')


@app.route('/book_show/<int:show_id>', methods=['GET', 'POST'])

def book_show(show_id):
    show = requests.get(Base_url + '/api/show/' + str(show_id)).json()
    booking = bookings.query.all()
    price = show['show_price']
    venue = show['show_venue']
    Alert = None
    capacity_temp = venues.query.filter_by(venue_id=venue).first()
    capacity = capacity_temp.venue_capacity
    for i in booking:
        if i.booking_show == show_id:
            capacity = capacity - i.num_tickets
    
    if capacity == 0:
        Alert = 'Sorry, no tickets available.'
        return render_template('book_show.html', show=show, Alert=Alert, capacity=capacity, price=price)
    else:
        if request.method == 'POST':
            booking_user = request.form.get('booking_user')
            booking_venue = venue
            booking_show = show_id
            num_tickets = int(request.form.get('num_tickets'))
            if num_tickets > capacity:
                Alert = 'Sorry, only ' + str(capacity) + ' tickets are available.'
                return render_template('book_show.html', show=show, Alert=Alert, capacity=capacity, price=price)
            total__price = int(request.form.get('total__price'))
            venue_name_temp = venues.query.filter_by(venue_id=venue).first()
            venue_name = venue_name_temp.venue_name
            show_name_temp = shows.query.filter_by(show_id=show_id).first()
            show_name = show_name_temp.show_name
            booking = bookings(booking_user=booking_user, booking_venue=booking_venue, booking_show=booking_show, num_tickets=num_tickets, total__price=total__price, venue_name=venue_name, show_name=show_name)
            db.session.add(booking)
            db.session.commit()
            Alert = 'Booking successful.'
            return redirect('/user_home')
    return render_template('book_show.html', show=show, price=price, capacity=capacity, Alert=Alert)


@app.route('/my_shows', methods=['GET', 'POST'])
def my_shows():
    user = users.query.all()
    if request.method == 'POST':
        user_email = request.form.get('user_email')
        return redirect('/my_shows/' + user_email)
    return render_template('my_shows.html', user=user)

@app.route('/my_shows/<string:user_email>', methods=['GET', 'POST'])
def user_shows(user_email):
    alert = None
    booking = bookings.query.filter_by(booking_user=user_email).all()
    if booking is None:
        alert = 'No bookings found.'
    return render_template('my_shows.html', booking=booking, alert=alert)

@app.route('/search', methods=['GET', 'POST'])
def search():
    alert = None
    if request.method == 'POST':
        searched = str(request.form.get('search'))
        #searched = searched.replace(' ', '-')
        return redirect('/search/' + searched)
    return render_template('search.html', alert=alert)

@app.route('/search/<string:searched>', methods=['GET', 'POST'])
def search_show(searched):
    alert = None
    showNameTemp = shows.query.filter(shows.show_name.like('%' + searched + '%')).all()
    venueNameTemp = venues.query.filter(venues.venue_name.like('%' + searched + '%')).all()
    show = "No shows found."
    venue = "No venues found."
    showvenue = None
    venueid = None
    for i in showNameTemp:
        show = i.show_name
        showvenue = i.show_venue
    for i in venueNameTemp:
        venue = i.venue_name
        venueid = i.venue_id
    return render_template('search.html', show=show, venue=venue, showvenue=showvenue, venueid=venueid, searched=searched)

    #its pending and not workinggggggg!!!!!!!..............its now working ;)




@app.route('/invoice/<int:booking_id>', methods=['GET', 'POST'])
def invoice(booking_id):
    booking = bookings.query.filter_by(booking_id=booking_id).first()
    show = shows.query.filter_by(show_id=booking.booking_show).first()
    return render_template('invoice.html', booking=booking, show=show)

@app.route('/delete_booking/<int:booking_id>', methods=['GET', 'POST'])
def delete_booking(booking_id):
    booking = bookings.query.filter_by(booking_id=booking_id).first()
    db.session.delete(booking)
    db.session.commit()
    return redirect('/my_shows')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/venueperformance', methods=['GET', 'POST'])
def venueperformance():

    plot = ticketCount()

    fig = Figure(figsize=(12, 6),facecolor='none')
    axis = fig.add_subplot(1, 1, 1)

    axis.bar(plot['show_name_y'], plot['num_tickets'],color='white')
    axis.set_title('Ticket Count')
    axis.set_xlabel('Shows')
    axis.set_ylabel('Ticket Count')
    axis.set_facecolor('none')
    


    fig2 = Figure(figsize=(12, 6),facecolor='none')
    axis2 = fig2.add_subplot(1, 1, 1)
    axis2.bar(plot['venue_name_y'], plot['total__price'],color='white')
    axis2.set_title('Revenue')
    axis2.set_xlabel('Venue')
    axis2.set_ylabel('Revenue')
    axis2.set_facecolor('none')


    canvas = FigureCanvas(fig)
    canvas2 = FigureCanvas(fig2)
    output = io.BytesIO()
    output2 = io.BytesIO()
    canvas.print_png(output)
    canvas2.print_png(output2)

    plot_img  = base64.b64encode(output.getvalue()).decode('utf8')
    plot_img2  = base64.b64encode(output2.getvalue()).decode('utf8')

    return render_template('venueperformance.html', plot_img=plot_img, plot_img2=plot_img2)