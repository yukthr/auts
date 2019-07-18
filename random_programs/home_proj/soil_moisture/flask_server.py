from flask import Flask, request
from aws_pubsub import publish_aws
app = Flask(__name__)

@app.route("/moisture", methods=['GET','POST'])
def moisture_publish():

    req_data = request.get_json()
    moisture_value = req_data['moisture_value']
    publish_aws(moisture_value)
    return "aws message has now been publiesh"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
