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


def all_shortest_distance(graph, weights=None):
    distances = shortest_distance(graph, weights=weights)
    all_dist = []
    for vertex in graph.get_vertices():
        for dd in distances[graph.vertex(vertex)].a: 
            if dd == np.finfo(np.double).max or dd == np.iinfo(np.int32).max or dd == 0: 
                pass  
            else: 
                all_dist.append(dd)
    return all_dist


def sample_shortest_distance(graph):
    source_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=1000)
    sample_dist = []
    for source in source_vertex:
        target_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=100)
        for target in target_vertex:
            distance = shortest_distance(graph, source, target=target)
            if distance == np.finfo(np.double).max or distance == np.iinfo(np.int32).max or distance == 0:
                pass
            else: 
                sample_dist.append(distance)
    return sample_dist


def mean_distance(graph, distance):
    return sum(distance)/comb(get_num_vertex(graph), 2) 

def all_connected_components(graph, attractors=False, directed=False):
    comp, his = label_components(graph, attractors=attractors)
    comp_list = list(comp.a)
    size_components = []
    for component in range(0, max(comp.a)+1):
        size_components.append(comp_list.count(component))
    return size_components


def all_betweeness(graph, sample=False, weight=None):
    if sample:
        source_vertex = np.random.randint(low=0,high=len(graph.get_vertices()), size=1000)
        vertex_b, edges_b = betweenness(graph, source_vertex)
    else:
        vertex_b, edges_b = betweenness(graph, weight=weight)
    all_b = []
    for vertex in vertex_b:
        if math.isnan(vertex): all_b.append(0)
        else: all_b.append(vertex)
    return all_b


def all_closeness(graph, weight=None):
    vertex_c = closeness(graph, weight=weight)
    all_c = []
    for vertex in vertex_c:
        if math.isnan(vertex): all_c.append(0)
        else: all_c.append(vertex)
    return all_c


def all_katz(graph, max_iter=None, weight=None):
    vertex_k = katz(graph, max_iter=max_iter, weight=weight)
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


def freq_relative(graph, all_measure, metric='degree'):
    if metric == 'degree':
        degree_distribution = np.bincount(list(all_measure))
        return degree_distribution/len(graph.get_vertices())
    elif metric == 'distance':
        distance_distribution = np.bincount(list(all_measure))
        return distance_distribution/comb(get_num_vertex(graph), 2)
    else:
        all_measure = np.array(all_measure)
        all_sum = float(all_measure.sum())
        return all_measure.cumsum(0)/all_sum  



def ccdf(graph, all_measure, metric='degree'):
    if metric == 'degree':
        freq = freq_relative(graph, all_measure, metric)
        ccdf = [1]
        for i in range(1, len(freq)):   
            sum_freq = 0    
            for j in range(0, i-1):     
                sum_freq += freq[j]     
            ccdf.append(1-sum_freq) 
        return ccdf
    else:
        return sorted(1 - freq_relative(graph, all_measure, metric), reverse=True)


def plot_distribution(graph, all_measure, xlabel, filename, metric='degree'):
    freq = freq_relative(graph, all_measure, metric)
    plt.plot(range(len(freq)), freq, 'o')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('CDF')
    plt.xlabel(xlabel)
    plt.savefig('graphs/'+filename+'_cdf.eps')
    plt.clf()


def plot_ccdf(graph, all_measure, xlabel, filename, metric='degree'):
    _ccdf = ccdf(graph, all_measure, metric)
    plt.plot(range(len(_ccdf)), _ccdf, 'o')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('CCDF')
    plt.xlabel(xlabel)
    plt.savefig('graphs/'+filename+'_ccdf.eps')
    plt.clf()


def plot_weight_distribution(graph):
    weights=graph.properties[('e', 'value')].a
    weights_distribution = np.bincount(list(weights)) 
    freq = weights_distribution/max(weights)
    plt.plot(range(len(freq)), freq, 'o')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('CDF')
    plt.xlabel('Weight')
    plt.savefig('graphs/hep/weight_hep_cdf.eps')
    plt.clf()


