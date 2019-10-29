import flask
from flask import request
from predictor_api import make_prediction, feature_names
from calculator_api import calculate_int, input_names, input_defaults

# Initialize the app

app = flask.Flask(__name__)

# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
@app.route("/")
def hello():
    return flask.send_file("static/html/index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    x_input, predictions = make_prediction(request.args)
    return flask.render_template('predictor.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions)

@app.route("/calculator", methods=["POST","GET"])
def calculate():
    i_input, matrix, appts = calculate_int(request.args)
    return flask.render_template('calculator.html',i_input=i_input,
                                 input_names=input_names,
                                 input_defaults=input_defaults,
                                 matrix = matrix,
                                 appts = appts)

# Start the server, continuously listen to requests.
# We'll have a running web app!

if __name__=="__main__":
    # For local development:
    #app.run(debug=True)
    # For public web serving:
    #app.run(host='0.0.0.0')
    app.run()
