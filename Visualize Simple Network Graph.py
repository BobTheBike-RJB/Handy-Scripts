## Visualize simple network graph

start_folder = input('Directory/Starting Folder: ')

import os
os.chdir(start_folder)

# Load data to a pandas dataframe
import pandas
data_file = 'Sample Network.csv'
df = pandas.read_csv(data_file)

# Load dataframe to a Networkx graph
import networkx
graph = networkx.from_pandas_edgelist(df,source='Parent',target='Child',edge_attr='Country')

# Set attribute for measuring betweenness centrality
bb = networkx.edge_betweenness_centrality(graph, normalized=False)
networkx.set_edge_attributes(graph, bb, "betweenness")

print("Average Node Connectivity in this graph: " + str(networkx.average_node_connectivity(graph)))

print(networkx.degree_centrality(graph))

# print(graph.edges['Account 4','Account 2']["betweenness"])
# for e in graph.edges():
#     print("Edge: " + str(e))
#     print("Betweenness: " + str(graph.edges[e]["betweenness"]))

# Setup visualization for showing edge weight set by a metric (like betweenness centrality)
widths = networkx.get_edge_attributes(graph, 'betweenness')
nodelist = graph.nodes()

for key in widths.keys():
    widths[key] = widths[key] * 3

print(widths)

import matplotlib.pyplot as plt

# plt.figure(figsize=(12,8))

pos = networkx.shell_layout(graph)
networkx.draw_networkx_nodes(graph,pos,
                       nodelist=nodelist,
                       node_size=500,
                       node_color='blue',
                       alpha=0.7)
networkx.draw_networkx_edges(graph,pos,
                       edgelist = widths.keys(),
                       width=list(widths.values()),
                       edge_color='lightblue',
                       alpha=0.6)

networkx.draw_networkx_labels(graph, pos=pos,
                        labels=dict(zip(nodelist,nodelist)),
                        font_color='black')

plt.box(False)
plt.show()

# # Visualize network graph
# import matplotlib.pyplot as plt
# G = networkx.draw_networkx(graph)
# # print(networkx.degree(graph))

# plt.show()

# # Calculate Eigenvalues
# import numpy.linalg

# L = networkx.normalized_laplacian_matrix(graph)
# e = numpy.linalg.eigvals(L.A)

# print(e)
