import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import brier_score_loss
import matplotlib.pyplot as plot

data = pd.read_csv("HeartDisease.csv")

data.head()

X = data.drop('target', axis=1)
y = data.target

X = X.as_matrix()
y = y.as_matrix()

kfold = KFold(n_splits=3)

logistic_regression = LogisticRegression()
ada_boost_classifier = AdaBoostClassifier(n_estimators=50, learning_rate=1)

accuracy_score_logi, accuracy_score_ada = 0, 0
balanced_score_logi, balanced_score_ada = 0, 0
avg_precision_score_logi, avg_precision_score_ada = 0, 0
brier_score_logi, brier_score_ada = 0, 0

for train, test in kfold.split(X):
    
    train_X, test_X = X[train], X[test]
    train_y, test_y = y[train], y[test]
    
    logistic_regression.fit(train_X, train_y)
    ada_boost_classifier.fit(train_X, train_y)
    
    pred_logi = logistic_regression.predict(test_X)
    pred_ada = ada_boost_classifier.predict(test_X)
    
    x_axis = range(test_y.size)
    
    plot.scatter(x_axis, test_y, color = 'green')
    plot.scatter(x_axis, pred_logi, color = 'red')
    plot.scatter(x_axis, pred_ada, color = 'blue')
    plot.show()
        
    temp_accuracy_score_logi = accuracy_score(test_y, pred_logi)
    temp_accuracy_score_ada = accuracy_score(test_y, pred_ada)
    temp_balanced_accuracy_score_logi = balanced_accuracy_score(test_y, pred_logi)
    temp_balanced_accuracy_score_ada = balanced_accuracy_score(test_y, pred_ada)
    temp_avg_precision_score_logi = average_precision_score(test_y, pred_logi)
    temp_avg_precision_score_ada = average_precision_score(test_y, pred_ada)
    temp_brier_score_logi = brier_score_loss(test_y, pred_logi)
    temp_brier_score_ada = brier_score_loss(test_y, pred_ada)
    
    accuracy_score_logi += temp_accuracy_score_logi
    accuracy_score_ada += temp_accuracy_score_ada
    balanced_score_logi += temp_balanced_accuracy_score_logi
    balanced_score_ada += temp_balanced_accuracy_score_ada
    avg_precision_score_logi += temp_avg_precision_score_logi
    avg_precision_score_ada += temp_avg_precision_score_ada
    brier_score_logi += temp_brier_score_logi
    brier_score_ada += temp_brier_score_ada

print("Accuracy score of Logistic Regression")
print(accuracy_score_logi/3)
print("Accuracy score of AdaBoost Classifier")
print(accuracy_score_ada/3)

print("Balanced accuracy score of Logistic Regression")
print(balanced_score_logi/3)
print("Balanced accuracy score of AdaBoost Classifier")
print(balanced_score_ada/3)

print("Average precision score of Logistic Regression")
print(avg_precision_score_logi/3)
print("Average precision score of AdaBoost Classifier")
print(avg_precision_score_ada/3)

print("Brier score loss of Logistic Regression")
print(brier_score_logi/3)
print("Brier score loss of AdaBoost Classifier")
print(avg_precision_score_ada/3)