from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd

# This is the a student dataset form kaggle datasets
df = pd.read_csv("Student_Performance.csv")

# Setting features and Target
features = ['Hours Studied', 'Previous Scores', 'Sleep Hours','Extracurricular Activities', 'Sample Question Papers Practiced']
target = 'Performance Index'
X = df[features]
y = df[target]

# Simple Encoding of Extracurriculat Activites Column
X.loc[:,'Extracurricular Activities'] = X.loc[:,'Extracurricular Activities'].map(lambda x: 1 if x=="Yes" else 0)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

model = RandomForestRegressor(n_estimators=300, random_state=0)
model.fit(X_train, y_train)
predictions = model.predict(X_valid)


# Model Validation
print("First 5 Samples of Actual Target Data: \n", y_valid.values[:5])
print("First 5 Samples of Model Predictions: \n", predictions.round(2)[:5])
print("Final mean absolute error: ", mean_absolute_error(predictions, y_valid))