import numpy as np

class diagnostic(object):
    """
    Take in a covariance matrix and perform some diagnostics on it.
    :param C:
        2D array of a covariance matrix
    """

    def __init__(self, C):
        C = np.array(C)

        if C.ndim < 2:
            raise Exception("Covariance matrix has too few dimensions.")
        if C.ndim > 2:
            raise Exception("Covariance matrix has too many dimensions.")
        if not np.allclose(C, C.T, atol=1e-8):
            raise Exception("Covariance matrix is not symmetric.")
        self.C = C
        
        #Shape
        self.shape = np.shape(C)
        
        #Compute eigenvalues
        w, v = np.linalg.eig(C)
        self.eigenvalues = w
        self.eigenvectors = v

        #See if it is positive definite
        self.is_pos_semidef = np.all(self.eigenvalues >= 0)
        print(self.is_pos_semidef)
        print(self.eigenvalues)

        #Compute degrees of freedom
        self.recompute_DOF()

    def recompute_DOF(self, N_samples=10000):
        iC = np.linalg.inv(self.C)
        chi2s = np.zeros(N_samples)
        for i in range(N_samples):
            x = np.random.multivariate_normal(np.zeros(len(self.C)),
                                              self.C)#, size=N_samples)
            chi2s[i] = np.dot(x, np.dot(iC, x))
        from scipy import stats
        import matplotlib.pyplot as plt
        x = np.linspace(0, 20, 100)
        plt.hist(chi2s, density=True, bins=50)
        dof = len(iC)
        plt.plot(x, stats.chi2.pdf(x, dof))
        plt.axvline(dof, c="k", ls="--")
        plt.show()
        return

if __name__=="__main__":
    #Test it builds
    N = 5
    I = np.identity(N)
    for i in range(N-1):
        I[i, i+1] = I[i+1, i] = 0.576
    print I
    d = diagnostic(I)
    print(d)
