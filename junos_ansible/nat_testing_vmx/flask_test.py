from flask import Flask,render_template,request
app = Flask(__name__)
import dynamo_4
from dynamo_4 import response_data,build_yaml,generate_config,invoke_ansible,final_update_dynamo,cleanup
from dynamo_4 import table
import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime

dt_iso = datetime.datetime.now().isoformat()

@app.route("/",methods=['GET','POST'])
def response_data():
    if request.method == 'POST':
        Public_IP = request.form['Public_IP']
        Private_IP = request.form['Private_IP']
        return dynamo_4.response_data(Public_IP,Private_IP)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
