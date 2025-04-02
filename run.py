import sys

print("Rodando run.py correto!", file=sys.stderr)
from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(3000), debug=True, use_reloader=False)