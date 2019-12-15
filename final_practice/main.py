from sklearn import datasets 
from calculate_all import * 
import numpy as np

k = 40
print(k)
print('CALCULANDO DO DATASET IRIS')
data_iris = datasets.load_iris()
cc = CalculateClasses(data_iris['data'], data_iris['target'], 3) 

print('COMMUNITY')
res = cc.calculate_community(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_cmm(res))
print('RANDOM WALK')
res = cc.calculate_walk(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_walk(res))
print('LABEL PROPAGATION')  
res = cc.calculate_propagation(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_lp(res))
print('SVM')  
res = cc.calculate_svm()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_svm(res))


print('CALCULANDO DO DATASET CANCER')
data_cancer = datasets.load_breast_cancer() 
cc = CalculateClasses(data_cancer['data'], data_cancer['target'], 2) 

print('COMMUNITY')
res = cc.calculate_community(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_cmm(res))
print('RANDOM WALK')
res = cc.calculate_walk(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_walk(res))
print('LABEL PROPAGATION')  
res = cc.calculate_propagation(k)
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_lp(res))
print('SVM')  
res = cc.calculate_svm()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print("teste: ", cc.calculate_test_svm(res))


# print('CALCULANDO DO DATASET DIGITOS')
# data_digits = datasets.load_digits() 
# cc = CalculateClasses(data_digits['data'], data_digits['target'], 10) 

# print('COMMUNITY')
# res = cc.calculate_community(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_cmm(res))
# print('RANDOM WALK')
# res = cc.calculate_walk(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_walk(res))
# print('LABEL PROPAGATION')  
# res = cc.calculate_propagation(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_lp(res))
# print('SVM')  
# res = cc.calculate_svm()
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_svm(res))


# print('CALCULANDO DOS SENSORES')
# data = open('../../data.txt')   
# sensors = data.readlines()   

# sensors_features = []
# sensors_target = []
# for sensor in sensors:
# 	new_sensor = sensor.split(' ')[3:]
# 	new_sensor[-1] = new_sensor[-1].split('\n')[0]
# 	if new_sensor[0] == '': pass
# 	else:
# 		sensors_target.append(int(new_sensor[0]))
# 		for i in range(1, len(new_sensor)):
# 			if new_sensor[i] == '': new_sensor[i] = 0.0
# 			new_sensor[i] = float(new_sensor[i])
# 		sensors_features.append(new_sensor[1:])
# cc = CalculateClasses(sensors_features, sensors_target, 54) 

# print('COMMUNITY')
# res = cc.calculate_community(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_cmm(res))
# print('RANDOM WALK')
# res = cc.calculate_walk(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_walk(res))
# print('LABEL PROPAGATION')  
# res = cc.calculate_propagation(k)
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_lp(res))
# print('SVM')  
# res = cc.calculate_svm()
# print(res)
# print("media: ", np.mean(res), "std: ", np.std(res))
# print("teste: ", cc.calculate_test_svm(res))
