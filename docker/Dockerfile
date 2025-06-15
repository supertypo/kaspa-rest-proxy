##
# builder image
##
FROM python:3.12-slim AS builder

ARG REPO_DIR=.

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /work

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

COPY "$REPO_DIR" .

RUN poetry install --only main


##
# runtime image
##
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /work/kaspa_rest_proxy /app/kaspa_rest_proxy

USER 13337:13337

ARG VERSION
ENV VERSION=$VERSION

ENTRYPOINT ["gunicorn", "--preload", "--worker-class=uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:15110", "--workers=2", "--timeout=120", "kaspa_rest_proxy.server:app", "--"]
CMD []
