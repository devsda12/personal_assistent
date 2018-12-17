import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/lol', methods=['GET'])
def lol():
    if 'id' in request.args:
        id = str(request.args['id'])
        if id == "lolzo":
            return "ID is working (lolzo)"
        else:
            return "OTHER ID SPECIFIED"
    else:
        return "No ID field specified"


app.run()