"""
description: Application description here

@author: Judith Nyatsine<@gmail.com>
@date: 01-June-2017

"""

import sqlite3
import datetime

__DBFILE__ = "db/rescu-db.db"


def db_connect():
    """Connect to the database and return the connection object.
    """

    # Connect to the database
    db = sqlite3.connect(__DBFILE__)
    return db


def init_db():
    """Initialise the database schema
    """
    db = db_connect()

    # create the table rescu_contacts
    return db.execute("create table if not exists rescu_contacts(full_name text, phone_number text, email_address text, message text, create_date datetime)")


def create_contact_message(full_name, phone_number, email_address, message):
    """Insert the contact message provided in the arguments
    """
    db = db_connect()
    c = db.cursor()

    date_now = datetime.datetime.now()

    # prepare insert statement
    sql_insert = "insert into rescu_contacts (full_name, phone_number, email_address, message, create_date) values('{0}', '{1}', '{2}', '{3}', '{4}')" \
        .format(full_name, phone_number, email_address, message, date_now.strftime("%Y-%m-%d %H-%M-%S"))

    # insert data into database
    db.execute(sql_insert)
    db.commit()

    db.close()


def retrieve_messages():
    """read inserted messages from the contacts table
    """
    db = db_connect()

    cursor = db.execute("select * from rescu_contacts order by create_date desc")

    return cursor.fetchall()
