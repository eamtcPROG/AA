import random
import time
import matplotlib.pyplot as plt
from collections import deque

# Function to perform DFS
def DFS(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        # print(node, end=" ")

        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                stack.append(neighbour)

# Function to perform BFS
def BFS(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        # print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Function to generate a random graph
def generate_graph(num_nodes, num_edges):
    graph = {i: [] for i in range(num_nodes)}
    for _ in range(num_edges):
        u = random.randint(0, num_nodes-1)
        v = random.randint(0, num_nodes-1)
        if u != v and v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
    return graph

# Plot speed vs number of nodes for DFS
def plot_dfs_speed_vs_nodes(num_nodes_list, num_edges):
    dfs_times = []
    for num_nodes in num_nodes_list:
        graph = generate_graph(num_nodes, num_edges)

        # Test DFS
        start_time = time.time()
        DFS(graph, 0)
        end_time = time.time()
        dfs_times.append(end_time - start_time)

    plt.plot(num_nodes_list, dfs_times, label="DFS")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (s)")
    plt.title("Depth-First Search")
    plt.legend()
    plt.show()

# Plot speed vs number of nodes for BFS
def plot_bfs_speed_vs_nodes(num_nodes_list, num_edges):
    bfs_times = []
    for num_nodes in num_nodes_list:
        graph = generate_graph(num_nodes, num_edges)

        # Test BFS
        start_time = time.time()
        BFS(graph, 0)
        end_time = time.time()
        bfs_times.append(end_time - start_time)

    plt.plot(num_nodes_list, bfs_times, label="BFS")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (s)")
    plt.title("Breadth-First Search")
    plt.legend()
    plt.show()

# Plot speed vs number of nodes for DFS and BFS for graphs with 100 to 1000 nodes
num_nodes_list = list(range(100, 1000, 100))
num_edges = 5000

plot_dfs_speed_vs_nodes(num_nodes_list, num_edges)
plot_bfs_speed_vs_nodes(num_nodes_list, num_edges)

# Plot comparison of DFS and BFS
dfs_times = []
bfs_times = []
for num_nodes in num_nodes_list:
    graph = generate_graph(num_nodes, num_edges)

    # Test DFS
    start_time = time.time()
    DFS(graph, 0)
    end_time = time.time()
    dfs_times.append(end_time - start_time)

    # Test BFS
    start_time = time.time()
    BFS(graph, 0)
    end_time = time.time()
    bfs_times.append(end_time - start_time)

plt.plot(num_nodes_list, dfs_times, label="DFS")
plt.plot(num_nodes_list, bfs_times, label="BFS")
plt.xlabel("Number of Nodes")
plt.ylabel("Time (s)")
plt.title("DFS vs BFS")
plt.legend()
plt.show()