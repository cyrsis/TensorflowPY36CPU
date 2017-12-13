# ========================================================================= #
#                              Ensemble learning                            #
#                                    Goal:                                  #
# Combine prediction from many individual predictors to improve performance #
#                                                                           #
# ========================================================================= #
#Boostrap sample = same size of (sample with replacement)

import tensorflow as tf

# Bagging
from sklearn.ensemble import BaggingRegressor


