# Python FastAPI Bigger Applications Template

![python](https://img.shields.io/badge/python-3.11.6-informational)
![fastapi-0.109.0-informational](https://img.shields.io/badge/fastapi-0.109.0-informational)
<a href="https://github.com/new?template_name=python-fastapi-bigger-applications-template&template_owner=kwame-mintah">
  <img src="https://img.shields.io/badge/use%20this-template-blue?logo=github">
</a>

This a template project, to demonstrate using FastAPI in a bigger application. The same file structure
has been followed as per FastAPI [docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

This repository is intended as a quick-start and includes the following:

- A `Dockerfile` to build the FastAPI application following [guidelines](https://docs.docker.com/develop/develop-images/guidelines/)
- `docker-compose.yml` file to build and start the application
- GitHub Action workflow to run linting and unit tests
- Pre-commit hooks to run on each commit
- Pydantic models as response models for endpoints
- Unit and feature tests for endpoints

## Usage

1. Install python packages used for the service

    ```console
   pip install -r requirements.txt
    ```
2. Run the FastAPI server, which will run on port 8000

    ```console
   python app/main.py
    ```
   Endpoint documentation are available on http://127.0.0.1:8000/docs

## Docker

Running the `docker-compose.yml`, will build a new image python-fastapi-bigger-applications-template-fastapi:latest
which will be used for the `fastapi` service within the container.

```console
docker-compose up -d
```

## Tests

Unit tests are located in `/tests/unit` directory, run unit tests using:

```console
pytest tests/unit
```

Additionally, a coverage report can be generated using [`pytest-cov`](https://pypi.org/project/pytest-cov/):

```console
pytest --cov=app tests/unit --cov-report=html:coverage_report
```

Will generate a coverage HTML file, in the `/coverage_report/` directory, simply open the `index.html` in your chosen web browser.

Integration tests are located in `/tests/integration` directory, run integration using:

```console
pytest tests/integration
```
