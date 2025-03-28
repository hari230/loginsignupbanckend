from flask import Flask
# from routes.user_routes import user_routes

from backend.routes.user_routes import user_routes


app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix="/auth")

@app.route("/")
def home():
    return {"message": "Welcome to Flask Auth"}

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
