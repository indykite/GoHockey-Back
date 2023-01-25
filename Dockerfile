FROM python:3.11-alpine

# Inspired by https://sourcery.ai/blog/python-docker/

ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache git && \
    pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile* .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY . /usr/src/app

EXPOSE 8080

ENV PATH="/usr/src/app/.venv/bin:$PATH"

ENTRYPOINT ["python3", "-m", "openapi_server"]
