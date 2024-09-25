# Heart_Stroke_Detection_Using_ML

## <br>Semester 5 Mini Project for Vidyalankar Institute of Technology<br><br>

Dataset used - https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset<br>

The stroke-prediction dataset used in this project is a beginner-friendly, cleaned dataset with more than 5000 rows of data spread across 12 columns.<br><be>

## Methodology<be><br>

### 1) Data Exploration and Visualization:

Basic data exploration, Checking for unique values, etc.<br>
Checking the correlation of each feature with the target variable.<br>
This is done mainly to choose the top 5 variables to use for prediction<br>

### 2) Data Preprocessing and Preparation:

Splitting data into train and test split

### 3) Models - 

a) Linear Regression Model <br>
b) Gaussian Naive Bayes<br>
c) Multinomial Naive Bayes<br>
d) Decision Tree<br>
e) Support Vector Machine<br>
f) Random Forest Classifier<br>
g) XGBoost Classifier<br>

### 4) HyperParameter Tuning

Tried Hyperparameter tuning on SVC using RandomSearch and GridSearch but with limited success

### 5) Final Model

Based on the best scores seen, the XGBoost Classifier was chosen as the final model.<br>
The model was then exported via pickle and loaded into a front end to display as an application.


