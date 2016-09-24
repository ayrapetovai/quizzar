#!/usr/bin/python

from peewee import *

#db = PostgresqlDatabase(
#    'postgres',  # Required by Peewee.
#    user='postgres',  # Will be passed directly to psycopg2.
#    password='postgres',  # Ditto.
#    host='192.168.1.39',  # Ditto.
#    port='5432'
#)

db = SqliteDatabase('users.db')

class User(Model):
    username = CharField()
    passwd = CharField()
    class Meta:
        database = db

#User.create_table()
#User.create(username="artem", passwd="1234")

for user in User.select():
	print user.username, user.passwd
