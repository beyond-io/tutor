from run import app
from routes import hello

@app.route('/')
def hello_route():
    return hello.hello()