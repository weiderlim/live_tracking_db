# db.create_all() requires a running Flask session to initialise. 
# creating the DB 

from main import app, db
app.app_context().push()
db.create_all()