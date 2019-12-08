Project Title
===============
AddressBook App

## Description

An address book application with CRUD API using Sqlite with Python and Flask

## Usage

GET: localhost:5000/user/<user_id>

GET_ALL: localhost:5000/user

UPDATE: localhost:5000/user/<user_id>

DELETE: localhost:5000/user/<user_id>

CREATE: localhost:5000/user

## Installation
Install Python 3 and clone this repo from git.

## Dependenices
pip install -r requirments.txt

## RUN
Run ./addressbook.py to start the server 

## Sample JSON Input

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
