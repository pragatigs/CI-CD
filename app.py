from flask import Flask, jsonify

app = Flask(__name__)
app.config['TESTING'] = True 

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)