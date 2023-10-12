from flask.cli import FlaskGroup

from questions import app


cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()