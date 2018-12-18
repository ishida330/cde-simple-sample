# cde-simple-sample
Simple Example of IBM cognos dashboard embedded App

- Embedding "Whiteboard"(=Non Existing") Dashboard to WebApp.
- DataSource module: Japanese UTF-8 ( json/CSVinfo_jp.json )
- DataSource data: Japanese UTF-8 CSV ( json/CSV_jp.csv )

Please see Qiita Article :


# How to run this app in localhost
### 1. Clone this repo
`git clone https://github.com/ishida330/cde-simple-sample.git`

### 2. Change constant in run.py

![image](https://qiita-image-store.s3.amazonaws.com/0/108535/535ca791-fcb7-f753-dfb3-0b3fb5ad4696.png)
api_endpoint_url/client_id/client_secret should be copied from Service Credentials of IBM cognos dashboard embedded service.

- my_Flask_url = "http://localhost:5000" ( <---change this to fit your env if you need )
- api_endpoint_url = "https://xxxxxx.dynamic-dashboard-embedded.cloud.ibm.com/daas"
- client_id = "xxxxxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxxx"
- client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

### 3. Run the App
type these command.

`set FLASK_APP=run.py`
`flask run`

If you're using Windows, you can execute **go.bat** instead

Then you will see
```
 * Serving Flask app "run"
 * Forcing debug mode off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
``` 
 ### 4. access the app 
 open any browsser and type http://127.0.0.1:5000/

![](https://qiita-image-store.s3.amazonaws.com/0/108535/9ca061c0-50d8-0798-4cc4-d182a3fec685.gif) 

That's all. Have Fun!
