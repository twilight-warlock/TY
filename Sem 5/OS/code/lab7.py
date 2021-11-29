import pandas as pd
noOfProcessors = int(input("Enter Number Of Processors: "))
columns = ["Processor", "Arrival Time",
           "Burst Time", "Waiting Time", "Turn-around Time"]
df = pd.DataFrame(columns=columns, index=[i for i in range(noOfProcessors)])

for i in range(noOfProcessors):
    arrival = int(input("Enter Arrival Time of Processor "+str(i)+": "))
    burst = int(input("Enter Burst Time of Processor "+str(i)+": "))
    df.loc[i] = ["P"+str(i), arrival, burst, 0, 0]

df.sort_values(by=["Arrival Time"], inplace=True)
start_time = df["Arrival Time"].tolist()[0]
waiting_time = [0]

for i in range(noOfProcessors-1):
    time = start_time
    for j in range(i+1):
        time += df["Burst Time"].tolist()[j]
    time -= df["Arrival Time"].tolist()[i+1]
    waiting_time.append(time)

df["Waiting Time"] = waiting_time

turn_time = []
for i in range(noOfProcessors):
    time = start_time
    for j in range(i+1):
        time += df["Burst Time"].tolist()[j]
    time -= df["Arrival Time"].tolist()[i]
    turn_time.append(time)

df["Turn-around Time"] = turn_time
print(df)

mean_wt = df['Waiting Time'].mean()
mean_tt = df['Turn-around Time'].mean()

print("Average waiting time = " + str(mean_wt))
print("Average turn around time = "+str(mean_tt))
