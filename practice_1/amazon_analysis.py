from graph_tool.all import *
import numpy as np


# Creating the Graph object
graph = Graph() 
graph.set_directed(False) 


# Reading file
file_amazon = open('networks/com-amazon.ungraph.txt')
all_lines = file_amazon.readlines()

# in the position 2, we have the node and edges
info = [int(i) for i in all_lines[2].split() if i.isdigit()]
nodes, edges = info[0], info[1]

# vertex = []
# for i in range(0, nodes):
# 	vertex.append(graph.add_vertex()) 

# since the position 4, we have the edges
# the nodes start from 1
for edge in range(4, len(all_lines)):
	relation = [int(i) for i in all_lines[edge].split() if i.isdigit()]
	v1, v2 = relation[0]-1, relation[1]-1
	graph.add_edge(v1, v2) 