# import osmnx as ox

# import networkx as nx
# import numpy as np
# import osmnx as ox
# ox.config(use_cache=True, log_console=True)

# city = 'Troy, NY'
# G = ox.graph_from_place(city, network_type='walk', simplify=True)


# G_nx = nx.relabel.convert_node_labels_to_integers(G)
# nodes, edges = ox.graph_to_gdfs(G_nx, nodes=True, edges=True)

# r_total = np.random.random(len(G_nx))
# nx.set_node_attributes(G_nx, {x:r_total[x] for x in nodes.index}, name='r')
# nc = ox.plot.get_node_colors_by_attr(G_nx, attr='r')  
# fig, ax = ox.plot_graph(G, edge_linewidth=0)
import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)

# get a graph
G = ox.graph_from_place('Troy, NY, USA', network_type='walk')

# get 2 shortest paths
r1 = nx.shortest_path(G, list(G)[0], list(G)[-1], weight='length')
r2 = nx.shortest_path(G, list(G)[10], list(G)[-10], weight='length')

# constrain plot to a bounding box
pt = ox.graph_to_gdfs(G, edges=False).unary_union.centroid
bbox = ox.utils_geo.bbox_from_point((pt.y, pt.x), dist=1000)
fig, ax = ox.plot_graph(G, bbox=bbox)