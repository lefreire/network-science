from graph_tool.all import *
import math
import matplotlib
matplotlib.use("macOSX") 
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb


def load_graph_from_path(path):
    return load_graph(path)


def get_num_vertex(graph):
    return len(graph.get_vertices())


def get_num_edges(graph):
    return len(graph.get_edges())


def all_in_degree(graph):
    return graph.get_in_degrees(graph.get_vertices())


def all_out_degree(graph):
    return graph.get_out_degrees(graph.get_vertices())


def all_shortest_distance(graph):
    distances = shortest_distance(graph)
    all_dist = []
    for vertex in graph.get_vertices():
        for dd in distances[graph.vertex(vertex)].a: 
            all_dist.append(dd)
    return all_dist


def sample_shortest_distance(graph):
    source_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=1000)
    sample_dist = []
    for source in source_vertex:
        target_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=100)
        for target in target_vertex:
            sample_dist.append(shortest_distance(graph, source, target=target))
    return sample_dist


def mean_distance(graph, distance):
    return sum(distance)/comb(get_num_vertex(graph), 2) 

def all_connected_components(graph):
    comp, hist, is_attractor = label_components(graph, attractors=True, directed=True)
    comp_list = list(comp.a)
    size_components = []
    for component in range(0, max(comp.a)+1):
        size_components.append(comp_list.count(component))
    return size_components


def all_betweeness(graph, sample=False):
    if sample:
        source_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=1000)
        vertex_b, edges_b = betweenness(graph, source_vertex)
    else:
        vertex_b, edges_b = betweenness(graph)
    all_b = []
    for vertex in vertex_b:
        if math.isnan(vertex): all_b.append(0)
        else: all_b.append(vertex)
    return all_b


def all_closeness(graph):
    vertex_c = closeness(graph)
    all_c = []
    for vertex in vertex_c:
        if math.isnan(vertex): all_c.append(0)
        else: all_c.append(vertex)
    return all_c


def all_katz(graph, max_iter=None):
    vertex_k = katz(graph, max_iter=max_iter)
    all_k = []
    for vertex in vertex_k:
        if math.isnan(vertex): all_k.append(0)
        else: all_k.append(vertex)
    return all_k

def get_mean(all_measure):
    return np.mean(all_measure)


def get_std(all_measure):
    return np.std(all_measure)


def get_median(all_measure):
    return np.median(all_measure)


def get_max(all_measure):
    return np.max(all_measure)


def get_min(all_measure):
    return np.min(all_measure)


def freq_relative(graph, all_measure):
    degree_distribution = np.bincount(list(all_measure))
    freq = degree_distribution/len(graph.get_vertices())
    return freq


def ccdf(graph, all_measure):
    freq = freq_relative(graph, all_measure)
    ccdf = [1]
    for i in range(1, len(freq)): 
        sum_freq = 0 
        for j in range(0, i-1): 
            sum_freq += freq[j] 
        ccdf.append(1-sum_freq)
    return ccdf


def plot_distribution(graph, all_measure, filename):
    freq = freq_relative(graph, all_measure)
    plt.plot(range(len(freq)), freq, 'o')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('Frequence')
    plt.xlabel('Degree')
    plt.savefig(filename+'_freq.eps')
    plt.clf()


def plot_ccdf(graph, all_measure, filename):
    _ccdf = ccdf(graph, all_measure)
    plt.plot(range(len(_ccdf)), _ccdf, 'o')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylim([0,1])
    plt.ylabel('CCDF')
    plt.xlabel('Degree')
    plt.savefig(filename+'_ccdf.eps')
    plt.clf()
