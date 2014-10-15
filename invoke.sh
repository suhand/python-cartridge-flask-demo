pip install flask
pip --default-timeout=100 install flask-sqlalchemy
pip install flask-bcrypt
pip install flask-WTF
pip install cherrypy
export APP_SETTINGS="config.DevelopmentConfig"
export PATH=$PATH:$APP_SETTINGS
echo $APP_SETTINGS
export DATABASE_URL="sqlite:////sample.db"
echo $DATABASE_URL
python db_create.py
python db_create_users.py
python sql.py
python server.py
