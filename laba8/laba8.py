import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

seeds_df = pd.read_csv("pima-indians-diabetes.csv")

samples = seeds_df.values

mergings = linkage(samples, method='complete')

dendrogram(mergings, leaf_rotation=90, leaf_font_size=5)
plt.show()

X = seeds_df.iloc[:, :].values
y = seeds_df.iloc[:, 8].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=10)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix: \n", result)
result1 = classification_report(y_test, y_pred)
print("Classification Report: \n", result1)
result2 = accuracy_score(y_test, y_pred)
print("Accuracy:", result2)

knnr = KNeighborsRegressor(n_neighbors=10)
knnr.fit(X, y)
print("The MSE is:", format(np.power(y - knnr.predict(X), 2).mean()))
