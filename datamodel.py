from init import db

# User Class/Model
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  age = db.Column(db.Integer)
  profile = db.relationship('UserProfile', backref='user', cascade="all, delete-orphan",uselist=False) 
  organisation = db.relationship('Organisation', backref='user', cascade="all, delete-orphan", lazy='dynamic') 

  def __init__(self, name, age,):
    self.name = name
    self.age = age

# UserProfile Class/Model
class UserProfile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,
                     db.ForeignKey('user.id'),
                     nullable=False)
  address = db.Column(db.String(100))
  

  def __init__(self, user_id, address):  
    self.user_id = user_id
    self.address = address

# Organisation Class/Model
class Organisation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,
                     db.ForeignKey('user.id'),
                     nullable=False)
  name = db.Column(db.String(100))
  

  def __init__(self, user_id, name):  
    self.user_id = user_id
    self.name = name

