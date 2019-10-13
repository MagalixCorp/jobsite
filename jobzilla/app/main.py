from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
@app.route("/", methods=['GET'])
def default():
    return jsonify({"source":"jobzilla","jobs": 
        [
            {
                "title":"DevOps Engineer",
                "description":"Currently there is a new role available in the networking area. You will be responsible for deploying and configuring in in-house/third-party develop software applications + supporting the agile software development practices including continuous deployment. Furthermore you will be using automation extensively to manage and configure the systems in support of the product(s) and the development teams."
            },
            {
                "title":"DevOps Engineer",
                "description":"With over 15 different DevOps teams working on client environments, there is a lot of overlap in technology and tooling, that’s where the SaaS team comes in. The team is responsible for providing all customer teams with the right tools to maintain the environments. They provide monitoring solutions, different authentication options, containerization, automation layers and more. They have their own infrastructure to support their tooling catalogue, distribute it throughout the company and are running a hybrid model on private cloud and different public cloud vendors. This team experiments with new solutions, works on new technologies to provide, further optimize / automate the current set and keeps the daily operations running."
            },
            {
                "title":"DevOps Engineer",
                "description":"Currently, we are at an exciting transformation period, working towards becoming a booking platform for package holidays. This means a lot of hard work and dedication, as well as a lot of opportunities! We are data-driven and results-oriented, following strict Agile and Lean Principles. To facilitate our purposes, we have created two “Super-teams”. These are a network of colleagues working together on the same value chain with a common purpose and continuous synchronisation. The multi-disciplinary Scrum team is a part of the Super-team as well as different stakeholders from all departments of the organisation."
            }
        ]
    })


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9091)
