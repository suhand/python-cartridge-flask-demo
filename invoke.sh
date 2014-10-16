cd /var/www/www
pip install flask
pip --default-timeout=100 install flask-sqlalchemy
pip --default-timeout=100 install flask-bcrypt
pip --default-timeout=100 install flask-WTF
pip install cherrypy
export APP_SETTINGS="config.DevelopmentConfig"
export PATH=$PATH:$APP_SETTINGS
echo $APP_SETTINGS
export DATABASE_URL="sqlite:////sample.db"
echo $DATABASE_URL
python /var/www/www/db_create.py > /tmp/db_create.log
python /var/www/www/db_create_users.py > /tmp/db_create_users.log
python /var/www/www/sql.py > /tmp/sql.log
python /var/www/www/server.py > /tmp/server.log
