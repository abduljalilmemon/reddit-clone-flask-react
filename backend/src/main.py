from flask import Flask, render_template
from apis import user


PATH = "../../frontend"
app = Flask(__name__, static_folder=f"{PATH}/dist/static", template_folder=f"{PATH}/dist", static_url_path="/static")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
