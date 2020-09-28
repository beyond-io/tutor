from tutor import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tutor.routes import home, course, resources # noqa
from tutor.routes import model # noqa


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)
