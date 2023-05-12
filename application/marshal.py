from flask_restful import fields


venue = {
    "venue_id": fields.Integer,
    "venue_name": fields.String,
    "venue_place": fields.String,
    "venue_location": fields.String,
    "venue_capacity": fields.Integer,
}

show = {
    "show_id": fields.Integer,
    "show_name": fields.String,
    "show_date": fields.String,
    "show_time": fields.String,
    "show_tag": fields.String,
    "show_rating": fields.Float,
    "show_price": fields.Integer,
    "show_venue": fields.Integer,
}

booking = {
    "booking_id": fields.Integer,
    "booking_user": fields.String,
    "booking_venue": fields.Integer,
    "booking_show": fields.Integer,
    "num_tickets": fields.Integer,
    "total__price": fields.Integer,
    "venue_name": fields.String,
    "show_name": fields.String,
}

user = {
    "user_id": fields.Integer,
    "user_name": fields.String,
    "user_password": fields.String,
    "user_email": fields.String,
}


# Path: application\api.py
# Compare this snippet from application\api.py: