import pandas as pd

noOfProcessors = int(input("Enter Number of Processors: "))
columns = ["Processor", "Arrival Time", "Burst Time",
           "Completion Time", "Waiting Time", "Turn-around Time"]

df = pd.DataFrame(columns=columns, index=[i for i in range(noOfProcessors)])

for i in range(noOfProcessors):
    arrival = int(input("Enter Arrival Time of Processor "+str(i)+": "))
    burst = int(input("Enter Burst Time of Processor "+str(i)+": "))
    df.loc[i] = ["P"+str(i), arrival, burst, 0, 0, 0]

df.sort_values(by=["Arrival Time"], inplace=True)

timestamp = int(input("Enter Timestamp: "))
print("Timestamp: "+str(timestamp))
start_time = df["Arrival Time"].tolist()[0]

dictionary = df[['Processor', 'Arrival Time', 'Burst Time']].to_dict("records")

processor1 = df["Processor"].tolist()[0]
queue = [processor1]

df.set_index("Processor", inplace=True)

t = start_time
total_time = df[['Burst Time']].sum()

burst_time = df[["Burst Time"]]
time = start_time+total_time
while(t < time).bool():
    current = queue.pop(0)
    if(df.loc[current, 'Burst Time'] >= timestamp):
        t += timestamp
        df.loc[current, 'Burst Time'] -= timestamp
        for pr in dictionary:
            if (pr['Arrival Time'] > t-timestamp and pr['Arrival Time'] <= t):
                queue.append(pr['Processor'])
        if(df.loc[current, 'Burst Time'] == 0):
            df.loc[current, 'Completion Time'] = t
        else:
            queue.append(current)
    else:
        t += df.loc[current, 'Burst Time']
        df.loc[current, 'Completion Time'] = t
        for pr in dictionary:
            if (pr['Arrival Time'] > t-timestamp and pr['Arrival Time'] <= t):
                queue.append(pr['Processor'])

df[['Burst Time']] = burst_time
df['Turn-around Time'] = df['Completion Time']-df['Arrival Time']
df['Waiting Time'] = df['Turn-around Time']-df['Burst Time']
print()

print(df.reset_index())

mean_wt = df['Waiting Time'].mean()
mean_tt = df['Turn-around Time'].mean()

print("Average waiting time = " + str(mean_wt))
print("Average turn around time = "+str(mean_tt))
