from flask import Flask
import requests
from flask import jsonify

app = Flask(__name__)
@app.route("/<userid>", methods=['POST'])
def default(userid):
    # Assuming that this service calls the database and retrieves the sources that this user is following
    response = {"userid": userid,
                "sources": [
                    {
                        "id": "1",
                        "name": "JobZilla"
                    },
                    {
                        "id": "2",
                        "name": "Wuzzuf"
                    },
                    {
                        "id": "3",
                        "name": "LinkedIn"
                    }
                ]
                }
    return jsonify(response)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8081)
