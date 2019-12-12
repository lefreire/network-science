from sklearn import datasets 
from graph import *
from utilities import *

data = datasets.load_iris()
x_train = np.concatenate((data['data'][0:20], data['data'][50:70], data['data'][100:120]))
y_train = np.concatenate((data['target'][0:20], data['target'][50:70], data['target'][100:120]))
x_test = np.concatenate((data['data'][21:49], data['data'][71:99], data['data'][121:])) 
y_test = np.concatenate((data['target'][21:49], data['target'][71:99], data['target'][121:])) 

gg = ConstructGraph(x_train, y_train, 3)
utilities = Utilities()

gg.construct_properties()
print(gg.vprop_features)

all_pos_list = []
all_dis_list = []
all_edges = []

for i in range(0, len(gg.vertex_list)):
	dist, pos = utilities.calculate_distances(i, [j for j in range(len(gg.vertex_list)) if j!= i], 
											  gg.vprop_features)
	all_dis_list.append(dist)
	all_pos_list.append(pos)

for i in range(0, len(all_dis_list)):
	utilities.sort_distance(all_dis_list[i], all_pos_list[i])

for i in range(0, len(gg.vertex_list)):
	all_edges = gg.define_kedge(i, all_dis_list[i], all_pos_list[i], with_label=True)


#CALCULO COM COMUNIDADES
cmm = CommunityGraph(gg, 3)
cmm.detect_community()

y_pred = []
for i in x_test:
	gg.insert_one_vertex()
	index_vertex = len(gg.vertex_list)-1
	gg.insert_one_property(index_vertex, i)
	dist, pos = utilities.calculate_distances(index_vertex, [j for j in range(len(gg.vertex_list)) if j!= index_vertex], 
											  gg.vprop_features)
	utilities.sort_distance(dist, pos)
	gg.define_kedge(index_vertex, dist, pos)

	y_pred.append(cmm.calculate_probabilty(index_vertex))


##CALCULO COM COMUNIDADES OBSERVANDO O LABEL DO TREINO (kAOG)




#CALCULO USANDO PASSEIO ALEATORIO COM K VIZINHOS
matrix_adjacency = gg.construct_adjacency(all_pos_list, all_dis_list, 10)
rwg = RandomWalkGraph(gg, matrix_adjacency)

num_train = len(gg.vertex_list)

y_pred = []
for i in x_test:
	gg.insert_one_vertex()
	index_vertex = len(gg.vertex_list)-1
	gg.insert_one_property(index_vertex, i)
	dist, pos = utilities.calculate_distances(index_vertex, [j for j in range(num_train)], 
											  gg.vprop_features)
	utilities.sort_distance(dist, pos)
	new_adj_matrix = rwg.new_adjacency_matrix(dist, pos)
	
	state = rwg.calculate_stationary(new_adj_matrix)

	y_pred.append(rwg.stationary_to_label(state))


