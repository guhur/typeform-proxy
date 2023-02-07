# TypeForm API Proxy

To use the TypeForm API in your client, you need to hide your personal access token.

This repo is simply acting as a proxy between TypeForm API and your proxy by injecting your personal access token on it. It allows you to control authorization, such as valid domain names.

Since our API relies on OpenAPI, documentation is automatically generated and it is available at api.yourdns.com/redoc or api.yourdns.com/docs.


## Installation with Docker

Copy the `.env` into `.env.local` with your own settings.

Then launch the dockers with:

`docker compose --env-file .env.local up -d`


## Deploy your project

See instructions in the [awesome-traefik](https://github.com/guhur/awesome-traefik) project.

## Run the tests

`docker/test.sh`


## Local development

1. Install [postgresql](https://www.postgresql.org/download/).

2. Install python 3.11.

3. Create a new virtual environment and activate it:


```bash
venv .venv
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

5. Copy `.env` into `.env.local` and edit environment variables


6. Start the server:

```
uvicorn app.main:app --reload --env-file .env.local
```

7. Visit the generated documentation:

```
http://127.0.0.1:8000/redoc
```

