from src.app import app, db

db.create_all()
app.run()