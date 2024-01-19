# Build a virtualenv using the appropriate Debian release
# * Install python3-venv for the built-in Python3 venv module (not installed by default)
# * Install gcc libpython3-dev to compile C Python modules
# * In the virtualenv: Update pip setuputils and wheel to support building new packages
FROM debian:12-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip3.11 install --no-build-isolation --disable-pip-version-check -r /requirements.txt
HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1"

# Copy the virtualenv into a distroless image
FROM gcr.io/distroless/python3-debian12:nonroot
COPY --from=build-venv /venv /venv
COPY . /app
WORKDIR /app
USER nobody
ENTRYPOINT ["/venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
