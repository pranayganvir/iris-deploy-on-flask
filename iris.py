# %%
import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt 
import pickle
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

# %%
from sklearn.datasets import load_iris

# %%
iris = load_iris()

# %%
X = iris.data

# %%
y = iris.target

# %%


# %%
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)

# %%


# %%


# %%
hyperparameters = {'n_estimators':list(range(0,10)),'max_depth':list(range(0,10))}

# %%
model = GridSearchCV(RandomForestClassifier(), hyperparameters)

# %%
model.fit(X_train,y_train)

# %%
model.best_params_

# %%
model.best_score_

# %%
y_pred = model.predict(X_test)

# %%
print(classification_report(y_test, y_pred))

# %%
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# %%
model.predict([[6.3	,3.3,	6,2.5]])

# %%
X_test

# %%
