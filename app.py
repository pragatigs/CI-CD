from flask import Flask, jsonify
import logging
app = Flask(__name__)
app.config['TESTING'] = True 
logging.basicConfig(level=logging.INFO)
@app.route("/")
def hello_world():
    logging.info("Inside k8s")
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)