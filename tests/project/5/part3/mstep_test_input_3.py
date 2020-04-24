import numpy as np
import common

#  Test: output3
#  Output:
#  Input:
X = np.array([
   [0.71412118, 0.3107728,  0.17604900],
   [0.67194715, 0.88702645, 0.65614617],
   [0.54812561, 0.97668549, 0.11344129],
   [0.0151568,  0.52031979, 0.2070992 ],
   [0.5065715,  0.12056714, 0.9258414 ],
   [0.23410788, 0.49456094, 0.05887604],
   [0.88187528, 0.27765549, 0.2986572 ],
   [0.90080239, 0.43536892, 0.69437366],
   [0.52461778, 0.80239982, 0.17114877],
   [0.30720593, 0.85717043, 0.89019952]])

K = 7

post = np.array([
   [0.13237083, 0.1336538,  0.1899142,  0.08264727, 0.04681867, 0.17869839, 0.23589683],
   [0.21605259, 0.18048411, 0.3215982,  0.03735339, 0.00499076, 0.17132835, 0.06819261],
   [0.15720316, 0.03741532, 0.28731422, 0.07265016, 0.15347595, 0.01827087, 0.27367032],
   [0.07058065, 0.07591934, 0.22898601, 0.11067177, 0.17651136, 0.13335903, 0.20397185],
   [0.0532819,  0.0956391,  0.2668536,  0.27713619, 0.12063235, 0.09340412, 0.09305273],
   [0.15007346, 0.32993049, 0.03398412, 0.19767351, 0.06672806, 0.03342314, 0.18818721],
   [0.11447092, 0.22990427, 0.03854194, 0.14122452, 0.06970123, 0.21779597, 0.18836114],
   [0.1787106,  0.05587748, 0.19302658, 0.00364463, 0.19072106, 0.21712463, 0.16089502],
   [0.10195809, 0.20145734, 0.11422507, 0.10097602, 0.22425354, 0.21529158, 0.04183835],
   [0.02359103, 0.3434686,  0.04767286, 0.05502425, 0.25615097, 0.21261869, 0.0614736 ]])

#  Output:
mu = np.array([
   [0.59395679, 0.59694061, 0.37754773],
   [0.49196875, 0.59189262, 0.42618544],
   [0.5448225,  0.59246037, 0.4535476 ],
   [0.47264785, 0.45182595, 0.41651106],
   [0.48086538, 0.61844679, 0.45859544],
   [0.58728795, 0.55825559, 0.47202943],
   [0.53476122, 0.54114134, 0.32110968]])

var = np.array([0.07215951, 0.08120291, 0.08584913, 0.08946518, 0.08693313, 0.07723237, 0.07903483])

p = np.array([0.11982932, 0.16837498, 0.17221168, 0.10790017, 0.1309984,  0.14913148, 0.15155397])

def data():
    return X, common.GaussianMixture(mu, var, p), post