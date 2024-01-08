from flask import Flask
from apis import user

app = Flask(__name__)

app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
