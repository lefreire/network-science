from graph_tool.all import *
import numpy as np
from sklearn.metrics import accuracy_score 

class ConstructGraph:

    def __init__(self, data, target, n_classes, is_directed=True):
        self.x = data
        self.y = target
        self.n_classes = n_classes
        self.g = Graph(directed=is_directed)
        self.num_features = len(self.x[0])
        self.vprop_features = self.g.new_vertex_property('vector<double>')
        self.vprop_label = self.g.new_vertex_property('int')
        self.edge_weight = self.g.new_edge_property('double') 
        self.vertex_list = []
        self.edges_dict = {}

    def construct_vertex_list(self):
        # vertex_list = []
        for i in range(0, len(self.x)):
            self.vertex_list.append(self.g.add_vertex()) 

    def insert_one_vertex(self):
        self.vertex_list.append(self.g.add_vertex()) 

    def insert_one_property(self, id_vertex, property_list):
        self.vprop_features[self.vertex_list[id_vertex]] = property_list

    def add_test(self, x_test):
        tam_train = len(self.x)
        for id_vertex in range(0, len(x_test)): 
            self.vertex_list.append(self.g.add_vertex())
            self.vprop_features[self.vertex_list[tam_train+id_vertex]] = x_test[id_vertex]
            self.vprop_label[self.vertex_list[tam_train+id_vertex]] = -1

    def construct_properties(self):
        ''' Definindo os valores das propriedades
        '''
        # vprop = define_properties()
        self.construct_vertex_list()
        for id_vertex in range(0, len(self.x)): 
            self.vprop_features[self.vertex_list[id_vertex]] = self.x[id_vertex]
        for id_label in range(0, len(self.y)):
            self.vprop_label[self.vertex_list[id_label]] = self.y[id_label]

    def define_kedge(self, node_1, distance_list, pos_vertex_list, k=10, with_label=False):
        ''' Define k vizinhos para o vértice node_1, de acordo com as
            menores distâncias - o vetor distance_list e pos_vertex_list já estão ordenados
            de forma crescente; então é só necessário pegar os k primeiros valores
        '''
        self.edges_dict[node_1] = []
        if with_label:
            count_neighbors = 0
            for i in range(0, len(distance_list)):
                if self.vprop_label[node_1] == self.vprop_label[pos_vertex_list[i]]:  
                    self.edges_dict[node_1].append(self.g.add_edge(node_1, pos_vertex_list[i]))
                    self.edge_weight[self.edges_dict[node_1][count_neighbors]] = distance_list[i]
                    count_neighbors += 1
                if count_neighbors == k: break
        else:
            for i in range(0, k):
                self.edges_dict[node_1].append(self.g.add_edge(node_1, pos_vertex_list[i]))
                self.edge_weight[self.edges_dict[node_1][i]] = distance_list[i]
                
        # count_neighbors = 0
        # for i in range(0, len(distance_list)):
        #     if with_label:
        #         if self.vprop_label[node_1] == self.vprop_label[pos_vertex_list[i]]: 
        #             self.edge_weight[self.edges_dict[node_1][i]] = distance_list[i]
        #             count_neighbors += 1
        #         if count_neighbors == k: break
        return self.edges_dict

    def plot_graph(self):
         graph_draw(self.g) 

    def construct_adjacency(self, all_pos_list, all_dist_list, k_neighboors):
        matrix = np.zeros((len(all_pos_list), len(all_pos_list)))
        for pos in range(0, len(all_pos_list)):
            for iid in range(0, k_neighboors):
                matrix[pos][all_pos_list[pos][iid]] = all_dist_list[pos][iid]
        return matrix

