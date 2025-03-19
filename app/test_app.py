import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.dirname(__file__) + "/..")
)  # ✅ Still before any imports

from app.server import app  # ✅ Now correctly placed after sys.path modification


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
