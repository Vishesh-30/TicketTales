from application.database import db
from flask_login import UserMixin



class admins(db.Model, UserMixin):
    __tablename__ = 'admins'
    admin_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    admin_name = db.Column(db.String(50), nullable = False)
    admin_email = db.Column(db.String(50), nullable = False, primary_key = True)
    admin_password = db.Column(db.String(50), nullable = False)
    def is_admin(self):
        return True


class users(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    def get_id(self):
        return self.user_email
    def is_admin(self):
        return False



class venues(db.Model):
    __tablename__ = 'venues'
    venue_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    venue_name = db.Column(db.String(50), nullable = False)
    venue_place = db.Column(db.String(50), nullable = False)
    venue_location = db.Column(db.String(50), nullable = False)
    venue_capacity = db.Column(db.Integer(), nullable = False)
    shows = db.relationship("shows")


class shows(db.Model):
    __tablename__ = 'shows'
    show_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    show_name = db.Column(db.String(50), nullable = False)
    show_date = db.Column(db.String(50), nullable = False)
    show_time = db.Column(db.String(50), nullable = False)
    show_tag = db.Column(db.String(50), nullable = False)
    show_rating = db.Column(db.Integer(), nullable = False)
    show_price = db.Column(db.Integer(), nullable = False)
    show_venue = db.Column(db.Integer(), db.ForeignKey('venues.venue_id'))



class bookings(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    booking_user = db.Column(db.String(50), db.ForeignKey('users.user_email'))
    booking_venue = db.Column(db.Integer(), db.ForeignKey('venues.venue_id'))
    booking_show = db.Column(db.Integer(), db.ForeignKey('shows.show_id'))
    num_tickets = db.Column(db.Integer(), nullable = False)
    total__price = db.Column(db.Integer(), nullable = False)
    venue_name = db.Column(db.String(50), db.ForeignKey('venues.venue_name'))
    show_name = db.Column(db.String(50), db.ForeignKey('shows.show_name'))