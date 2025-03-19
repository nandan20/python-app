import sys
import os
from app.server import app  # This import must be at the top

# Ensure the app/ directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
