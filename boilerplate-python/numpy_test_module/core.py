
from . import helpers
import numpy as np

class NumpyTestModule(object):

    def __init__(self):
        self.variable_of_object ='123'
        print("[message] NumpyTestModule constructor")
        pass

    def print_numpy_examples(self):

        A = np.array( [ [1, 2, 3],
                        [3, 2, 1],
                        [1, 0, -1] ])

        eigenvalues, eigenvectors = helpers.get_eigen_vectors(A)
