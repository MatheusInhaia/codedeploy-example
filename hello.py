from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Gr�mio � maior que inter 2 :D'
