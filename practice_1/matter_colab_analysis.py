print("\n")
from utilities import *

graph = load_graph_from_path('networks/cond-mat-2003.gml')

print("Number of vertex: ", get_num_vertex(graph))
print("Number of edges: ", get_num_edges(graph))

'''
   Calculating degree and information about
'''
out_degree = all_out_degree(graph)
plot_distribution(graph, out_degree,'Out Degree', 'out_degree_matter')
plot_ccdf(graph, out_degree, 'Out Degree','out_degree_matter')
print("DEGREE: ")
#mean
print("Mean: ")
print("out degree: ", get_mean(out_degree))
print("\n")

#standard deviation
print("Standard Deviation: ")
print("out degree: ", get_std(out_degree))
print("\n")

#median
print("Median: ")
print("out degree: ", get_median(out_degree))
print("\n")

#maximum value
print("Maximum: ")
print("out degree: ", get_max(out_degree))
print("\n")

#minimum value
print("Minimum: ")
print("out degree: ", get_min(out_degree))

'''
   Calculating distance and information about
'''
distance = all_shortest_distance(graph)
plot_distribution(graph, distance, 'Distance', 'distance_matter', metric='distance')
plot_ccdf(graph, distance, 'Distance', 'distance_matter', metric='distance')
print("\n")
print("DISTANCE: ")
#mean
print("Mean: ",  mean_distance(graph, distance))

#standard deviation
print("Standard Deviation: ", get_std(distance))

#median
print("Median: ", get_median(distance))

#maximum value
print("Maximum: ", get_max(distance))

#minimum value
print("Minimum: ", get_min(distance))

'''
   Calculating size of connected components and information about
'''
connected = all_connected_components(graph)
plot_distribution(graph, connected, 'Connected Components', 'cc_matter', metric='cc')
plot_ccdf(graph, connected,'Connected Components', 'cc_matter', metric='cc')
print("\n")
print("CONNECTED COMPONENTS: ")
#mean
print("Mean: ", get_mean(connected))

#standard deviation
print("Standard Deviation: ", get_std(connected))

#median
print("Median: ", get_median(connected))

#maximum value
print("Maximum: ", get_max(connected))

#minimum value
print("Minimum: ", get_min(connected))

'''
   Calculating vertex centrality and information about
'''
betweeness = all_betweeness(graph)
closeness = all_closeness(graph)
katz = all_katz(graph)
plot_distribution(graph, betweeness, 'Betweeness','betweeness_matter', metric='betweeness')
plot_ccdf(graph, betweeness, 'Betweeness', 'betweeness_matter', metric='betweeness')

plot_distribution(graph, closeness, 'Closeness', 'closeness_matter', metric='closeness')
plot_ccdf(graph, closeness, 'Closeness', 'closeness_matter', metric='closeness')

plot_distribution(graph, katz, 'Katz','katz_matter', metric='katz')
plot_ccdf(graph, katz, 'Katz', 'katz_matter', metric='katz')
print("\n")
print("VERTEX CENTRALITY: ")
#mean
print("Mean: ")
print("betweeness: ", get_mean(betweeness))
print("closeness: ", get_mean(closeness))
print("katz: ", get_mean(katz))
print("\n")

#standard deviation
print("Standard Deviation: ")
print("betweeness: ", get_std(betweeness))
print("closeness: ", get_std(closeness))
print("katz: ", get_std(katz))
print("\n")

#median
print("Median: ")
print("betweeness: ", get_median(betweeness))
print("closeness: ", get_median(closeness))
print("katz: ", get_median(katz))
print("\n")

#maximum value
print("Maximum: ")
print("betweeness: ", get_max(betweeness))
print("closeness: ", get_max(closeness))
print("katz: ", get_max(katz))
print("\n")

#minimum value
print("Minimum: ")
print("betweeness: ", get_min(betweeness))
print("closeness: ", get_min(closeness))
print("katz: ", get_min(katz))
print("\n")