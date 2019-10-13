from flask import Flask
import requests
import os
import json
from flask import jsonify

app = Flask(__name__)
@app.route("/<userid>", methods=['GET'])
def default(userid):
    sources_url = os.getenv("sources_url", "http://localhost:8081/")
    feeds_url = os.getenv("feeds_url", "http://localhost:8082/")
    sources_resp = requests.post(sources_url+userid, data={"userid": userid})
    sources = json.loads(sources_resp.text)['sources']
    result = []
    for source in sources:
        feed_resp = requests.get(feeds_url+source['id'])
        result.append(feed_resp.json())
    return jsonify(result)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
