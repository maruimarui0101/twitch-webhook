# import flask dependencies
from flask import Flask, request, make_response, jsonify, Response

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/callback', methods=['POST'])
def index():
    print(request.json)
    data = request.json['challenge']
    print(data)
    return make_response(data, 201)

if __name__ == "__main__":
    # Flask must run on 443 and on HTTPS as per requirement from Twitch
    app.run(ssl_context='adhoc', debug=True, port=443)