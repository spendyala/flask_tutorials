# Flask Tutorials

## About

This Flask Tutorial series uses `Python3.6`

## Prerequsites
- `python3.6`
- `virtualenv`
- `pip`

## Create virtual environment.
```
virtualenv -p `which python3` .venv
```

## Fetch requirements from `pip`
`pip freeze > requirements.txt`

## Install requirements.txt
`pip install -r requirements.txt`

## Run the server
`python hello.py`


## Some CLI commands we used
`curl -XGET http://127.0.0.1:9500/f_to_c/%20105%20`
`curl -XPOST http://127.0.0.1:9500/f_to_c/`

```
telnet 127.0.0.1 9500
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
POST /f_to_c/ HTTP/1.0
Host: 127.0.0.1:9500
Content-Length: 3

105
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 20
Server: Werkzeug/0.14.1 Python/3.6.5
Date: Mon, 18 Jun 2018 07:42:42 GMT

This is POST RequestConnection closed by foreign host.
```


## Warning
Please don't use `pdb` or `ipython` or `ipdb` in `requirements.txt` file

## Some important links
- http://flask.pocoo.org/docs/0.12/api/
- http://docs.python-requests.org/en/master/user/quickstart/#custom-headers
- https://en.wikipedia.org/wiki/JSON 
