from flask import request
from flask_restful import Resource, Api
from application.models import users, admins, venues, shows, bookings
from application.database import db
from application.validate import NotFoundError, MissingParameterError
from main import api
from application.marshal import *
from flask_restful import marshal_with
from application.parsers import update_venue_parser, create_venue_parser, create_show_parser, update_show_parser, create_booking_parser, update_booking_parser, create_user_parser, update_user_parser



class VenueAPI(Resource):
    @marshal_with(venue)
    def get(self, venue_id):
        venue = venues.query.filter_by(venue_id=venue_id).first()
        if venue:
            return venue
        else:
            raise NotFoundError(404, "Venue not found")
        
    @marshal_with(venue)
    def put(self, venue_id):
        venue = venues.query.filter_by(venue_id=venue_id).first()
        if venue:
            args = update_venue_parser.parse_args()
            venue.venue_name = args['venue_name']
            venue.venue_place = args['venue_place']
            venue.venue_location = args['venue_location']
            venue.venue_capacity = args['venue_capacity']
            if not venue.venue_name:
                raise MissingParameterError(400, "Venue name is required")
            if not venue.venue_place:
                raise MissingParameterError(400, "Venue place is required")
            if not venue.venue_location:
                raise MissingParameterError(400, "Venue location is required")
            if not venue.venue_capacity:
                raise MissingParameterError(400, "Venue capacity is required")
            else:
                db.session.commit()
                return {"message": "Venue updated successfully"}
        else:
            raise NotFoundError(404, "Venue not found")
    
    @marshal_with(venue)
    def delete(self, venue_id):
        venue = venues.query.filter_by(venue_id=venue_id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()
            return {"message": "Venue deleted successfully"}
        else:
            raise NotFoundError(404, "Venue not found")

    @marshal_with(venue)    
    def post(self):
        args = create_venue_parser.parse_args()
        venue_name = args['venue_name']
        venue_place = args['venue_place']
        venue_location = args['venue_location']
        venue_capacity = args['venue_capacity']
        if not venue_name:
            raise MissingParameterError(400, "Venue name is required")
        if not venue_place:
            raise MissingParameterError(400, "Venue place is required")
        if not venue_location:
            raise MissingParameterError(400, "Venue location is required")
        if not venue_capacity:
            raise MissingParameterError(400, "Venue capacity is required")
        else:
            venue = venues(venue_name=venue_name, venue_place=venue_place, venue_location=venue_location, venue_capacity=venue_capacity)
            db.session.add(venue)
            db.session.commit()
            return {"message": "Venue created successfully"}

class ShowsAPI(Resource):
    @marshal_with(show)
    def get(self, show_id):
        show = shows.query.filter_by(show_id=show_id).first()
        if show:
            return show
        else:
            raise NotFoundError(404, "Show not found")
        
    @marshal_with(show)
    def put(self, show_id):
        show = shows.query.filter_by(show_id=show_id).first()
        if show:
            args = update_show_parser.parse_args()
            show.show_name = args['show_name']
            show.show_date = args['show_date']
            show.show_time = args['show_time']
            show.show_tag = args['show_tag']
            show.show_rating = args['show_rating']
            show.show_price = args['show_price']
            show.show_venue = args['show_venue']
            if not show.show_name:
                raise MissingParameterError(400, "Show name is required")
            if not show.show_date:
                raise MissingParameterError(400, "Show date is required")
            if not show.show_time:
                raise MissingParameterError(400, "Show time is required")
            if not show.show_tag:
                raise MissingParameterError(400, "Show tag is required")
            if not show.show_rating:
                raise MissingParameterError(400, "Show rating is required")
            if not show.show_price:
                raise MissingParameterError(400, "Show price is required")
            if not show.show_venue:
                raise MissingParameterError(400, "Show venue is required")
            else:
                db.session.commit()
                return {"message": "Show updated successfully"}
        else:
            raise NotFoundError(404, "Show not found")
    
    @marshal_with(show)
    def delete(self, show_id):
        show = shows.query.filter_by(show_id=show_id).first()
        if show:
            db.session.delete(show)
            db.session.commit()
            return {"message": "Show deleted successfully"}
        else:
            raise NotFoundError(404, "Show not found")

    @marshal_with(show)    
    def post(self):
        args = create_show_parser.parse_args()
        show_name = args['show_name']
        show_date = args['show_date']
        show_time = args['show_time']
        show_tag = args['show_tag']
        show_rating = args['show_rating']
        show_price = args['show_price']
        show_venue = args['show_venue']
        if not show_name:
            raise MissingParameterError(400, "Show name is required")
        if not show_date:
            raise MissingParameterError(400, "Show date is required")
        if not show_time:
            raise MissingParameterError(400, "Show time is required")
        if not show_tag:
            raise MissingParameterError(400, "Show tags is required")
        if not show_rating:
            raise MissingParameterError(400, "Show rating is required")
        if not show_price:
            raise MissingParameterError(400, "Show price is required")
        if not show_venue:
            raise MissingParameterError(400, "Show venue is required")
        else:
            show = shows(show_name=show_name, show_date=show_date, show_time=show_time, show_tag=show_tag, show_rating=show_rating, show_price=show_price, show_venue=show_venue)
            db.session.add(show)
            db.session.commit()
            return {"message": "Show created successfully"}
        

class BookingAPI(Resource):
    @marshal_with(booking)
    def get(self, booking_id):
        booking = bookings.query.filter_by(booking_id=booking_id).first()
        if booking:
            return booking
        else:
            raise NotFoundError(404, "Booking not found")

    @marshal_with(booking)    
    def put(self, booking_id):
        booking = bookings.query.filter_by(booking_id=booking_id).first()
        if booking:
            args = update_booking_parser.parse_args()
            booking.booking_user = args['booking_user']
            booking.booking_venue = args['booking_venue']
            booking.booking_show = args['booking_show']
            booking.num_tickets = args['num_tickets']
            booking.total__price = args['total__price']
            booking.venue_name = args['venue_name']
            booking.show_name = args['show_name']
            if not booking.booking_user:
                raise MissingParameterError(400, "Booking user is required")
            if not booking.booking_venue:
                raise MissingParameterError(400, "Booking venue is required")
            if not booking.booking_show:
                raise MissingParameterError(400, "Booking show is required")
            if not booking.num_tickets:
                raise MissingParameterError(400, "Number of tickets is required")
            if not booking.total__price:
                raise MissingParameterError(400, "Total price is required")
            else:
                db.session.commit()
            return {"message": "Booking updated successfully"}
        else:
            raise NotFoundError(404, "Booking not found")
    
    @marshal_with(booking)
    def delete(self, booking_id):
        booking = bookings.query.filter_by(booking_id=booking_id).first()
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return {"message": "Booking deleted successfully"}
        else:
            raise NotFoundError(404, "Booking not found")
        
    @marshal_with(booking)
    def post(self):
        args = create_booking_parser.parse_args()
        booking_user = args['booking_user']
        booking_venue = args['booking_venue']
        booking_show = args['booking_show']
        num_tickets = args['num_tickets']
        total__price = args['total__price']
        booking.venue_name = args['venue_name']
        booking.show_name = args['show_name']
        if not booking_user:
            raise MissingParameterError(400, "Booking user is required")
        if not booking_venue:
            raise MissingParameterError(400, "Booking venue is required")
        if not booking_show:
            raise MissingParameterError(400, "Booking show is required")
        if not num_tickets:
            raise MissingParameterError(400, "Number of tickets is required")
        if not total__price:
            raise MissingParameterError(400, "Total price is required")
        else:
            booking = bookings(booking_user=booking_user, booking_venue=booking_venue, booking_show=booking_show, num_tickets=num_tickets, total__price=total__price)
            db.session.add(booking)
            db.session.commit()
            return {"message": "Booking created successfully"}
        



class UserAPI(Resource):
    @marshal_with(user)
    def get(self, user_id):
        user = users.query.filter_by(user_id=user_id).first()
        if user:
            return user
        else:
            raise NotFoundError(404, "User not found")

    @marshal_with(user)    
    def put(self, user_id):
        user = users.query.filter_by(user_id=user_id).first()
        if user:
            args = update_user_parser.parse_args()
            user.user_name = args['user_name']
            user.user_password = args['user_password']
            user.user_email = args['user_email']
            if not user.user_name:
                raise MissingParameterError(400, "User name is required")
            if not user.user_password:
                raise MissingParameterError(400, "User password is required")
            if not user.user_email:
                raise MissingParameterError(400, "User email is required")
            else:
                db.session.commit()
                return {"message": "User updated successfully"}
        else:
            raise NotFoundError(404, "User not found")
    
    @marshal_with(user)
    def delete(self, user_id):
        user = users.query.filter_by(user_id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}
        else:
            raise NotFoundError(404, "User not found")
        
    @marshal_with(user)
    def post(self):
        args = create_user_parser.parse_args()
        user_name = args['user_name']
        user_password = args['user_password']
        user_email = args['user_email']
        if not user.user_name:
            raise MissingParameterError(400, "User name is required")
        if not user.user_password:
            raise MissingParameterError(400, "User password is required")
        if not user.user_email:
            raise MissingParameterError(400, "User email is required")
        else:
            user = users(user_name=user_name, user_password=user_password, user_email=user_email)
            db.session.add(user)
            db.session.commit()
            return {"message": "User created successfully"}
        

api.add_resource(UserAPI, '/api/user/<user_id>','/api/user')
api.add_resource(VenueAPI, '/api/venue/<venue_id>','/api/venue')
api.add_resource(ShowsAPI, '/api/show/<show_id>','/api/show')
api.add_resource(BookingAPI, '/api/booking/<booking_id>','/api/booking')


