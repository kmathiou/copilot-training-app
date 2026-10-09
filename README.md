# FastAPI Starter

Run the development server from the project directory:

```sh
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000 for the home page or http://127.0.0.1:8000/docs for interactive API documentation.

## Tests

Run the unit tests with:

```sh
python -m unittest discover -s tests -v
```

## Container

Build and run the app locally with:

```sh
docker build -t copilot-training-app .
docker run --rm -p 8000:8000 copilot-training-app
```

The GitHub Actions workflow runs the tests on pull requests and pushes to `main`. After tests pass, it publishes the image to `ghcr.io/kmathiou/copilot-training-app` on pushes to `main` and version tags (`v*`). The `main` image is tagged `latest` and with the commit SHA.