class Config:
	SECRET_KEY = 'd48a6a92d6a7db63d02717b32f484949'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER: 'smtp.gmail.com'
	MAIL_PORT: 587
	MAIL_USE_TLS: True
	MAIL_USE_SSL: False
	MAIL_USERNAME: 'axelhamilton02@gmail.com'
	MAIL_PASSWORD: 'axel:hamilton:2002'
	MAIL_DEFAULT_SENDER: ('Axel Hamilton from CET', 'axelhamilton02@gmail.com')
