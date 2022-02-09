from flask import Flask, request
from backports.pbkdf2 import pbkdf2_hmac
import os, binascii
import hmac
import hashlib
import base64

secret_path = "/tmp/app/secret"
app_secret = open(secret_path).readline().rstrip() if os.path.exists(secret_path) else ""

# derive key based on configured APP_SECRET
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
secret = app_secret.encode("utf8")
key = pbkdf2_hmac("sha256", secret, salt, 4096, 32)

app = Flask(__name__)

@app.route("/")
def hello():
    message = request.args.get('message')
    if message is None:
        return "Give me a message and I'll sign it for you"
    else:
        h = hmac.new(key, message.encode(), hashlib.sha256)
        return "<b>Original message:</b> {}<br/><b>Signature:</b> {}".format(message, h.hexdigest())

if __name__ == "__main__":
    app.run()
