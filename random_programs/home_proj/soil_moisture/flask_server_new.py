from flask import Flask, request
from aws_pubsub import publish_aws
app = Flask(__name__)
import ast # will be used to convert byte strings(in this dictionary is enclosed in string) to evaluate to dictionary
import json

@app.route("/moisture", methods=['GET','POST'])
def moisture_publish():

    req_data = request.get_data()
    dict_value = ast.literal_eval(req_data.decode("utf-8")) #We get byte string from the Microcontroller
    publish_aws(json.dumps(dict_value)) #We convert this into Json here instead of converting in AWS script
    return "aws message has now been published"

"""
updating influx and integrating with Grafana is the next step, probably just use the dict_value and upate Influx
appropriately

Dockerising flaks was not a problem at all, the problem was with AWS Pubsub, probably will give it another try

"""



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
