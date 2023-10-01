# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

ARG SERVER_PORT=8000
EXPOSE ${SERVER_PORT}

# Keeps Python from generating .pyc files in the container
ARG PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ARG PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /workspace
COPY . /workspace

# Creates a non-root user with an explicit UID and adds permission to access the /workspace folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /workspace
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD python ./app/manage.py runserver 0.0.0.0:${SERVER_PORT}
