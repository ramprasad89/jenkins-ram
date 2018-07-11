#!/root/py3.7/bin/python

from flask import Flask
from flask import request
import json
import requests
#import pprint
#pp = pprint.PrettyPrinter()
app = Flask(__name__)

user = "pandar"
api_token = "11daf50680fbc304ba1ee49da101d26af3"
jenkins_url = "ec2-34-212-45-251.us-west-2.compute.amazonaws.com:8080"
job = "dev_host"
#auth_token = "e4BDh=#'oh53X_F;t8#Xk4>KnEnDJV"
auth_token = "abc123"
name = "Rinku"
repo_url = "https://github.com/ramprasad89/jenkins-ram.git"

@app.route('/github.php', methods=['POST'])
def json_POST():
    req_data = request.get_json()
#    pp.pprint(req_data)
    if req_data['ref'] == 'refs/heads/master' and req_data['repository']['name'] == 'jenkins-ram':
        exec_url = "http://{}:{}@{}/job/{}/buildWithParameters?token={}&name={}&$Repository={}".format(user,api_token,jenkins_url,job,auth_token,name,repo_url)
#        print(exec_url)
        response = requests.get(exec_url)
        if response.status_code == 201:
            build_no = response.headers['Location'].split('/')[5]
            print("Build no. [{}] has been triggered for job {}".format(build_no, job))
    return json.dumps(req_data)

if __name__=='__main__':
	app.run(host='172.31.42.178', port=80, debug=True)
