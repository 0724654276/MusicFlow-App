#from typing_extensions import Required
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from flask import Flask
class Music:
    """
    Music class to define music objects
    """

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'spotify.jpg' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count

#database models

#retrieving a user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    pass_secure  = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f"User {self.username}"

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f"User {self.name}"



#reviews
class Review:

    all_reviews = []

    def __init__(self,music_id,title,imageurl,review):
        self.music_id = music_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
