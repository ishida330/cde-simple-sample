# cde-simple-sample
Simple Example of IBM cognos dashboard embedded

- Embedding "Whiteboard"(=Non Existing") Dashboard to WebApp.
- DataSource module: Japanese UTF-8 CSV ( json/CSVinfo_jp.json )
- DataSource data: Japanese UTF-8 CSV ( json/CSV_jp.csv )
 
- 


See Qiita Article :

- Flask/Python
- 

# How to run this in localhost
### 1. Clone this repo
git clone https://github.com/ishida330/cde-simple-sample.git
### 2. Change constant in run.py
api_endpoint_url/client_id/client_secret will be copied from Credentials of IBM cognos dashboard embedded service.

my_Flask_url = "http://localhost:5000"
api_endpoint_url = "https://us-south.dynamic-dashboard-embedded.cloud.ibm.com/daas"
client_id = "xxxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

### 3. Run App
type these command. 
set FLASK_APP=run.py
flask run

If you're using Windows, you can execute **go.bat** instead

Then 
 * Serving Flask app "run"
 * Forcing debug mode off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 ### 4. access http://127.0.0.1:5000/
 
