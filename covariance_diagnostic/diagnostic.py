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

        #Shape
        self.shape = np.shape(C)
        
        #Compute eigenvalues
        w, v = np.linalg.eig(C)
        self.eigenvalues = w
        self.eigenvectors = v

        #See if it is positive definite
        self.is_pos_def = np.all(self.eigenvalues > 0)

        #Compute degrees of freedom

    def recompute_DOF(self):
        pass
