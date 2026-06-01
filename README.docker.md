# Docker Setup — Lightweight App Container

## Quick Start

Ensure Ollama is running on your host first:

```bash
ollama serve
```

Then build and run the container:

```bash
docker compose build
docker compose up
```

The app will be available at `http://localhost:5173` and the WebSocket backend at `ws://localhost:9876`.

## Prerequisites

- **Ollama** running on the host (not in Docker)
- Pull a model: `ollama pull llama3`
- The app expects Ollama at `http://host.docker.internal:11434`

## Environment Variables

Customize by setting environment variables before running:

```bash
export ROBOT_IP=172.168.10.2
export ROBOT_PORT=4880
export FRONTEND_HOST=0.0.0.0
export FRONTEND_PORT=5173
export BACKEND_PORT=9876
export OLLAMA_HOST=http://host.docker.internal:11434
export OLLAMA_MODEL=llama3

docker compose up
```

Or edit `docker-compose.yml` directly.

## Stop the Container

```bash
docker compose down
```

## Network Notes

- **Robot Access**: The container needs network access to your FANUC robot at `ROBOT_IP:ROBOT_PORT`.
- **Ollama**: Uses `host.docker.internal` to reach Ollama on your Mac/host machine. On Linux, use `--network host` or adjust the `OLLAMA_HOST`.
- **Voice Input**: Audio passthrough requires special Docker configuration; disable voice in the app if unavailable in the container.
