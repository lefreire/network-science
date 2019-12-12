import numpy as np

class Utilities:

	def __init__(self):
		pass

	def calculate_distance(self, node1, node2, properties_list):
		# print(properties_list[node1])
		sum_diff = 0
		for i in range(0, len(properties_list[node1])):
			sum_diff += np.abs(properties_list[node1][i] - properties_list[node2][i])
		return sum_diff/len(properties_list[node1])

	def calculate_distances(self, node1, all_nodes, properties_list):
		distances = []
		pos_nodes = []
		for i in all_nodes:
			distances.append(self.calculate_distance(node1, i, properties_list))
			pos_nodes.append(i)
		return distances, pos_nodes

	def sort_distance(self, distance_list, pos_list):
		''' Método para ordenar as distâncias de um no para os outros
			e ordenar estes vértices de acordo com a ordenação das distâncias
			ordenação: maior - menor
		'''
		for dist_id in range(0, len(distance_list)):
			best_dist = dist_id
			for next_id in range(dist_id+1, len(distance_list)):
				if distance_list[next_id] < distance_list[best_dist]:
					distance_list[best_dist], distance_list[next_id] = distance_list[next_id], distance_list[best_dist]  
					pos_list[best_dist], pos_list[next_id] = pos_list[next_id], pos_list[best_dist]
	    
