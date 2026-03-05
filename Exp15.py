# Write the python program to implement Decision Tree 
from sklearn.tree import DecisionTreeClassifier
X = [
    [25, 50000],
    [30, 60000],
    [45, 80000],
    [35, 65000]
]
Y = [0, 0, 1, 1]
model = DecisionTreeClassifier()
model.fit(X, Y)
test = [[40, 70000]]
prediction = model.predict(test)
print("Test Input (Age, Salary):", test[0])
print("Predicted Class:", prediction[0])
if prediction[0] == 1:
    print("Interpretation: Based on the trained Decision Tree model,")
    print("the customer is likely to BUY the product.")
else:
    print("Interpretation: Based on the trained Decision Tree model,")
    print("the customer is NOT likely to buy the product.")