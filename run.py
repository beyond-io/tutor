from tutor import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tutor.routes import home, model, logout


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)
