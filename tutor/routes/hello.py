from flask import render_template
 
def hello():
    return render_template('index.html')