from utilities import *

graph = load_graph_from_path('networks/polblogs.gml')

'''
   Calculating degree and information about
'''
in_degree = all_in_degree(graph)
out_degree = all_out_degree(graph)
#mean
print("Mean: ")
print("out degree: ", get_mean(in_degree))
print("in degree: ", get_mean(out_degree))

#standard deviation
print("Standard Deviation: ")
print("out degree: ", get_std(in_degree))
print("in degree: ", get_std(out_degree))

#median
print("Median: ")
print("out degree: ", get_median(in_degree))
print("in degree: ", get_median(out_degree))

#maximum value
print("Maximum: ")
print("out degree: ", get_max(in_degree))
print("in degree: ", get_max(out_degree))

#minimum value
print("Minimum: ")
print("out degree: ", get_min(in_degree))
print("in degree: ", get_min(out_degree))

'''
   Calculating distance and information about
'''
distance = all_shortest_distance(graph)

#mean
print("Mean: ", get_mean(distance))

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

#mean
print("Mean: ")
print("betweeness: ", get_mean(betweeness))
print("closeness: ", get_mean(closeness))
print("katz: ", get_mean(katz))

#standard deviation
print("Standard Deviation: ")
print("betweeness: ", get_std(betweeness))
print("closeness: ", get_std(closeness))
print("katz: ", get_std(katz))

#median
print("Median: ")
print("betweeness: ", get_median(betweeness))
print("closeness: ", get_median(closeness))
print("katz: ", get_median(katz))

#maximum value
print("Maximum: ")
print("betweeness: ", get_max(betweeness))
print("closeness: ", get_max(closeness))
print("katz: ", get_max(katz))

#minimum value
print("Minimum: ")
print("betweeness: ", get_min(betweeness))
print("closeness: ", get_min(closeness))
print("katz: ", get_min(katz))