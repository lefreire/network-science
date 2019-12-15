from sklearn import datasets 
from graph import *
from utilities import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.svm import SVC

class CalculateClasses:

	def __init__(self, data, target, num_classes, test_size=0.3):
		self.data = data
		self.target = target
		self.test_size = test_size
		self.n_classes = num_classes
		self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.data, self.target, test_size=self.test_size, random_state=42)
		kf = StratifiedKFold(n_splits=10, random_state=512, shuffle=True)
		self.splits = [(train_index, val_index) for train_index, val_index in kf.split(self.X_train, self.Y_train)]
		self.utilities = Utilities()

	def __calculate_graph(self, x_train, y_train):
		gg = ConstructGraph(x_train, y_train, self.n_classes)
		gg.construct_properties()
		return gg

	def __calculate_distances(self, gg, with_label=False, k=10):
		all_pos_list = []
		all_dis_list = []
		all_edges = []

		for i in range(0, len(gg.vertex_list)):
			dist, pos = self.utilities.calculate_distances(i, [j for j in range(len(gg.vertex_list)) if j!= i], 
													  gg.vprop_features)
			all_dis_list.append(dist)
			all_pos_list.append(pos)

		for i in range(0, len(all_dis_list)):
			self.utilities.sort_distance(all_dis_list[i], all_pos_list[i])

		for i in range(0, len(gg.vertex_list)):
			all_edges = gg.define_kedge(i, all_dis_list[i], all_pos_list[i], k=k, with_label=with_label)

		return all_pos_list, all_dis_list, all_edges

	def calculate_community(self, k=10):
		res_cmm = []
		for i in self.splits:
			res_cmm.append(self.calculate_cmm(self.X_train[i[0]], self.Y_train[i[0]], self.X_train[i[1]], self.Y_train[i[1]], k))
			print("ESTOU AQUI")
		return res_cmm

	def calculate_walk(self, k=10):
		res_rw = []
		for i in self.splits:
			res_rw.append(self.calculate_rw(self.X_train[i[0]], self.Y_train[i[0]], self.X_train[i[1]], self.Y_train[i[1]], k))
		return res_rw

	def calculate_propagation(self, k=10):
		res_lp = []
		for i in self.splits:
			res_lp.append(self.calculate_lp(self.X_train[i[0]], self.Y_train[i[0]], self.X_train[i[1]], self.Y_train[i[1]], k))
		return res_lp

	def calculate_svm(self):
		res_svm = []
		for i in self.splits:
			res_svm.append(self.calculate_ssvm(self.X_train[i[0]], self.Y_train[i[0]], self.X_train[i[1]], self.Y_train[i[1]]))
		return res_svm

	def calculate_test_cmm(self, res_cmm, k=10):
		best_split = np.argmax(res_cmm)
		x_train = self.X_train[self.splits[best_split][0]]
		y_train = self.Y_train[self.splits[best_split][0]]
		return self.calculate_cmm(x_train, y_train, self.X_test, self.Y_test, k)

	def calculate_test_walk(self, res_walk, k=10):
		best_split = np.argmax(res_walk)
		x_train = self.X_train[self.splits[best_split][0]]
		y_train = self.Y_train[self.splits[best_split][0]]
		return self.calculate_rw(x_train, y_train, self.X_test, self.Y_test, k)

	def calculate_test_lp(self, res_lp, k=10):
		best_split = np.argmax(res_lp)
		x_train = self.X_train[self.splits[best_split][0]]
		y_train = self.Y_train[self.splits[best_split][0]]
		return self.calculate_lp(x_train, y_train, self.X_test, self.Y_test, k)

	def calculate_test_svm(self, res_cvm):
		best_split = np.argmax(res_cvm)
		x_train = self.X_train[self.splits[best_split][0]]
		y_train = self.Y_train[self.splits[best_split][0]]
		return self.calculate_ssvm(x_train, y_train, self.X_test, self.Y_test)

	def calculate_cmm(self, x_train, y_train, x_val, y_val, k=10):
		gg = self.__calculate_graph(x_train, y_train)
		_, _, _ = self.__calculate_distances(gg, True, k)

		#CALCULO COM COMUNIDADES
		cmm = CommunityGraph(gg, gg.n_classes)
		cmm.detect_community()
		y_pred = []
		for i in x_val:
			gg.insert_one_vertex()
			index_vertex = len(gg.vertex_list)-1
			gg.insert_one_property(index_vertex, i)
			dist, pos = self.utilities.calculate_distances(index_vertex, [j for j in range(len(gg.vertex_list)) if j!= index_vertex], 
													  gg.vprop_features)
			self.utilities.sort_distance(dist, pos)
			gg.define_kedge(index_vertex, dist, pos)

			y_pred.append(cmm.calculate_probabilty(index_vertex))
		return cmm.calculate_acc(y_val, y_pred)

	def calculate_rw(self, x_train, y_train, x_val, y_val, k=10):
		gg = self.__calculate_graph(x_train, y_train)
		all_pos_list, all_dis_list, _ = self.__calculate_distances(gg, False, k)

		matrix_adjacency = gg.construct_adjacency(all_pos_list, all_dis_list, k)
		rwg = RandomWalkGraph(gg, matrix_adjacency)

		num_train = len(gg.vertex_list)
		y_pred = []
		for i in x_val:
			gg.insert_one_vertex()
			index_vertex = len(gg.vertex_list)-1
			gg.insert_one_property(index_vertex, i)
			dist, pos = self.utilities.calculate_distances(index_vertex, [j for j in range(num_train)], 
													  gg.vprop_features)
			self.utilities.sort_distance(dist, pos)
			new_adj_matrix = rwg.new_adjacency_matrix(dist, pos)
			

			state = rwg.calculate_stationary(new_adj_matrix)

			y_pred.append(rwg.stationary_to_label(state))
		return rwg.calculate_acc(y_val, y_pred)

	def calculate_lp(self, x_train, y_train, x_val, y_val, k=10):
		gg = self.__calculate_graph(x_train, y_train)
		gg.add_test(x_val)
		_, _, _ = self.__calculate_distances(gg, False, k)
		
		#CALCULO USANDO LABEL PROPAGATION
		lp = LabelPropagation(gg)
		lp.calculate_train_size()
		lp.calculate_prob_label()
		lp.all_target_source()
		lp.define_label()
		y_pred = lp.return_label()
		return lp.calculate_acc(y_val, y_pred)

	def calculate_ssvm(self, x_train, y_train, x_val, y_val):
		clf = SVC(gamma='auto')
		clf.fit(x_train, y_train)
		return clf.score(x_val, y_val)



