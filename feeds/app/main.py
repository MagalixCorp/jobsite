from flask import Flask
import requests
import os
from flask import jsonify
# Description: it accepts the feed id from the client and uses it to fetch job listings from the corresponding URL

# The feeds dictionary simulates a database where the URL and the ID of the job site should be stored.
# Because we are deploying this in a Kubernetes environment, we use environment variables to get the URLs corresponding to the IDs or
# default to localhost (if you are going to host the entire application on your local machine without containers)
feeds = {
    "1": os.getenv("jobzilla", "http://localhost:9091"),
    "2": os.getenv("wuzzuf", "http://localhost:9092"),
    "3": os.getenv("linkedin", "http://localhost:9093")
}

app = Flask(__name__)
# The URL should be http://service/id where the ID is used to retreive the corresponding job site
@app.route("/<feed>", methods=['GET'])
def default(feed):
    resp = requests.get(feeds[feed])
    return resp.json()


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8082)
