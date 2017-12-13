# -*- coding: utf-8 -*-

import sys  
import os 
import time
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import operator
from Nbayes_lib import *

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 夹角余弦距离公式
def cosdist(vector1,vector2):
	return dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))

# kNN分类器
# 测试集：testdata
# 训练集：trainSet
# 类别标签：listClasses
# k:k个邻居数
def classify(testdata, trainSet, listClasses, k):
	  # 返回样本集的行数
    dataSetSize = trainSet.shape[0]    
    # 计算测试集与训练集之间的距离：夹角余弦
    distances = array(zeros(dataSetSize))
    for indx in xrange(dataSetSize):
    	distances[indx] = cosdist(testdata,trainSet[indx])
    # 5.根据生成的夹角余弦按从大到小排序,结果为索引号
    sortedDistIndicies = argsort(-distances)  
    classCount={}     
    # 获取角度最小的前三项作为参考项          
    for i in range(k):  # i = 0~(k-1)  	  
    	  # 按序号顺序返回样本集对应的类别标签
        voteIlabel = listClasses[sortedDistIndicies[i]]
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
# testdata=[0.2,0.2]
# dataSet,labels = createDataSet()
# print classify(mat(testdata), mat(dataSet), labels, k)
dataSet,listClasses = loadDataSet()
nb = NBayes()
nb.train_set(dataSet,listClasses)
print classify(nb.tf[3], nb.tf, listClasses, k)
