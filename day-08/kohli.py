import pandas as pd

df = pd.read_csv("D:\\Python_Winter_Training_2023\\day-08\\dataset.csv")
# print(df.head(10))
# print(df.tail(10))

# df.info()
# print(df.shape)
# print(df.describe())

# print(df["Opposition"].describe())


# print(df)
# print(df["Runs"].value_counts())

new_df = df[["Runs", "4s", "6s", "Opposition"]]

# print(new_df)
# print(new_df.describe())

# print(new_df.iloc[2])
# print(new_df.iloc[2:5])
# print(new_df.iloc[2:13]["Runs"])
# print(new_df.iloc[2:13]["6s"])

# print(df["Opposition"] == "v Australia")
vs_aussies = df[df["Opposition"] == "v Australia"]
# print(vs_aussies.head(10))
# print(vs_aussies["Runs"].sum())
# print(vs_aussies["6s"].sum())

# vs_aussies2 = df[df["Opposition"] == "v Australia" & df["Runs"] >= 100]
# centuries = vs_aussies[vs_aussies["Runs"] >= 100]
# print(centuries)

centuries = df[(df["Opposition"] == "v Australia") & (df["Runs"] >= 100)]
print(centuries)

def findCenturies(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"
df["Centuries"] = df["Runs"].apply(findCenturies)    

print(df)