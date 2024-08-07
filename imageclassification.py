import numpy as np
from sklearn.datasets import load_sample_image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


china = load_sample_image("china.jpg")
flower = load_sample_image("flower.jpg")


data = np.array([china, flower])
n_samples, height, width, channels = data.shape


X = data.reshape((n_samples, -1))
y = np.array([0, 1]) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=0)


clf.fit(X_train, y_train)


accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
