from pathlib import Path

from fastapi import FastAPI, status
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="FastAPI Starter", version="0.1.0")
users: list[dict[str, str | int]] = []
SNAKE_GAME_PAGE = Path(__file__).resolve().parent / "snake-game.html"


class UserCreate(BaseModel):
  name: str
  email: str


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> dict[str, str | int]:
  new_user = {"id": len(users) + 1, "name": user.name, "email": user.email}
  users.append(new_user)
  return new_user


@app.get("/snake-game", include_in_schema=False)
async def snake_game() -> FileResponse:
  return FileResponse(SNAKE_GAME_PAGE)


@app.get("/", response_class=HTMLResponse)
async def home() -> str:
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FastAPI Starter</title>
    <style>
      body { margin: 0; font: 16px/1.5 -apple-system, BlinkMacSystemFont, sans-serif; color: #17212b; background: #f4f7f5; }
      main { max-width: 720px; margin: 12vh auto; padding: 0 24px; }
      h1 { margin-bottom: 8px; font-size: 2.5rem; }
      p { color: #52616b; }
      nav { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
      a { padding: 10px 14px; border-radius: 5px; color: white; background: #087f69; text-decoration: none; }
      a:hover { background: #066653; }
      a:focus-visible { outline: 3px solid #17212b; outline-offset: 3px; }
    </style>
  </head>
  <body>
    <main>
      <h1>FastAPI is running</h1>
      <p>Your Python API is ready. Explore the interactive docs or check its health.</p>
      <nav><a href="/docs">API documentation</a><a href="/health">Health check</a><a href="/snake-game" target="_blank" rel="noopener noreferrer">Play Snake <span aria-hidden="true">&#8599;</span></a></nav>
    </main>
  </body>
</html>"""


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}