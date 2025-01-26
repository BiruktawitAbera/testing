from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/another_route')
def another_route():
    return 'This is another route!', 200  # Ensure it returns 200 status code

if __name__ == '__main__':
    app.run(debug=True)
