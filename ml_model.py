from sklearn.linear_model import LinearRegression
import numpy as np

# Fake historical data (demo purpose)
rainfall_data = np.array([2, 5, 10, 20, 30, 40]).reshape(-1, 1)
risk_data = np.array([3, 7, 15, 28, 45, 60])

model = LinearRegression()
model.fit(rainfall_data, risk_data)

def predict_risk_ml(rainfall):
    return model.predict([[rainfall]])[0]
