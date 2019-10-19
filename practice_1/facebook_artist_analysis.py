# from graph_tool.all import *
# import numpy as np
from utilities import *


# Creating the Graph object
graph = Graph() 
graph.set_directed(False) 


# Reading file
file_facebook_artist = open('networks/artist_edges.txt')
all_lines = file_facebook_artist.readlines()

# since the position 2, we have the edges
# the nodes start from 1
for edge in range(4, len(all_lines)):
	relation = [int(i) for i in all_lines[edge].replace(',', ' ').split() if i.isdigit()]
	v1, v2 = relation[0], relation[1]
	graph.add_edge(v1, v2) 

'''
   Calculating degree and information about
'''
out_degree = all_out_degree(graph)
plot_distribution(graph, out_degree, 'Degree', 'out_degree_facebook')
plot_ccdf(graph, out_degree, 'Degree', 'out_degree_facebook')
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
distance = sample_shortest_distance(graph)
plot_distribution(graph, distance, 'Distance', 'distance_facebook', metric='distance')
plot_ccdf(graph, distance, 'Distance', 'distance_facebook', metric='distance')
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
plot_distribution(graph, betweeness, 'Betweeness','betweeness_facebook', metric='betweeness')
plot_ccdf(graph, betweeness, 'Betweeness', 'betweeness_facebook', metric='betweeness')

plot_distribution(graph, katz, 'Katz','katz_facebook', metric='katz')
plot_ccdf(graph, katz, 'Katz', 'katz_facebook', metric='katz')
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