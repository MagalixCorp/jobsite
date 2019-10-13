from flask import Flask
from flask import jsonify
# Description: Simulates a real-world API that returns a list of job posts
app = Flask(__name__)
@app.route("/", methods=['GET'])
def default():
    return jsonify({"source": "wuzzuf", "jobs":
                    [
                        {
                            "title": "Senior Devops Engineer",
                            "description": "Are you ambitious and eager to learn about industrial automation? Would you like to work in an informal team in an international organisation? We are a growing software and consultancy company that focuses on the logistical processes of container terminals, intermodal facilities, airports, factories and other logistics systems all over the world. Because the demand for our software products has grown considerably, we are looking for reinforcement of our ICT department."
                        },
                        {
                            "title": "Senior Devops Engineer",
                            "description": "Are you a Senior DevOps engineer? Are you looking for a company that values their employees, offers career, work with the newest technologies, and endless projects for you to enhance/ develop? If yes, then you have chosen correctly, we are looking forward to arranging an interview with you soon!"
                        },
                        {
                            "title": "DevOps Engineer",
                            "description": "As a DevOps Engineer, your main focus will be to  develop and maintain secure AWS based cloud solutions and be responsible for delivering effective and maintainable code while maintaining the IT Infrastructure."
                        }
                    ]
                    })


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9092)
