from tutor import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tutor.routes import home
from tutor.routes import model
from tutor.models import course
from tutor.models import resource


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)
