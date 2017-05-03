import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def plotGraph(red_edges):
    G = nx.DiGraph()
    labels = {'t1','t2','t4','t5','t6','t9','t11','t12','t13','t14','t15', 't18','t19','t20'}
    initPosition = {'t9': [ 0.30929179,  0.97162183], 't6': [ 0.0547307 ,  0.75364438], 't4': [ 0.42352058,  0.4473366 ], 't5': [ 0.34546013,  0.30230591], 't2': [ 1.0,  0.59112415], 't1': [ 0.62595554,  0.02705918], 't14': [ 0.8467943 ,  0.11395259], 't15': [ 0.72025018,  0.95667722], 't11': [ 0.66388604,  0.53207903], 't12': [ 0.57086641,  0.99915934], 't13': [ 0.87557846,  0.84131369], 't20': [ 0.06955834,  0.21560298], 't18': [ 0.0,  0.44155557], 't19': [ 0.36301489,  0.0]}
    Edges = [('t4', 't5'), ('t4', 't6'), ('t5', 't6'), ('t1', 't11'), ('t2', 't11'), ('t9', 't12'), ('t11', 't13'), ('t12', 't13'), ('t4', 't14'),
     ('t5', 't14'), ('t11', 't15'), ('t13', 't15'), ('t1', 't19'), ('t11', 't19'), ('t18', 't20')]
    G.add_edges_from(Edges)

    currentNode = ['t1', 't2', 't4', 't9', 't18']
    pos = nx.spring_layout(G, pos = initPosition, fixed = labels)
    black_edges = [edge for edge in G.edges()]
    black_nodes = [edge[1] for edge in G.edges() if edge[1] not in currentNode]
    nx.draw_networkx_nodes(G,pos, node_color='#C0C0C0')
    nx.draw_networkx_nodes(G,pos, nodelist=currentNode, node_color='#00FF00')
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='r', arrows=True)
    plt.show()

    currentList = []
    for edge in red_edges:
        print "Edge: ", edge
        # print "Current List: ", currentList
        # print "Current Node: ", currentNode
        # print "Black Nodes: ", black_nodes
        currentList.append(edge)
        currentNode.append(edge[1])
        pos = nx.spring_layout(G, pos = initPosition, fixed = labels)
        black_edges = [edge for edge in G.edges() if edge not in currentList]
        black_nodes = [label for label in labels if label not in currentNode]
        nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_nodes(G,pos, nodelist=currentNode, node_color='#7CFC00')
        nx.draw_networkx_nodes(G,pos, nodelist=black_nodes, node_color='#C0C0C0')
        nx.draw_networkx_edges(G, pos, edgelist=currentList, edge_color='b', arrows=True)
        nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='r', arrows=True)
        plt.show()


# plotGraph([('t1', 't2'), ('t1', 't3'), ('t3', 't5'), ('t2', 't4')])
plotGraph([('t4', 't5'), ('t4', 't6'), ('t5', 't6'), ('t1', 't11'), ('t2', 't11'), ('t9', 't12'), ('t11', 't13'), ('t12', 't13'), ('t4', 't14'),
('t5', 't14'), ('t11', 't15'), ('t13', 't15'), ('t1', 't19'), ('t11', 't19'), ('t18', 't20')])
