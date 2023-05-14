import networkx as nx
import random
import time
import matplotlib.pyplot as plt

class RandomGraph:
    def __init__(self, nodes, sparse=False):
        self.nodes = nodes
        self.sparse = sparse
        self.graph = self.generate_graph()

    def generate_graph(self):
        if self.sparse:
            edge_prob = 0.1  # smaller probability for sparse graph
        else:
            edge_prob = 0.8  # larger probability for dense graph

        graph = nx.fast_gnp_random_graph(self.nodes, edge_prob)

        for (u, v, w) in graph.edges(data=True):
            w['weight'] = random.randint(1, 100)

        return graph


class MST:
    def __init__(self, graph):
        self.graph = graph

    def run_prim(self):
        start_time = time.time()
        mst = nx.minimum_spanning_tree(self.graph, algorithm='prim')
        end_time = time.time()
        return mst, end_time - start_time

    def run_kruskal(self):
        start_time = time.time()
        mst = nx.minimum_spanning_tree(self.graph, algorithm='kruskal')
        end_time = time.time()
        return mst, end_time - start_time


class GraphDrawer:
    def __init__(self, graph, mst, algorithm):
        self.graph = graph
        self.mst = mst
        self.algorithm = algorithm

    def draw(self):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, with_labels=False, node_size=100)
        nx.draw_networkx_edges(self.graph, pos, edgelist=self.mst.edges(), width=2, edge_color='r')
        plt.title(f'MST using {self.algorithm}')
        plt.show()


def compare_algorithms(nodes, sparse):
    prim_times = []
    kruskal_times = []

    for n in nodes:
        graph_obj = RandomGraph(n, sparse)
        mst_obj = MST(graph_obj.graph)

        _, prim_time = mst_obj.run_prim()
        prim_times.append(prim_time)

        _, kruskal_time = mst_obj.run_kruskal()
        kruskal_times.append(kruskal_time)

    # plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, prim_times, label="Prim's Algorithm")
    plt.plot(nodes, kruskal_times, label="Kruskal's Algorithm")
    plt.xlabel('Number of nodes')
    plt.ylabel('Execution time (seconds)')
    plt.title('Performance of Prim\'s and Kruskal\'s Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

nodes = [100, 500, 1000, 2000]
compare_algorithms(nodes, False)  # for a dense graph
compare_algorithms(nodes, True)  # for a sparse graph

nodes = 10
sparse = False

graph_obj = RandomGraph(nodes, sparse)
mst_obj = MST(graph_obj.graph)

mst_prim, _ = mst_obj.run_prim()
drawer = GraphDrawer(graph_obj.graph, mst_prim, "Prim's Algorithm")
drawer.draw()

mst_kruskal, _ = mst_obj.run_kruskal()
drawer = GraphDrawer(graph_obj.graph, mst_kruskal, "Kruskal's Algorithm")
drawer.draw()

sparse = True

graph_obj = RandomGraph(nodes, sparse)
mst_obj = MST(graph_obj.graph)

mst_prim, _ = mst_obj.run_prim()
drawer = GraphDrawer(graph_obj.graph, mst_prim, "Prim's Algorithm Spare")
drawer.draw()

mst_kruskal, _ = mst_obj.run_kruskal()
drawer = GraphDrawer(graph_obj.graph, mst_kruskal, "Kruskal's Algorithm Spare")
drawer.draw()