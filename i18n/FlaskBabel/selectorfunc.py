from flask import g, request


@babel.localeselector
def get_locale():
    #if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    #otherwise try to guess the language from the user accept
    #header the browser transmits. We support de/fr/en in this
    # example. the best match wins.
    return request.accept_languages.best_match(['de', 'fr', 'en'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
#above example assumes that the current user is stored on the flask.g object

