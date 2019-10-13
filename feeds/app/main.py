from flask import Flask
import requests
import os
from flask import jsonify

feeds = {
    "1": os.getenv("jobzilla", "http://localhost:9091"),
    "2": os.getenv("wuzzuf", "http://localhost:9092"),
    "3": os.getenv("linkedin", "http://localhost:9093")
}

app = Flask(__name__)
@app.route("/<feed>", methods=['GET'])
def default(feed):
    resp = requests.get(feeds[feed])
    return resp.json()


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8082)
