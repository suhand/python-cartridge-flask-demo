from project import db
from project.models import User

# insert data
db.session.add(User("suhan", "suhanr@wso2.com", "pissupuusa"))
db.session.add(User("admin", "admin@dev.stratos.org", "admin"))
db.session.add(User("stratos", "stratos@dev.stratos.org", "stratos"))

# commit the changes
db.session.commit()
