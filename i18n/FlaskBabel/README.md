Flask-Babel is an extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and speaklater. It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to gettext translations.

Installation
Install the extension from PyPi:

$ pip install Flask-Babel

Configuration

To get started all you need to do is to instantiate a Babel object after configuring the application:

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
