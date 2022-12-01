from flask import *
import numpy as np
import joblib
import pandas as pd
import xgboost

app = Flask(__name__)

model = joblib.load("model_heartstroke.joblib")

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [int(x) for x in request.form.values()]
    df = pd.DataFrame(float_features)
    features = np.array(float_features)
    print(features)
    #print(df)
    prediction = model.predict([features])
    output= format(prediction)

    if output==0:
        return render_template("form.html", prediction_text = "chances of a heart stroke is low")
    elif output==1:
        return render_template("form.html", prediction_text = "chances of a heart stroke is High")

if __name__=="__main__":
    app.run(debug=True)
        