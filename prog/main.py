import numpy as np 
import matplotlib.pyplot as plt 
from kuramoto import *
from settings import *

'''
Test d'intégration pour la fonction exponentielle
'''
# t = np.linspace(0, 2, 100)
# x0 = 1
# f = lambda x, t : x

# intgr = Integration()

# #---------- Test by Euler's method ----------#

# y1 = intgr.euler(f, x0, t)

# #---------- Test by RK2's method ----------#

# y2 = intgr.RK2(f, x0, t)

# #---------- Test by RK4's method ----------#

# y3 = intgr.RK4(f, x0, t)

# # plt.plot(t, y1, label="Euler")
# # plt.plot(t, y2, label="RK2")
# # plt.plot(t, y3, label="RK4")
# plt.plot(t, np.exp(t), label="exp")
# plt.legend()
# plt.grid()
# plt.show()

#------------------------------------------------------------#
kuramoto = KuramotoModel(omega)
f  = kuramoto
t, theta = kuramoto.integrate(f, theta0, 30)
# t1, theta1 = kuramoto.integrate(f, theta0, 100, "RK2")
# t2, theta2 = kuramoto.integrate(f, theta0, 100, "Euler")

R, phi = kuramoto.R_exp_i_phi(f, theta)

plt.plot(t, theta%(2 * np.pi), label="Kuramoto (RK4)", marker="+")
# plt.plot(t, theta1%(2 * np.pi), label="Kuramoto (RK2)", marker="+")
# plt.plot(t, theta2%(2 * np.pi), label="Kuramoto (Euler)", marker="+")
plt.plot(t, R, label=r"$t \longmapsto R(t)$", marker="+")
plt.plot(t, phi, label=r"$t \longmapsto \Phi(t)$", marker="+")

plt.xlabel(r"$t$")
plt.ylabel(r"$\theta$")
plt.legend()
plt.grid()
plt.show()
