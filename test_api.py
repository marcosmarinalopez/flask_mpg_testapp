from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola, Mundo"

@app.route("/abc/")
def abc():
    return "Probando abc"

if __name__ == '__main__':
    app.run(debug=True)
