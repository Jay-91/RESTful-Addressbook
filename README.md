Address Book App

An address book application with CRUD API using Sqlite with Python and Flask

CREATE: localhost:5000/user

GET: localhost:5000/user/<user_id>
GET_ALL: localhost:5000/user
UPDATE: localhost:5000/user/<user_id>
DELETE: localhost:5000/user/<user_id>

Setup:
======

Install Python 3 and clone this repo from git.

Get the requriments from requirments.txt
Run the 

Run ./addressbook.py to start the server 


Sample JSON input:
{
  "name": "John",
  "age": 35,
  "organisation": [
    {
      "name": "ABC Inc.,"
    },
    {
      "name": "DEF pvt"
    }
  ],
  "profile": {
  "address":"Sweden"
  }
}
