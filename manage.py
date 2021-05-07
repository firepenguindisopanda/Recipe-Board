from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app
from App.models import db

manager = Manager(app)
migrate = Migrate(app, db)

from App.models import User

# add migrate command
manager.add_command('db', MigrateCommand)

# initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

# serve command
@manager.command
def serve():
    print('Application running in '+app.config['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=app.config['ENV']=='development')

@manager.command
def make_users():
    bob = User(first_name="Bob", last_name="Smith", username="bob", email="bob@example.com")
    bob.set_password("bobpass")
    sally = User(first_name="Sally", last_name="Smith", username="sal", email="sal@example.com")
    sally.set_password("salpass")
    rob = User(first_name="Rob", last_name="Smith", username="rob", email="rob@example.com")
    rob.set_password("robpass")
    db.session.add(bob)
    db.session.add(sally)
    db.session.add(rob)
    db.session.commit()
    print("users created")

@manager.command
def hello():
    print("Hello World!")

if __name__ == "__main__":
    manager.run()
