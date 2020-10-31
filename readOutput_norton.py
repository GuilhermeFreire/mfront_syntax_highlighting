# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

file_path = "./norton.res"
data = np.loadtxt(file_path)
fig1 = plt.subplots();

plt.plot(data[:,2],data[:,8],'b-h', label = 'Chaboche', linewidth = 0.5, markersize = 0.5)
plt.yscale('linear')
plt.grid(True)

plt.legend()

# first column: time
# 2 column: 1th component of the strain
# 3 column: 2th component of the strain
# 4 column: 3th component of the strain
# 5 column: 4th component of the strain
# 6 column: 5th component of the strain
# 7 column: 6th component of the strain
# 8 column: 1th component of the stress
# 9 column: 2th component of the stress
# 10 column: 3th component of the stress
# 11 column: 4th component of the stress
# 12 column: 5th component of the stress
# 13 column: 6th component of the stress
# 14 column: first  component of internal variable 'ElasticStrain'
# 15 column: second component of internal variable 'ElasticStrain'
# 16 column: third  component of internal variable 'ElasticStrain'
# 17 column: fourth  component of internal variable 'ElasticStrain'
# 18 column: fifth   component of internal variable 'ElasticStrain'
# 19 column: sixth   component of internal variable 'ElasticStrain'
# 20 column: p
# 21 column: first  component of internal variable 'a[0]'
# 22 column: second component of internal variable 'a[0]'
# 23 column: third  component of internal variable 'a[0]'
# 24 column: fourth  component of internal variable 'a[0]'
# 25 column: fifth   component of internal variable 'a[0]'
# 26 column: sixth   component of internal variable 'a[0]'
# 27 column: first  component of internal variable 'a[1]'
# 28 column: second component of internal variable 'a[1]'
# 29 column: third  component of internal variable 'a[1]'
# 30 column: fourth  component of internal variable 'a[1]'
# 31 column: fifth   component of internal variable 'a[1]'
# 32 column: sixth   component of internal variable 'a[1]'
# 33 column: stored energy
# 34 column: disspated energy