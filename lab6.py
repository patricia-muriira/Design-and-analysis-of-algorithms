def bfs(start_vertex):
    global front, rear
    queue = [0] * 20
    visited = [0] * 20
    queue[rear] = start_vertex
    visited[start_vertex] = 1

    while front <= rear:
        current_vertex = queue[front]
        print(current_vertex, end=" ")

        for i in range(1, n + 1):
            if a[current_vertex][i] and not visited[i]:
                visited[i] = 1
                rear += 1
                queue[rear] = i

        front += 1


def dfs(current_vertex):
    global count
    reach[current_vertex] = 1
    for i in range(1, n + 1):
        if a[current_vertex][i] and not reach[i]:
            print(current_vertex, "->", i)
            dfs(i)


# Main program
n = int(input("Enter the number of vertices: "))
a = [[0] * (n + 1) for _ in range(n + 1)]
front, rear = -1, 0

# Read the adjacency matrix
print("Enter the adjacency matrix:")
for i in range(1, n + 1):
    a[i][1:n + 1] = map(int, input().split())

# BFS
start_vertex_bfs = int(input("Enter the starting vertex for BFS: "))
print("BFS traversal starting from vertex", start_vertex_bfs, "is:")
bfs(start_vertex_bfs)

# DFS
reach = [0] * 20
count = 0
print("\nDFS traversal is:")
dfs(1)

# Check if the graph is connected
if count == n:
    print("\nGraph is connected")
else:
    print("\nGraph is not connected")
