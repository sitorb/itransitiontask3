
import math
import re

from flask import Flask, Response, request

app = Flask(__name__)


@app.get("/<email_slug>")
def calculate_lcm_endpoint(email_slug):
    x = request.args.get("x", "")
    y = request.args.get("y", "")

    if not re.fullmatch(r"[0-9]+", x):
        return Response("NaN", mimetype="text/plain")

    if not re.fullmatch(r"[0-9]+", y):
        return Response("NaN", mimetype="text/plain")

    result = math.lcm(int(x), int(y))

    return Response(str(result), mimetype="text/plain")
