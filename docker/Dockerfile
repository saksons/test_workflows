FROM python:3.11.6-slim-bullseye AS builder

ENV HOST="127.0.0.1"\
    PORT="50900"\
    POETRY_VERSION=1.8.2\
    POETRY_VIRTUALENVS_IN_PROJECT=false\
    PIP_ROOT_USER_ACTION=ignore

WORKDIR /api

COPY ./api/poetry.lock ./api/pyproject.toml ./

# installing & configuration poetry
RUN pip install --upgrade pip \ 
    && python -m pip install --root-user-action=${PIP_ROOT_USER_ACTION} --no-cache-dir poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.in-project ${POETRY_VIRTUALENVS_IN_PROJECT} \
    && poetry install --no-interaction --no-ansi


FROM builder AS testing

COPY ./api/api/ ./api/
COPY ./api/tests/ ./tests/ 

# RUN poetry run pytest
CMD poetry run pytest
