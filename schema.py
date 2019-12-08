from init import ma
from datamodel import User, UserProfile, Organisation

# Organisation Schema
class OrganisationSchema(ma.Schema):
  model = Organisation
  class Meta:
    fields = ('name',)


          
# UserProfile Schema
class UserProfileSchema(ma.Schema):
  model = UserProfile
  class Meta:
    fields = ('address',)

     
# User Schema
class UserSchema(ma.Schema):
  organisation = ma.Nested(OrganisationSchema, many=True)
  profile = ma.Nested(UserProfileSchema, many=False)
  class Meta: 
    model = User
    fields = ('id', 'name', 'age', 'organisation','profile')