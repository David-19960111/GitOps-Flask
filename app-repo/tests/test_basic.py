from app.main import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hola desde Flask" in r.data 