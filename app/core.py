import os

def get_port():
    return int(os.getenv("PORT", "8000"))
