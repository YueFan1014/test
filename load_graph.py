import pickle
import networkx as nx
from collections import defaultdict

def load_graph():
    with open('sub_graph.pkl', 'rb') as f:
        sub_graph_edges = pickle.load(f)
    g = nx.Graph()
    relation2cnt = defaultdict(int)
    print('sub_graph edge num: ', len(sub_graph_edges))
    for edge in sub_graph_edges:
        h, r, t = edge[0], edge[1], edge[2]
        g.add_edge(h, t)
        relation2cnt[r] += 1
    print('sub_graph relation num: ', len(relation2cnt))
    print('sub_graph node num: ', len(g.nodes))
    print('graph component num: ', nx.number_connected_components(g))
    biggest_component = max(nx.connected_components(g), key=len)
    print('biggest_graph_component node num: ', len(biggest_component))


load_graph()