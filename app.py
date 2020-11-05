from flask import Flask, request
from flask_appconfig import AppConfig
import json
import log

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is Github listener server'


@app.route('/api/github-webhook', methods=['POST'])
def github_webhook():
    request_data = request.json
    if not request_data:
        return "JSON data is expected", 400

    log.info("Headers from Github:\n" + json.dumps(dict(request.headers), indent=4, sort_keys=False))
    log.info("Payload from Github:\n" + json.dumps(request_data, indent=4, sort_keys=False))
    return "OK", 200


if __name__ == '__main__':
    AppConfig(app, configfile="config.py")
    app.config['SECRET_KEY'] = 'S3cr3t!'
    app.run(host='0.0.0.0', port=9000)
