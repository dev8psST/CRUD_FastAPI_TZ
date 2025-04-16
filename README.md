# CRUD_FastAPI_TZ
Database run with docker-compose file.<br>
Install requirements<br>
<pre>DB
  user: root
  password: password
  DB: test
  host: mysql_db</pre>

#if you want use HTTPS local):
  $ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 30 -nodes
  $ uvicorn main:app --host 0.0.0.0 --port 4343 --ssl-keyfile=key.pem --ssl-certfile=cert.pem

#use uv , its fast and comfy:
  $ uv venv --python=3.13 <..name env..>
  $ uv pip install -r requirements.txt
  $ uv pip list

# run unicron :
  $ uvicorn main:app --workers 4 --loop uvloop --http httptools
  OR
  $ uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
