import pandas as pd
import sqlite3


def ticketCount():
    conn = sqlite3.connect('instance\TicketTales.sqlite3')
    venues = pd.read_sql_query("SELECT * FROM venues", conn)
    shows = pd.read_sql_query("SELECT * FROM shows", conn)
    bookings = pd.read_sql_query("SELECT * FROM bookings", conn)
    bs = pd.merge(shows, bookings, left_on='show_id', right_on='booking_show')
    svb = pd.merge(bs, venues, left_on='booking_venue', right_on='venue_id')
    conn.close()
    return svb

    





