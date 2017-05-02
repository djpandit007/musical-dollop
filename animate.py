import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def plotGraph(red_edges):
    G = nx.DiGraph()
    labels = {'t1','t2','t3','t4','t5'}
    initPosition = {'t6': [0.32223838, 0.43601068],
                    't4': [0.5, 0.21554374],
                    't5': [0.13372532, 0.43445189],
                    't2': [0.35372889, 0.0],
                    't3': [0.0, 0.22875369],
                    't1': [0.09115616, 0.00502474]}
    Edges = [('t1', 't2'), ('t1', 't3'), ('t2', 't4'), ('t3', 't5')]
    G.add_edges_from(Edges)
    
    currentList = []
    for edge in red_edges:
        currentList.append(edge)
        pos = nx.spring_layout(G, pos = initPosition, fixed = labels)
        black_edges = [edge for edge in G.edges() if edge not in currentList]
        nx.draw_networkx_nodes(G,pos, node_color='c')
        nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_edges(G, pos, edgelist=currentList, edge_color='b', arrows=True)
        nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='r', arrows=True)
        plt.show()
       
    
plotGraph([('t1', 't2'), ('t1', 't3'), ('t3', 't5'), ('t2', 't4')])