class CommunityGraph:

    def __init__(self, graph, n_classes):
        self.graph = graph
        self.n_classes = n_classes
        self.comm_to_lab = {}
        self.state = None

    def set_graph(self, graph):
        self.graph = graph

    def detect_community(self):
        self.state = minimize_blockmodel_dl(self.graph.g, B_min=self.n_classes, B_max=self.n_classes)
        self.community_to_labels()
        print(self.comm_to_lab)

    def community_to_labels(self):
        id_communities = set(self.state.b.a)  
        for i in id_communities:
            self.comm_to_lab[i] = 0 

        for i in range(0, self.n_classes):
            index = [j for j in range(0, len(self.graph.vprop_label.a)) if self.graph.vprop_label.a[j] == i]
            comm = self.state.b.a[index]
            values, counts = np.unique(comm, return_counts=True)
            self.comm_to_lab[values[np.argmax(counts)]] = i

    def calculate_probabilty(self, vertex):
        probs = []
        for i in range(0, self.n_classes):
            probs.append(self.state.get_move_prob(vertex, i))
        return self.comm_to_lab[np.argmax(probs)]

    def calculate_acc(self, y_test, y_pred):
        return accuracy_score(y_test, y_pred)


class RandomWalkGraph:
    
    def __init__(self, graph, adjacency_matrix, k_neighboors=10, rate=1.0):
        self.graph = graph
        self.num_train = len(graph.vertex_list)
        self.adjacency_matrix = adjacency_matrix
        self.k_neighboors = k_neighboors
        self.rate = rate

    def new_adjacency_matrix(self, dist, pos):
        new_matrix_dist = np.zeros(self.num_train)
        for i in range(0, self.k_neighboors): 
            new_matrix_dist[pos[i]] = dist[i] 

        new_matrix = self.adjacency_matrix + self.rate*new_matrix_dist

        row_sums = np.array(new_matrix).sum(axis=1) 
        return new_matrix/row_sums[:, np.newaxis]

    def calculate_stationary(self, new_adj_matrix):
        #We have to transpose so that Markov transitions correspond to right multiplying by a column vector.  np.linalg.eig finds right eigenvectors. 
        evals, evecs = np.linalg.eig(new_adj_matrix.T) 
        evec1 = evecs[:,np.isclose(evals, 1)] 
        #Since np.isclose will return an array, we've indexed with an array 
        #so we still have our 2nd axis.  Get rid of it, since it's only size 1.
        evec1 = evec1[:,0] 

        stationary = evec1 / evec1.sum() 

        #eigs finds complex eigenvalues and eigenvectors, so you'll want the real part.
        stationary = stationary.real      
        return stationary

    def stationary_to_label(self, stationary_array):
        return self.graph.vprop_label[np.argmax(stationary_array)]

    def calculate_acc(self, y_test, y_pred):
        return accuracy_score(y_test, y_pred)


class LabelPropagation:

    def __init__(self, graph):
        self.graph = graph
        self.esource = None
        self.etarget = None
        self.train_size = 0
        self.prob_labels = [0]*graph.n_classes 

    def calculate_train_size(self):
        self.train_size = sum([1 for i in self.graph.vprop_label if i != -1])

    def calculate_prob_label(self):
        for i in range(0, len(self.prob_labels)):
            sum_class = sum([1 for j in self.graph.vprop_label if j == i])
            self.prob_labels[i] = sum_class/self.train_size

    def all_target_source(self):
        self.esource = edge_endpoint_property(self.graph.g, self.graph.g.vertex_index, "source")
        self.etarget = edge_endpoint_property(self.graph.g, self.graph.g.vertex_index, "target")

    def get_source(self, node_target):
        source_vizinho = [] 
        for i in range(0, len(self.etarget.a)): 
            if self.etarget.a[i] == node_target: source_vizinho.append(self.esource.a[i]) 
        return source_vizinho

    def define_label(self):
        classes_prob = [0]*self.graph.n_classes
        for id_susp in range(0, len(self.graph.vprop_label.a)):
            if self.graph.vprop_label[id_susp] == -1:
                source_vizinho = self.get_source(id_susp)
                for i in source_vizinho:
                    prob = utilities.calculate_distance(i, id_susp, self.graph.vprop_features)*self.prob_labels[self.graph.vprop_label[i]] 
                    if prob > classes_prob[gg.vprop_label[i]]: 
                        classes_prob[self.graph.vprop_label[i]] = prob
                self.graph.vprop_label[id_susp] = np.argmax(classes_prob)



