#!/usr/bin/python3
from flask import Flask, request, json, Response
from MongoDao import MongoDao
from bson import json_util
import os

app = Flask(__name__)
logger = app.logger
db = MongoDao();


@app.route("/token")
def getToken():
    logger.debug("Get Token");
    key = request.args.get('key');
    secret = request.args.get('secret');
    dao = db.get_connection()
    result = dao.authenticateClient(key, secret);
    if result:
        return Response(json_util.dumps({"token":result}), status=201);
    else:
        return Response(status=401);


@app.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(service="auth",healthy='true');


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
