from sklearn import datasets 
from calculate_all import * 
import numpy as np

print('CALCULANDO DO DATASET IRIS')
data_iris = datasets.load_iris()
cc = CalculateClasses(data_iris['data'], data_iris['target'], 3) 

print('COMMUNITY')
res = cc.calculate_community()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print('RANDOM WALK')
res = cc.calculate_walk()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print('LABEL PROPAGATION')  
res = cc.calculate_propagation()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))
print('SVM')  
res = cc.calculate_svm()
print(res)
print("media: ", np.mean(res), "std: ", np.std(res))