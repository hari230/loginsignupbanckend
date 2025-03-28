from flask import Flask
# from routes.user_routes import user_routes
from flask_cors import CORS
from backend.routes.user_routes import user_routes
app = Flask(__name__)
CORS(app)
app.register_blueprint(user_routes, url_prefix="/auth")

@app.route("/")
def home():
    return {"message": "Welcome to Login and Signup API"}

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
