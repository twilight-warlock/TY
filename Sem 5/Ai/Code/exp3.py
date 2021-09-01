nodes=['S','A','B','C','D','Y','X','E']
a = [0,5,6,4,15,8,5,0]
c = [17,999,999,999,999,999,999,999]

xyz = {
  'S': ['A','B'],
  'A': ['Y','X'],
  'B': ['C','D'],
  'Y': ['E'],
  'X': ['E'],
  'C': ['E'],
  'D': ['E'],
  'E': []
}

dist = []
for i in range(len(nodes)):
    dist.append([0]*len(nodes))

for i in range(len(nodes)):
    for x in xyz[nodes[i]]:
        d = int(input("Enter distance of {} from {} : ".format(x,nodes[i])))
        y = nodes.index(x)
        dist[i][y] = d
        dist[y][i] = d

src = input("Enter the Source Node : ")
lastNode = input("Enter the last node: ")

visited = {}
distance = {}
main = {}
bfs_output = []
queue1 = {}
queue = []
for i in xyz.keys():
    visited[i] = False
    main[i] = None
    distance[i] = 99999
    queue1[i] = 99999

source = src
visited[source] = True
distance[source]= 0
queue1[source] = 17
queue.append(source)
v = 1
while len(queue)!=0:
    pop = queue.pop(0)
    queue1.pop(pop)
    bfs_output.append(pop)

    for i in xyz[pop]:
        tot = distance[pop] + dist[nodes.index(pop)][nodes.index(i)] + a[nodes.index(i)]
        if c[nodes.index(i)] > tot:
            visited[i] = True
            v+=1
            main[i] = pop
            distance[i] = distance[pop] + dist[nodes.index(pop)][nodes.index(i)]
            c[nodes.index(i)] = distance[i] + a[nodes.index(i)]
            queue1[i] = distance[i] + a[nodes.index(i)]
        queue.append(i)
        queue.append(i)
        sortedQueue = sorted(queue1.items(), key=lambda x: x[1])
        queue = []
        for j in sortedQueue:
            queue.append(j[0])

print(a)

path = []
print("Total Cost: ",distance)
print("Number of nodes visited: ",v)
while lastNode is not None:
    path.append(lastNode)
    lastNode = main[lastNode]
path.reverse()
print("Path taken",path)

