# ========================================================================= #
#                             Using Multiple Layer networking               #
#                                                                          #
# :                                                                         #
# ========================================================================= #
# -*- coding: utf-8 -*-
# __author__ = 'Victor Tong'
# --github-- = 'cyrsis

import  tensorflow as tf
import matplotlib.pyplot as plt
import csv
import os
import os.path
import random
import numpy as np
import requests
from tensorflow.python.framework import ops
ops.reset_default_graph()

#bring in some data

# Low Birthday data:
# Colums Variables                       Abbreviation
#-----------------------------------------------------
#low Birthday Weight(0 = Birthday Weight >=2500g,
#                    1 = Birthday weight < 25000g,
# Age of the Mother in Years
# Weight in Pounds at the last Menstrual Period
# Race (1= white, Black, 3= Other)
# Smoking Status During Pregnancy (1 = Yes, 0 =No)
# History of Premature Labor (0 =None, 1 = one,etc)
# Presence of Uterine Irritability(1 = YES, 0 = No)
# Birth Weight in Grams
#------------------------------------------------------


