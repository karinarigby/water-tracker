# run.py
import logging
import os

from app import create_app

config_name = str(os.getenv("FLASK_CONFIG") or "default")
app = create_app(config_name)

# s

if __name__ == "__main__":
    app.run(host="0.0.0.0")
