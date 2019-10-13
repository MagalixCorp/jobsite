from flask import Flask
import requests
import os
import json
from flask import jsonify
# Description: this is the manager service that responds to the front page with the user's feed of the job he/she is interested in
app = Flask(__name__)
# The URL is in the form of http://service/id where the ID is the user id 
@app.route("/<userid>", methods=['GET'])
def default(userid):
    # The sources and feeds service URLs can be retreived from environment variables or fallback to the defaults (localhost)
    sources_url = os.getenv("sources_url", "http://localhost:8081/")
    feeds_url = os.getenv("feeds_url", "http://localhost:8082/")
    # We need to construct the sources URL so that it has the user id appended. For example, http://sources-svc/1
    sources_resp = requests.get(sources_url+userid)
    sources = json.loads(sources_resp.text)['sources']
    result = []
    # We request the feeds from each source through the feeds URL
    for source in sources:
        feed_resp = requests.get(feeds_url+source['id'])
        result.append(feed_resp.json())
    # The resulting list is returned to the client
    return jsonify(result)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
