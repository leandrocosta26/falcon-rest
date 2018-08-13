### HUG REST

#### PRÉ REQ

`
Python 3.6 >~
Mongo
`

#### VIRTUALENV

```bash
$ cd falcon-rest
$ virtualenv -p python3 venv
$ pip install -r requirements.txt
```

#### RUN

```bash
$ gunicorn app:app
```


#### DEPENDECY

```bash
astroid==2.0.4
falcon==1.4.1
gunicorn==19.9.0
isort==4.3.4
lazy-object-proxy==1.3.1
marshmallow==2.15.4
mccabe==0.6.1
pylint==2.1.1
pymongo==3.7.1
python-mimeparse==1.6.0
six==1.11.0
typed-ast==1.1.0
wrapt==1.10.11
```