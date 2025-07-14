from flask import Flask
from app.routes import app as routes_blueprint

app = Flask(__name__)
app.secret_key = "your-secret-key"
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
