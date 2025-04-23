# Absolutely! Here's a barebones end-to-end ML pipeline using all open-source tools that you can run locally. It does 3 key things:

# Trains a tiny model (scikit-learn)

# Packages it with FastAPI (for deployment)

# Uses Docker (for scalable deployment anywhere: cloud, Kubernetes, etc.)

# 🚀 Overview:
# Model: Logistic Regression on the Iris dataset

# API: FastAPI

# Deployment infrastructure: Docker


#Step 1: Train and Save the Model (train_model.py)



# train_model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model to file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


    