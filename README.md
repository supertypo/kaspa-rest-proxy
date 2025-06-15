# kaspa-rest-proxy

## Getting started

### Pre-packaged

[Docker image](https://hub.docker.com/r/kaspanet/kaspa-rest-proxy)
or check releases for uploads.

### From source

Python 3.12 and Git must be installed

Clone Git repository
```shell
git clone https://github.com/supertypo/kaspa-rest-proxy
```

Install Poetry
```shell
pip install poetry
```

Run Poetry install
```shell
poetry install
```

Run application
```shell
gunicorn --preload --worker-class=uvicorn.workers.UvicornWorker --bind=0.0.0.0:15110 --workers=2 --timeout=120 kaspa_rest_proxy.server:app -- -s ws://localhost:17110
```
Append --help at the end for more information
