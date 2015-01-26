#!/usr/bin/env python
# encoding: utf-8

import os
from bottle import get, route, run

path = os.path.dirname(__file__)


@route("/time")
def time():
    with open(os.path.join(path, "resources", "time.txt"), "rt") as fp:
        return fp.read()


if __name__ == "__main__":
    run(host="0.0.0.0", port=7315)
