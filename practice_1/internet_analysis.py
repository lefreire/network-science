from utilities import *

graph = load_graph_from_path('networks/as-22july06.gml')

print("Number of vertex: ", get_num_vertex(graph))
print("Number of edges: ", get_num_edges(graph))

'''
   Calculating degree and information about
'''
out_degree = all_out_degree(graph)
plot_distribution(graph, out_degree, 'Degree', 'out_degree_internet')
plot_ccdf(graph, out_degree, 'Degree', 'out_degree_internet')
print("DEGREE: ")

#mean
print("Mean: ", get_mean(out_degree))

#standard deviation
print("Standard Deviation: ", get_std(out_degree))

#median
print("Median: ", get_median(out_degree))

#maximum value
print("Maximum: ", get_max(out_degree))

#minimum value
print("Minimum: ", get_min(out_degree))

'''
   Calculating distance and information about
'''
# distance = all_shortest_distance(graph)
distance = sample_shortest_distance(graph)
plot_distribution(graph, distance, 'Distance', 'distance_internet', metric='distance')
plot_ccdf(graph, distance, 'Distance', 'distance_internet', metric='distance')
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
   Calculating vertex centrality and information about
'''
betweeness = all_betweeness(graph, sample=True)
katz = all_katz(graph, max_iter=10000)
plot_distribution(graph, betweeness, 'Betweeness','betweeness_internet', metric='betweeness')
plot_ccdf(graph, betweeness, 'Betweeness', 'betweeness_internet', metric='betweeness')

plot_distribution(graph, katz, 'Katz','katz_internet', metric='katz')
plot_ccdf(graph, katz, 'Katz', 'katz_internet', metric='katz')
print("\n")
print("VERTEX CENTRALITY: ")
#mean
print("Mean: ")
print("betweeness: ", get_mean(betweeness))
print("katz: ", get_mean(katz))
print("\n")

#standard deviation
print("Standard Deviation: ")
print("betweeness: ", get_std(betweeness))
print("katz: ", get_std(katz))
print("\n")

#median
print("Median: ")
print("betweeness: ", get_median(betweeness))
print("katz: ", get_median(katz))
print("\n")

#maximum value
print("Maximum: ")
print("betweeness: ", get_max(betweeness))
print("katz: ", get_max(katz))
print("\n")

#minimum value
print("Minimum: ")
print("betweeness: ", get_min(betweeness))
print("katz: ", get_min(katz))
print("\n")