# Python FastAPI Bigger Applications Template

![fastapi-0.103.2-informational](https://img.shields.io/badge/fastapi-0.103.2-informational)

This a template project, to demonstrate using FastAPI in a bigger application. The same file structure
has been followed as per FastAPI [docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/). Additionally,
a `Dockerfile` has been created so FastAPI can be run within a docker container.

## Usage

1. Install python packages used for the service
    ```console
   pip install - requirements.txt
    ```
2. Run the FastAPI server, which will run on port 8000
    ```console
   python app/main.py
    ```
   Endpoint documentation are available on http://127.0.0.1:8000/docs

## Docker

Running the `docker-compose.yml`, will build a new image python-fastapi-bigger-applications-template-fastapi:latest
which will be used for the `fastapi` service within the container.

```commandline
docker-compose up -d
```

## Tests

Unit tests are located in `/tests` directory.

``console
pytest
``
