from app import app
from app.routes.user_routes import user_bp
from app.routes.task_routes import task_bp

app.register_blueprint(user_bp)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)