import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok"}

@app.route("/info")
def info():
    return {
        "app": "Flask Render",
        "student": "TON_NOM",
        "version": "v1"
    }

@app.route("/env")
def env():
    return {"env": os.getenv("ENV")}

@app.route("/db")
def db():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
```

Et dans ton `Dockerfile`, assure-toi que `psycopg2` est installé. Vérifie ton `requirements.txt` :
```
flask
psycopg2-binary
```

---

### 4️⃣ React — Dans Render (interface)

Structure minimale à créer dans ton repo :
```
frontend/
├── package.json
├── public/
│   └── index.html
└── src/
    └── index.js
