from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Welcome to my API!</h1>'

@app.route('/about')
def nite_to_meet_u():
    return 'This is a simple Flask API.'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
