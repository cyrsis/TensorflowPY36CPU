# -*- coding: utf-8 -*-

import sys  
import os 
import time
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')
# 
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

# 夹角余弦距离公式
def cosdist(vector1,vector2):
	Lv1 = sqrt(vector1*vector1.T)
	Lv2 = sqrt(vector2*vector2.T)
	return vector1*vector2.T/(Lv1*Lv2)
    

# kNN分类器
# 测试集：inX
# 训练集：dataSet
# 类别标签：labels
# k:k个邻居数
def classify(testdata, dataSet, labels, k):
	  # 返回样本集的行数
    dataSetSize = dataSet.shape[0]    
    # 计算测试集与训练集之间的距离：标准欧氏距离
    # 1.计算测试项与训练集各项的差
    diffMat = tile(testdata, (dataSetSize,1)) - dataSet
    # 2.计算差的平方和
    sqDiffMat = diffMat**2
    # 3.按列求和
    sqDistances = sqDiffMat.sum(axis=1)
    # 4.生成标准化欧氏距离
    distances = sqDistances**0.5
    print distances
    # 5.根据生成的欧氏距离大小排序,结果为索引号
    sortedDistIndicies = distances.argsort()        
    classCount={}     
    # 获取欧氏距离的前三项作为参考项          
    for i in range(k):  # i = 0~(k-1)  	  
    	  # 按序号顺序返回样本集对应的类别标签
        voteIlabel = labels[sortedDistIndicies[i]]
        # 为字典classCount赋值,相同key，其value加1
        # key:voteIlabel，value: 符合voteIlabel标签的训练集数 
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # 对分类字典classCount按value重新排序
    # sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True) 
    # 该句是按字典值排序的固定用法
    # classCount.iteritems()：字典迭代器函数
    # key：排序参数；operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # 返回序最高的一项
    return sortedClassCount[0][0]

k=3
testdata=[0.2,0.2]
dataSet,labels = createDataSet()

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111)
indx = 0 
for point in dataSet:
	if labels[indx] == 'A' :
		ax.scatter(point[0],point[1],c='blue',marker='o',linewidths=0, s=300)
		plt.annotate("("+str(point[0])+","+str(point[1])+")",xy = (point[0],point[1]))
	else:
		ax.scatter(point[0],point[1],c='red',marker='^',linewidths=0, s=300)
		plt.annotate("("+str(point[0])+", "+str(point[1])+")",xy = (point[0],point[1]))	
	indx += 1

ax.scatter(testdata[0],testdata[1],c='green',marker='s',linewidths=0, s=300)
plt.annotate("("+str(testdata[0])+", "+str(testdata[1])+")",xy = (testdata[0],testdata[1]))		

plt.show()
print classify(testdata, dataSet, labels, k)