from project import db
# from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
# this is moved to sql.py script with new columns id, author_id - suhan 07/10/2014
# db.session.add(BlogPost("Good", "I\'m good."))
# db.session.add(BlogPost("Well", "I\'m well."))
# db.session.add(BlogPost("Excellent", "I\'m excellent."))
# db.session.add(BlogPost("Okay", "I\'m okay."))
# db.session.add(BlogPost("postgres", "we setup a local postgres instance"))

# commit the changes
db.session.commit()
