# main application file to execute

from app import create_app

application = create_app()


if __name__ == "__main__":
    application.run("0.0.0.0", 5002, debug=True)
