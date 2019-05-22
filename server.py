from bottle import route, run, view
from datetime import datetime as dt
from random import random
import os
from horoscope import generate_prophecies

@route("/")
@view("predictions")
def index():
    now = dt.now()

    x = random()

    return {
        "date": f"{now.year}-{now.month}-{now.day}",
        "predictions": generate_prophecies() ,
        "special_date": x > 0.5,
        "x": x,
    }


@route("/api/test")
def api_test():
    return {"test_passed": True}

@route('/static/<filename>')
def send_js(filename):
    return static_file(filename, root='static')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)

