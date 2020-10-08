import numpy as np 

class Integration:
    """Integration by Euler's, RK2's, RK4's methods"""
    def euler(self, f, x0, t):
        '''Approximate the solution of x' = f(x) by Euler's method.

        ---------- Args ----------
        
        f : function
            Right-hand side of the differential equation x' = f(x, t)
        x : ndarray
            Initial value x(t0) = x0 where t0 is the entry at index 0 in the array t
        t : ndarray
            1D NumPy array of t values where we approximate x values. Time step
            at each iteration is given by t[n+1] - t[n].

        ---------- Return ----------

        x : ndarray
            Approximation x[n] of the solution x(t_n) computed by Euler's method.
        '''

        x = np.zeros((len(x0), len(x0)))
        x[:][0] = x0[:]

        for n in range(len(t)-1):
            deltaT = t[n + 1] - t[n]
            x[n + 1] = x[n] + f(x, t + deltaT / 2)[:][n] * deltaT

        return x

    def RK2(self, f, x0, t):
        '''Approximate the solution of x' = f(x) by RK2's method.

        ---------- Args ----------
        
        f : function
            Right-hand side of the differential equation x' = f(x, t)
        x : ndarray
            Initial value x(t0) = x0 where t0 is the entry at index 0 in the array t
        t : ndarray
            1D NumPy array of t values where we approximate x values. Time step
            at each iteration is given by t[n+1] - t[n].

        ---------- Return ----------

        x : 1D NumPy array
            Approximation x[n] of the solution x(t_n) computed by RK2's method.
        '''

        x = np.zeros((len(x0), len(x0)))
        x[:][0] = x0[:]

        for n in range(len(t)-1):
            deltaT = t[n + 1] - t[n]
            step = x[:] + f(x[:], t + deltaT / 2)[:][n] * deltaT / 2
            x[:][n + 1] = x[n] + f(step[:], t + deltaT / 2)[:][n] * deltaT


        return x

    def RK4(self, f, x0, t):
        '''Approximate the solution of x' = f(x) by RK4's method.

        ---------- Args ----------
        
        f : function
            Right-hand side of the differential equation x' = f(x, t)
        x : ndarray
            Initial value x(t0) = x0 where t0 is the entry at index 0 in the array t
        t : ndarray
            1D NumPy array of t values where we approximate x values. Time step
            at each iteration is given by t[n+1] - t[n].

        ---------- Return ----------

        x : 1D NumPy array
            Approximation x[n] of the solution x(t_n) computed by RK4's method.
        '''

        K = np.zeros((4, len(x0), len(x0)))

        x = np.zeros((len(x0), len(x0)))
        x[:][0] = x0[:]

        for n in range(len(t)-1):
            deltaT = t[n + 1] - t[n]
            K[0][:][n] = f(x[:], t)[:][n]
            K[1][:][n] = f(x[:] + K[0][:][n] * deltaT / 2, t + deltaT / 2)\
                                                                        [:][n]
            K[2][:][n] = f(x[:] + K[1][:][n] * deltaT / 2, t + deltaT / 2)\
                                                                        [:][n]
            K[3][:][n] = f(x[:] + K[2][:][n] * deltaT, t + deltaT)[:][n]

            x[:][n + 1] = x[:][n] + (K[0][:][n] + 2 * K[1][:][n]\
                        + 2 * K[2][:][n] + K[3][:][n]) * deltaT / 6



        return x
        