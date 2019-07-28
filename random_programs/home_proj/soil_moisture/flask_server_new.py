from flask import Flask, request
from aws_pubsub import publish_aws
app = Flask(__name__)
import ast # will be used to convert byte strings(in this dictionary is enclosed in string) to evaluate to dictionary
import json
from datetime import datetime
from influxdb import InfluxDBClient


def write_to_influx(dvalue):
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    client = InfluxDBClient('192.168.0.151',8086)
    client.switch_database('moisture_value')
    json_body = [
        {
            "measurement": "moisture_value",
            "tags": {
            "name":"moisture_value_basil_bedroom",
            },
            "time": current_time,
            "fields":
                dvalue, #This has to be in { ] brackets but since dictionary already has it, we are skipping it
        },]
    client.write_points(json_body)
    print("writtent to influx {}".format(dvalue))

@app.route("/moisture", methods=['GET','POST'])
def moisture_publish():

    req_data = request.get_data()
    dict_value = ast.literal_eval(req_data.decode("utf-8")) #We get byte string from the Microcontroller
    print(dict_value)
    try:
        write_to_influx(dict_value)
        publish_aws(json.dumps(dict_value)) #We convert this into Json here instead of converting in AWS script
    except:
        write_to_influx(dict_value)
        publish_aws(json.dumps(dict_value))
    return "aws message has now been published"

"""
updating influx and integrating with Grafana is the next step, probably just use the dict_value and upate Influx
appropriately

Dockerising flaks was not a problem at all, the problem was with AWS Pubsub, probably will give it another try

"""



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
