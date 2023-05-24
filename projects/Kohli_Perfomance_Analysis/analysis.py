import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the csv file
df = pd.read_csv("D:\\Python_Winter_Training_2023\\day-09\\dataset.csv")
# print(df.head(10))

# find total number of runs Kohli has scored
totalRun = df["Runs"].sum()
noOfMatches = len(df["Runs"])
# print(f"Total no. of runs Kohli scored in {noOfMatches} matches : {totalRun}")

# Average of the number of runs he has scored
# avgRuns = df["Runs"].mean()
# print(
#     f"Total no. of average runs Kohli scored in {noOfMatches} matches : {int(avgRuns)}")

# Number of matches he has played at different position
positions = df["Pos"].unique()
# print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"

})

# print(df[["Runs","Pos","Opposition"]].head())
pos_count = df["Pos"].value_counts()
# print(pos_count)
# print(type(pos_count))

posValues = pos_count.values
posLables = pos_count.index
# print(posValues)

# fig = plt.figure(figsize=(10, 7))
# plt.pie(posValues,labels=posLables)
# plt.show()


# oponents = df["Opposition"].value_counts()
# grounds = df["Ground"].value_counts()
# posLables2 = oponents.index
# plt.pie(oponents.values, labels=posLables2)
# plt.show()


def show_pie_plot(df, key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_labels = counts.index

    fig = plt.figure(figsize=(10, 7))
    plt.pie(count_values, labels=count_labels)
    plt.show()


# show_pie_plot(df,"Pos")
# show_pie_plot(df, "Opposition")
# show_pie_plot(df, "Ground")

# print(oponents.values)


# Total runs scored in different positions
runs_at_pos = df.groupby("Pos")["Runs"].sum()
runs_at_values = runs_at_pos.values
runs_at_pos_lables = runs_at_pos.index

# fig = plt.figure(figsize=(10, 7))
# plt.pie(runs_at_values, labels=runs_at_pos_lables)
# plt.show()

# Total sixes scored wirh different oppositions
sixes_with_ops = df.groupby("Opposition")["6s"].sum()
sixes_with_ops_values = sixes_with_ops.values
sixes_with_ops_lables = sixes_with_ops.index

# fig = plt.figure(figsize=(10, 7))
# plt.pie(sixes_with_ops_values, labels=sixes_with_ops_lables)
# plt.show()

# Number of centuries scored by Kohli in first and second innings
centuries = df.query("Runs >=100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]
tons_t = centuries.groupby("Runs")["Inns"].value_counts()

# fig = plt.figure(figsize=(10,7))
# plt.bar(innings,tons,color="blue",width=0.2)
# plt.show()

# Calculate the dismissals of Kohli
dismissals = df["Dismissal"].value_counts()
print(dismissals)
dismissals_counts = dismissals.values
dismissals_labels = dismissals.index

# show_pie_plot(df,"Dismissal")

# Against which team he has scored the most runs
# fig = plt.figure(figsize=(10,7))
# plt.bar(
#     df["Opposition"],df["Runs"],color="red",width=0.2
# )
# plt.show()

#Against which teams he has scored the most centuries
fig = plt.figure(figsize=(10,7))
plt.bar(
    centuries["Opposition"],centuries["Runs"],color="green",width=0.2
)
plt.show()

#Analyze the strike rate
