from tutor import app, db


from tutor.routes import home
from tutor.routes import course

if __name__ == "__main__":
    app.run(debug=True)
