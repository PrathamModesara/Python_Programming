#data science fundamental with python

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1️⃣ NUMPY (Numerical Computing)

print("===== NUMPY =====")
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# 2️⃣ PANDAS (Data Handling)

print("\n===== PANDAS =====")

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 40, 50, 55, 65, 70]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# 3️⃣ DATA CLEANING

print("\n===== DATA CLEANING =====")

df.loc[2, "Marks"] = np.nan 
print("\nWith Missing Value:")
print(df)

df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print("\nAfter Filling Missing Value:")
print(df)

# 4️⃣ VISUALIZATION

print("\n===== VISUALIZATION =====")

plt.scatter(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

sns.regplot(x="Hours_Studied", y="Marks", data=df)
plt.title("Regression Plot")
plt.show()

# 5️⃣ MACHINE LEARNING (Linear Regression)

print("\n===== MACHINE LEARNING =====")

X = df[["Hours_Studied"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

print("\nPrediction for 7 hours study:")
print("Predicted Marks:", model.predict([[7]])[0])