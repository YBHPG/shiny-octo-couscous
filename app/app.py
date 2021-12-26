from flask import Flask, render_template, session
from scen_query.routes import query_app
from scen_auth.routes import auth_app
from scen_update.routes import update_app
from scen_cart.routes import cart_app
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['DB_CONFIG'] = json.load(open('configs/db.json'))
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))

app.register_blueprint(query_app, url_prefix='/query')
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(update_app, url_prefix='/update')
app.register_blueprint(cart_app, url_prefix="/cart")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exit')
def exit():
    session.clear()
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
