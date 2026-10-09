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

## Kubernetes

The Helm chart is in `charts/copilot-training-app`. Validate it with:

```sh
helm lint charts/copilot-training-app
helm template copilot-training-app charts/copilot-training-app
```

When ready to deploy, install it with:

```sh
helm upgrade --install copilot-training-app charts/copilot-training-app \
	--namespace copilot-training-app --create-namespace
```

The chart defaults to one replica because users are stored in memory. For a private GHCR package, configure an `imagePullSecrets` entry in a values file before installing.