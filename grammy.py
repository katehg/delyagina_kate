from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
app.debug = True

def get_data():
    url = "https://raw.githubusercontent.com/katehg/delyagina_kate/master/grammy_new.json"
    r = requests.get(url)
    return r.json()


@app.route('/')
def list_rows():
    our_data = get_data()
    return render_template('grammy_1.html', data=our_data)



if __name__ == '__main__':
    app.run()

