from utilities import *

graph = load_graph_from_path('networks/polblogs.gml')

print("Number of vertex: ", get_num_vertex(graph))
print("Number of edges: ", get_num_edges(graph))

'''
   Calculating degree and information about
'''
in_degree = all_in_degree(graph)
out_degree = all_out_degree(graph)
plot_distribution(graph, in_degree, 'in_degree_blog')
plot_distribution(graph, out_degree, 'out_degree_blog')
plot_ccdf(graph, in_degree, 'in_degree_blog')
plot_ccdf(graph, out_degree, 'out_degree_blog')
print("DEGREE: ")
#mean
print("Mean: ")
print("out degree: ", get_mean(in_degree))
print("in degree: ", get_mean(out_degree))
print("\n")

#standard deviation
print("Standard Deviation: ")
print("out degree: ", get_std(in_degree))
print("in degree: ", get_std(out_degree))
print("\n")

#median
print("Median: ")
print("out degree: ", get_median(in_degree))
print("in degree: ", get_median(out_degree))
print("\n")

#maximum value
print("Maximum: ")
print("out degree: ", get_max(in_degree))
print("in degree: ", get_max(out_degree))
print("\n")

#minimum value
print("Minimum: ")
print("out degree: ", get_min(in_degree))
print("in degree: ", get_min(out_degree))

'''
   Calculating distance and information about
'''
distance = all_shortest_distance(graph)
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