import covariance_diagnostic as cd
import numpy as np
import numpy.testing as npt

def test_diagnostic():
    #Test it builds
    I = np.identity(3)
    d = cd.diagnostic(I)
    npt.assert_equal(True, d.is_pos_def)
    npt.assert_array_equal([3,3], d.shape)
    npt.assert_array_equal([1,1,1], d.eigenvalues)
    x = np.arange(3)
    for i in range(3):
        evec = 1*(x == i)
        npt.assert_array_equal(evec, d.eigenvectors[i])
    pass
