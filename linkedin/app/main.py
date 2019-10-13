from flask import Flask
from flask import jsonify
# Description: Simulates a real-world API that returns a list of job posts
app = Flask(__name__)
@app.route("/", methods=['GET'])
def default():
    return jsonify({"source": "linkedin",
                    "jobs":
                    [
                        {
                            "title": "Google Cloud DevOps Engineer",
                            "description": "As a DevOps Engineer, you make sure the company’s e-commerce website infrastructure can grow fast and sustainable way which is crucial to our success and future. You will have the opportunity to learn and develop, with a focus on the automation within different departments of the company."
                        },
                        {
                            "title": "DevOps Engineer",
                            "description": "In this role, you’ll ensure our infrastructure scales with our growth. Your job is to keep our ridiculously high-quality bar set ridiculously high, and to help us identify and execute ways to raise it even higher."
                        },
                        {
                            "title": "Azure DevOps Engineer",
                            "description": "Our clients are building innovative solutions within the financial sector. Even with crypto currencies on the rise, the financial sector is still creating new fintech’s, payment offerings, crowdfunding platforms and e-commerce integrations into other value chains. They build, consume and integrate api’s to create innovative new services. Our European based team of tech enthusiasts are looking for an experienced engineer to join their eager and highly skilled team. As a key member of the engineering team, you will work on all aspects of product development. Which includes design, develop, prototype, write interface specifications, implement, debug, maintain current code, write new code, review code and test. Interact with customers and product management to understand requirements and develop innovative solutions that create a smile on our customers face. You will complete complex technical assignments with your empowered agile team. You will mentor junior developers and guide them on complex aspects and do regular code reviews. Are you able to shape and create a product strategy? To help define the product features, refine system architecture, and spearhead the best practices. Then this is the job for you"
                        }
                    ]
                    })


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9093)
