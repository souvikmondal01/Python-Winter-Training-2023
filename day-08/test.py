import pandas as pd

data = {
    "apples": [4, 2, 6, 5],
    "bananas": [1, 3, 2, 6]
}


# print(purchases)
# print(type(purchases))

# print(purchases["apples"])

index = ["Aaron", "Lee", "Steve", "Shaun"]
purchases = pd.DataFrame(data, index=index)
# print(purchases)
print(purchases.loc["Aaron"])


