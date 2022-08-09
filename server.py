from models import create_app, db

app = create_app()


@app.route('/')
def home():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    db.create_all()
    app.run()