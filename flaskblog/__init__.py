from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


"""
app.config['SECRET_KEY'] = 'd48a6a92d6a7db63d02717b32f484949'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

"""
mail_settings = {
	'MAIL_SERVER': 'smtp.gmail.com',
	'MAIL_PORT': 587,
	'MAIL_USE_TLS': True,
	'MAIL_USE_SSL': False,
	'MAIL_USERNAME': 'axelhamilton02@gmail.com',
	'MAIL_PASSWORD': 'axel:hamilton:2002',
	'MAIL_DEFAULT_SENDER': ('Axel Hamilton from CET', 'axelhamilton02@gmail.com')
}

app.config.update(mail_settings)
"""

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from flaskblog.users.routes import users
	from flaskblog.posts.routes import posts
	from flaskblog.main.routes import main
	from flaskblog.errors.handlers import errors

	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app