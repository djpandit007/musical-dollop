import webbrowser


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py


def plotGraoph(red_edges,red_edges_lbl):
    G = nx.DiGraph()
    labels = {'t1','t2','t3','t4','t5'}
    Edges = [('t1', 't2'), ('t1', 't3'), ('t4', 't2'), ('t5', 't3'),('t5','t6')]
    G.add_edges_from(Edges)
    
    
#     red_edges = [('A', 'C'), ('E', 'C')]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]
    
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos, node_color='c')
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edge_labels(G, pos,red_edges_lbl)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='b', arrows=False)
    plt.savefig("graph")
    
    
    f = open('graph.html','w')
      
    img_tag_1 = '<img src="{0}">'.format("graph.png")
#     img_tag_2 = '<img src="{0}">'.format("graph.png")
     
    f.write(img_tag_1)
#     f.write(img_tag_2)
    f.close()
     
    filename = 'graph.html'
    webbrowser.open_new(filename)

