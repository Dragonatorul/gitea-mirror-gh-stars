# Gitea Mirror GH Stars

A lightweight Python utility to automatically mirror your starred GitHub repositories to a self-hosted Gitea instance.

## Features

- 🌟 **Automatic Mirroring**: Automatically creates live mirror repositories in Gitea for every repository you star on GitHub.
- 🔁 **Idempotent Sync**: Checks existing Gitea repositories and skips repositories that have already been mirrored.
- 🐳 **Docker Ready**: Pre-built container images available on GitHub Container Registry (`ghcr.io`).

## Configuration

Copy the example environment file:

```bash
cp example.env .env
```

Configure your credentials in `.env`:

| Environment Variable | Description | Example |
| :--- | :--- | :--- |
| `GITHUB_USER` | Target GitHub username whose starred repos to mirror | `octocat` |
| `GITEA_TOKEN` | Gitea Personal Access Token (*Settings ➔ Applications*) | `a1b2c3d4e5f6...` |
| `GITEA_HOST` | Full URL of your self-hosted Gitea instance | `https://gitea.example.com` |

## Usage

### Option 1: Using Docker Compose (Recommended)

1. Ensure `.env` is populated with your settings.
2. Run the synchronization:
   ```bash
   docker-compose up
   ```

### Option 2: Running Directly with Python

1. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python3 src/main.py
   ```

## Automation

You can schedule periodic runs using cron or a systemd timer to keep your Gitea mirrors updated with your latest GitHub stars.
