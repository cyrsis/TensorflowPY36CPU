# -*- coding: utf-8 -*-

import sys  
import os
import time
from numpy import *
import scipy.spatial.distance as dist



Vector1 = array([1,1,0,1,0,1,0,0,1])
Vector2 = array([0,1,1,0,0,0,1,1,1])
matV = mat([Vector1 ,Vector2])
print(matV)
print("dist.jaccard:", dist.pdist(matV, 'jaccard'))
