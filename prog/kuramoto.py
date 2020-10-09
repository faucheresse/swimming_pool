import numpy as np 
import matplotlib.pyplot as plt
from settings import * 
from integrator import *
from math import ceil

class KuramotoModel:

    def __init__(self, omega, kappa):

        self.N = N
        self.omega = omega
        self.integr = Integration()
        self.kappa = kappa
        self.n = 1

    def __call__(self, theta, t):
        self.d_theta = np.zeros((self.N, len(t)))
        K = np.zeros((self.N, self.N))
        for i in range(len(K)):
            i = i % self.N
            for j in range(len(K)):
                if abs(i-j) <= self.n:
                    K[i, j] = self.kappa

        for i in range(self.N):
            self.d_theta[i, :] = self.omega[i] + (1 / self.N)\
                        * sum(K[i, j] * np.sin(theta[j, :] - theta[i, :])\
                                for j in range(i - self.n, 1 + self.n))
        

        return self.d_theta

    def integrate(self, f, theta0, tf=100, integrator="RK4"):
        t = np.linspace(0, tf, 1000)

        if integrator == "RK4":
            theta = self.integr.RK4(self, theta0, t)
        elif integrator == "RK2":
            theta = self.integr.RK2(self, theta0, t)
        elif integrator == "Euler":
            theta = self.integr.euler(self, theta0, t)

        return t, theta%(2 * np.pi)

    def graph_kuramoto(self, t, theta, integrator="RK4"):     
        plt.plot(t, theta, label="Kuramoto ({0})".format(integrator))
        plt.xlabel(r"$t$")
        plt.ylabel(r"$\theta$")
        plt.title("Kuramoto integrate by %s"%integrator)
        plt.grid()
        plt.show()

    def all_graph_kuramoto(self, t, theta):
        for i in range(len(theta)):
            plt.plot(t, theta[i], label="Kuramoto ({0})".format(i))
        plt.xlabel(r"$t$")
        plt.ylabel(r"$\theta$")
        plt.title("Kuramoto")
        plt.grid()
        plt.show()

    def orders(self, theta, t):
        z = np.zeros(self.N)
        R, phi = np.zeros(len(t)), np.zeros(len(t))
        for _t in range(len(t)):
            z = sum(np.exp(1j * theta[i][_t])\
                    for i in range(self.N)) / self.N

            R[_t] = np.absolute(z)
            phi[_t] = np.angle(z)

        return R, phi

    def graph_orders(self, theta, t):
        R, phi = self.orders(theta, t)
        plt.plot(t, R, label=r"$t \longmapsto R(t)$")
        plt.plot(t, phi, label=r"$t \longmapsto \Phi(t)$")

        plt.xlabel(r"$t$")
        plt.ylabel(r"$R, \Phi$")
        plt.legend()
        plt.grid()
        plt.show()

    def shanon_entropy(self, theta, t):
        n = self.n
        q = len(t) // 2 # en attendant
        p = np.zeros(len(t))
        S = np.zeros(len(t))
        count = 0


        for i in range(len(t)):
            count += 1
            ib = (i - n) % self.N
            ia = (i + n) % self.N
            for a in range(q):
                inf = (2 * np.pi * a) / q
                sup = (2 * np.pi * (a + 1)) / q
                p[a] = sum(theta[k-1] for k in range(ib, ia)\
                        if inf <= theta[k-1] <  sup) / (2 * n + 1)

            S[i] = -sum(p[a] * np.log(p[a]) for a in range(q) if p[a] != 0)
            print(count)

        return S

    def graph_shanon_entropy(self, theta, t):
        S = self.shanon_entropy(theta, t)
        i = np.arange(len(t))
        plt.plot(i, S, label=r"$i \longmapsto S_i^{q, n}(t)$")

        plt.xlabel(r"$i$")
        plt.ylabel(r"$S$")
        plt.legend()
        plt.grid()
        plt.show()

    def graph_density_shanon_entropy(self, theta, t):
        S = np.zeros((len(t), len(t)))
        ind = np.arange(len(t))
        for i in range(len(t)):
            S[:, i] = self.shanon_entropy(theta[:, i], t)
            plt.plot(ind, S[:, i])

        plt.xlabel(r"$i$")
        plt.ylabel(r"$S$")
        plt.legend()
        plt.grid()
        plt.show()

