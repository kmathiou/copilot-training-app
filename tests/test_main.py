import unittest

from fastapi.testclient import TestClient

from main import app, users


class FastAPIAppTests(unittest.TestCase):
    def setUp(self) -> None:
        users.clear()
        self.client = TestClient(app)

    def test_home_links_to_snake_game_in_new_tab(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn('href="/snake-game" target="_blank"', response.text)

    def test_health_reports_ok(self) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_create_user_returns_created_user(self) -> None:
        response = self.client.post(
            "/users",
            json={"name": "Ada Lovelace", "email": "ada@example.com"},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
        )

    def test_create_user_requires_email(self) -> None:
        response = self.client.post("/users", json={"name": "Ada Lovelace"})

        self.assertEqual(response.status_code, 422)

    def test_snake_game_serves_local_page(self) -> None:
        response = self.client.get("/snake-game")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Snake / After hours", response.text)


if __name__ == "__main__":
    unittest.main()