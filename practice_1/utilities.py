from graph_tool.all import *
import numpy as np


def load_graph(path):
	return load_graph(path)


def all_in_degree(graph):
	return graph.get_in_degrees(graph.get_vertices())


def all_out_degree(graph):
	return graph.get_out_degrees(graph.get_vertices())


def all_shortest_distance(graph):
	distances = shortest_distance(graph)
	all_dist = []
	for vertex in g.get_vertices():
		for dd in dist[g.vertex(vertex)].a: 
			all_dist.append(dd)
	return all_dist


def all_connected_components(graph):
	comp, hist, is_attractor = label_components(graph, attractors=True, directed=True)
	comp_list = list(comp.a)
	size_components = []
	for component in range(0, max(comp.a)+1):
		size_components.append(comp_list.count(component))
	return size_components


def all_betweeness(graph):
	vertex_b, edges_b = betweenness(graph)
	all_b = []
	for vertex in vertex_b:
		all_b.append(vertex)
	return all_b


def all_closeness(graph):
	vertex_c = closeness(graph)
	all_c = []
	for vertex in vertex_c:
		all_c.append(vertex)
	return all_c


def all_katz(graph):
	vertex_k = katz(graph)
	all_k = []
	for vertex in vertex_k:
		all_k.append(vertex)
	return all_k

def get_mean_degree(all_measure):
	return np.mean(all_measure)


def get_std_degree(all_measure):
	return np.std(all_measure)


def get_median_degree(all_measure):
	return np.median(all_measure)


def get_max_degree(all_measure):
	return np.max(all_measure)


def get_min_degree(all_measure):
	return np.min(allall_measure_degree)


def freq_relative(graph, all_measure):
	degree_distribution = np.bincount(all_measure)
	freq = degree_distribution/len(graph.get_vertices())
	return freq


def ccfd(graph, all_measure):
	freq = freq_relative(graph, all_measure)
	ccdf = [1]
	for i in range(1, len(freq)): 
	    sum_freq = 0 
	    for j in range(0, i-1): 
	        sum_freq += freq[j] 
	    ccdf.append(1-sum_freq)
	return ccdf
