from flask import *
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

#model = joblib.load("model_heartstroke.joblib")
model = pickle.load(open("pickled.pkl","rb"))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')    

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = np.array(float_features)
    df = pd.DataFrame([features], columns = ['age','hypertension','heart_disease','ever_married','avg_glucose_level'])
    print(df)
    #print(df)
    prediction = model.predict(df)
    output= prediction[0]
    #prediction[0]

    if output==0:
        return render_template("form.html", prediction_text = "chances of a heart stroke is low")
    elif output==1:
        return render_template("form.html", prediction_text = "chances of a heart stroke is High")

if __name__=="__main__":
    app.run(debug=True)
        