A blog platform using flask

set environment variable
on powershell:
$env:FLASK_APP = "run.py"

set debug mode:
$env:FLASK_DEBUG=1

Run the app:
flask run
You need to set the environment variable in order to use this command

Run sql datebase:
python
from blog import db (which is database variable)
db.create_all()
from blog.models import User, Post(import the user table and post table)
User.query.all() (check all user information)