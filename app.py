from flask import Flask 


def create_app(app_name):
    app = Flask(app_name)
    return app


if __name__ == '__main__':
    app = create_app('My App')
    app.run(host='0.0.0.0', port=4999, debug=True)
