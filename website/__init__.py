from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_healthz import healthz
from flask_healthz import HealthError

db = SQLAlchemy()


def liveness():
    pass


def readiness():
    try:
        db.session
    except Exception:
        raise HealthError("Can't connect to the database")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rfvtgbyhn edcrfvtgb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p0ssw0rd@postgres-postgresql:5432/postgres'
    # Pooling control
    app.config['SQLALCHEMY_POOL_SIZE'] = 10
    # logging of DB connection
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(healthz, url_prefix='/healthz')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.config.update(
        HEALTHZ={
            "live": lambda: liveness(),
            "ready": lambda: readiness(),
        }
    )

    return app


def create_database(app):
    db.create_all(app=app)
    print('Created Database!')



