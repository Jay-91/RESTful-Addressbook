from flask import request, jsonify
from flask_restful import Resource

from init import app, db, api
from datamodel import User, UserProfile, Organisation
from schema import UserSchema, UserProfileSchema, OrganisationSchema


# Init schema
organisation_schema = OrganisationSchema()

userprofile_schema = UserProfileSchema()

user_schema = UserSchema()
users_schema = UserSchema(many=True)




# Create a User
class UserResource(Resource):
    def post(self):
      name = request.json['name']
      age = request.json['age']
      profile = request.json['profile']
      organisation = request.json['organisation']
      new_user = User(name, age)
      new_user.profile = UserProfile(new_user.id, profile['address'])

      for i in organisation:
        new_organisation = Organisation(new_user.id, i['name'])
        new_user.organisation.append(new_organisation)
        db.session.add(new_organisation)
       
      db.session.add(new_user.profile)
      db.session.add(new_user)
      db.session.commit()
      return user_schema.jsonify(new_user)

class GetUserResource(Resource):

    # Get Single user
    def get(self,id):
      user = User.query.get(id)
      return user_schema.jsonify(user)
     
    # Update a user

    def put(self,id):
      user = User.query.get(id)

      name = request.json['name']
      age = request.json['age']
      organisation = request.json['organisation']
      profile = request.json['profile']
      organisation_list = []

      for i in organisation:
        new_organisation = Organisation(user.id, i['name'])
        organisation_list.append(new_organisation)


      user.name = name
      user.age = age
      user.profile.address=  profile['address']
      user.organisation = organisation_list
      
      db.session.commit()

      return user_schema.jsonify(user)

    # Delete User

    def delete(self,id):
      user = User.query.get(id)
      db.session.delete(user)
      db.session.commit()

      return user_schema.jsonify(user)

class AllUsers(Resource):
    # Get All Users

    def get(self):
      all_users = User.query.all()
      result = users_schema.dump(all_users)
      return jsonify(result)


api.add_resource(UserResource, '/user') # Route_1
api.add_resource(GetUserResource, '/user/<id>') # Route_2
api.add_resource(AllUsers, '/user') # Route_3

# Run Server
if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)