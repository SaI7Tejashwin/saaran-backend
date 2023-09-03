# saaran-backend

This is a fastapi powered backend to test and deploy the text summarization model as a ML API.

## Project package manager setup
> This is a `poetry` setup project

To install poetry in your system, check this [Install Guide](https://python-poetry.org/docs/#installation)

All the required poetry commands listed [here](https://python-poetry.org/docs/cli/)

## Project Setup

To get started after cloning the project, run
```
poetry install
```

This will automatically create a virtualenv, which can be accessed by
```
poetry shell
```

execute `exit` in the shell (not `deactivate`) to quit out of the shell. Check out the [CLI documentation](https://python-poetry.org/docs/cli/) for more commands for poetry

> The backend is built using FastAPI

To run the server try out the command (at the root of the project):
```
uvicorn src.saaran_backend.main:app --reload
```

> Checkout the documentaion for more configurations on uvicorn and gunicorn server deployments.

## API Testing

Your locally hosted uvicorn server can be tested out on tools like Postman or Thunderclient-vscode-extention

Alternatively, try out <localhost-url>:<port>/docs (127.0.0.1:8000/docs) to test it in FastAPI's interactive API docs

### Summarization Testing
File summarization API is now up! To try out the summarization yourself, check out these endpoints

```
http://127.0.0.1:8000/predict/extract/<the-model-you-want-to-try>

```

The models you can try out now are `sumy_lex | sumy_luhn | sumy_kl | sumy_lsa`

## References

Referenced from the [Poetry](https://python-poetry.org/docs/) and [FastAPI](https://fastapi.tiangolo.com/) documentation

