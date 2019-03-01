import requests;
from flask import Flask,request;
import json;
import http;

app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return 'from '+request.base_url

# @app.route('/test',methods=['GET'])
# def te():
#     print('send successfull '+request.args.get('name')+' ')
#     return 'test',200

@app.route('/name',methods=['GET','POST','DELETE'])
def name():
    with open('test.json') as json_file:
        data=json.load(json_file)
        for i in data:
            requests.get(url=i['host'],params={'from':request.base_url})
    return 'ok'
app.run(debug=True,host='0.0.0.0',port=3000)