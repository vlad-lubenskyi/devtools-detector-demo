import os

from flask import Flask, send_from_directory, make_response

app = Flask(__name__)

CONTENT_ROOT = os.path.join(os.getcwd(), 'static')


@app.route('/<path:filename>', methods=['GET'])
def serve_static_file(filename):
    response = make_response(send_from_directory(CONTENT_ROOT, filename))

    if filename.endswith(".map"):
        # When the source map is requested, respond a special cookie.
        response.set_cookie("dev_tools", "true")
    return response


if __name__ == '__main__':
    app.run(debug=True)
