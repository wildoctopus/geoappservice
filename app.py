# main application file to execute

from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
