from http import HTTPStatus

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id == '1':
        data = {'name': 'Datta Tembare'}
        # send response with status code 200
        return jsonify(data), HTTPStatus.OK

    # return error message with status code 404 if security key is invalid
    return "User not found", HTTPStatus.NOT_FOUND


@app.route("/user", methods=["POST"])
def create_user():
    key = request.headers.get('sec-key')
    if key == 'my_sec_key':
        # create response object
        res = Response()
        # set response headers
        res.headers['res_headers'] = 'successful_res'
        # set response data
        res.data = request.data
        # send response with status code 201
        return res, HTTPStatus.CREATED

    # return error message with status code 404 if security key is invalid
    return {"error": "Invalid Sec key"}, HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run()
