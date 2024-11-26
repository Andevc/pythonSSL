from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola con HTTPS :3 "


if __name__ == '__main__':
    app.run(ssl_context=('ssl/web/server_web.crt', 'ssl/web/server_web.key'), debug=True)

