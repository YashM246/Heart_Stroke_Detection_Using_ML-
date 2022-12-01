import pandas as pd
import joblib 
import numpy as np
import xgboost as xgb
import pickle

#model = joblib.load("model_heartstroke.joblib")
#model = pickle.load(open("pickled_xgc.pkl","rb"))
modeljson = xgb.Booster()
modeljson.load_model("model_json_xgc.json")
filename = 'final_model.sav'
pickle.dump(modeljson, open(filename,"wb"))
loaded_model = pickle.load(open(filename,"rb"))
#float_features = [ 20 ,  1 ,  0 ,  1 , 200 ]
data={
  "age": [42.0],
  "hypertension": [0.0],
  "heart_disease":[0.0],
  "ever_married":[1.0],
  "avg_glucose_level":[82.67]
}
features = pd.DataFrame(data)
print(features)
# prediction =
print(loaded_model.predict(features))
#output= format(prediction)
#print(output)