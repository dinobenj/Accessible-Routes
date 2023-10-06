import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
def testPlotRoute(RPI):
      orig = ox.nearest_nodes(RPI, 42.7324294, -73.6905807)
      dest = ox.nearest_nodes(RPI, 42.7338301, -73.6847063)
      #1208042175, "lat": 42.7268945, "lon": -73.6737245
      route = nx.shortest_path(RPI, orig, dest, 'travel_time')
      print(route)
      #route_map = ox.plot_route_folium(RPI, route)
      #route_map.save('test.html')
      return route
def plotGraph(place):
      ox.config(use_cache=True, log_console=False)
      RPI = ox.graph_from_address(place, dist=500, network_type="walk")
      RPI = ox.speed.add_edge_speeds(RPI)
      RPI = ox.speed.add_edge_travel_times(RPI)
      #point1 = "lat": 42.7334294, "lon": -73.6905807
      #point2 = "lat": 42.7338301, "lon": -73.6887063
      north = 42.73201
      south = 42.72492
      east = -73.67119
      west = -73.68663
      print(RPI.edges)
      fig, ax = ox.plot_graph(RPI, bbox=(north, south, east, west), edge_color = 'r', node_color='b')
      testPlotRoute(RPI)
      return fig, ax


place = 'Rensselaer Polytechnic Institute'
plotGraph(place)

#ox.save_load.save_graph_osm(RPI, filename='RPI.osm')