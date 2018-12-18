#
from flask import Flask, render_template
import json
import urllib.request
import base64

# urllib.error.URLError
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>
# https://shinespark.hatenablog.com/entry/2015/12/06/100000
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

# コンスタント
my_Flask_url = "http://localhost:5000"
api_endpoint_url = "https://us-south.dynamic-dashboard-embedded.cloud.ibm.com/daas"
client_id = "xxxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

@app.route("/")
def index():
    client = client_id+":"+client_secret
    encoded_client = base64.b64encode(client.encode('utf-8')).decode('utf-8')
    url = api_endpoint_url+'/v1/session'
    data = {
      "expiresIn": 3600,
      "webDomain": my_Flask_url
    }
    headers = {
        'Content-Type': 'application/json',
        'authorization': 'Basic ' + encoded_client
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
        body = json.loads(body)
    print(body["sessionId"])
    print(body["sessionCode"])
    return render_template('index.html', 
            sessionCode = body["sessionCode"])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
