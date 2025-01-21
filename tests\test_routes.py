class TestHealthcheck:
    def test_healthcheck_with_success(self, client):
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}