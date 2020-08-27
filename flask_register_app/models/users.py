import datetime as dt
from peewee import *


db = SqliteDatabase('users.db')


# ORM
# Database -> Excel file
# Model -> Excel sheet
# Model fields -> Excel sheet columns
# Model values -> Excel sheet values (in rows)
# Model records -> Excel sheet rows
class User(Model):
    name = CharField(max_length=50)
    email = CharField(max_length=150, unique=True)
    image = CharField(max_length=250)
    password = CharField(max_length=100)
    terms = BooleanField(default=True)
    registered_at = DateTimeField()

    class Meta:
        database = db


class Comment(Model):
    user = ForeignKeyField(User, backref='comments')
    text = TextField()
    created_at = DateTimeField(default=dt.datetime.now)

    class Meta:
        database = db


# 1 User
# 5 Comments from this user

# Comment.select().where(Comment.user == existing_user) -> default select for multiple records
# existing_user.comments -> backref (argv for ForeignKeyField)