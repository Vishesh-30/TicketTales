from flask_restful import reqparse


create_venue_parser = reqparse.RequestParser()
create_venue_parser.add_argument("venue_name",type = str)
create_venue_parser.add_argument("venue_place",type = str)
create_venue_parser.add_argument("venue_location",type = str)
create_venue_parser.add_argument("venue_capacity",type = int)

update_venue_parser = reqparse.RequestParser()
update_venue_parser.add_argument("venue_name",type = str)
update_venue_parser.add_argument("venue_place",type = str)
update_venue_parser.add_argument("venue_location",type = str)
update_venue_parser.add_argument("venue_capacity",type = int)

create_show_parser = reqparse.RequestParser()
create_show_parser.add_argument("show_name",type = str)
create_show_parser.add_argument("show_date",type = str)
create_show_parser.add_argument("show_time",type = str)
create_show_parser.add_argument("show_tag",type = str)
create_show_parser.add_argument("show_rating",type = float)
create_show_parser.add_argument("show_price",type = int)
create_show_parser.add_argument("show_venue",type = int)

update_show_parser = reqparse.RequestParser()
update_show_parser.add_argument("show_name",type = str)
update_show_parser.add_argument("show_date",type = str)
update_show_parser.add_argument("show_time",type = str)
update_show_parser.add_argument("show_tag",type = str)
update_show_parser.add_argument("show_rating",type = float)
update_show_parser.add_argument("show_price",type = int)
update_show_parser.add_argument("show_venue",type = int)

create_booking_parser = reqparse.RequestParser()
create_booking_parser.add_argument("booking_user",type = str)
create_booking_parser.add_argument("booking_venue",type = int)
create_booking_parser.add_argument("booking_show",type = int)
create_booking_parser.add_argument("num_tickets",type = int)
create_booking_parser.add_argument("total__price",type = int)
create_booking_parser.add_argument("venue_name",type = str)
create_booking_parser.add_argument("show_name",type = str)

update_booking_parser = reqparse.RequestParser()
update_booking_parser.add_argument("booking_user",type = str)
update_booking_parser.add_argument("booking_venue",type = int)
update_booking_parser.add_argument("booking_show",type = int)
update_booking_parser.add_argument("num_tickets",type = int)
update_booking_parser.add_argument("total__price",type = int)
update_booking_parser.add_argument("venue_name",type = str)
update_booking_parser.add_argument("show_name",type = str)


create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("user_name",type = str)
create_user_parser.add_argument("user_password",type = str)
create_user_parser.add_argument("user_email",type = str)

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument("user_name",type = str)
update_user_parser.add_argument("user_password",type = str)
update_user_parser.add_argument("user_email",type = str)

# Path: application\api.py
# Compare this snippet from application\api.py:
