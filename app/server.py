import logging
from flask import Flask, request

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello():
    app.logger.info(f"Received request from {request.remote_addr} to {request.path}")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
