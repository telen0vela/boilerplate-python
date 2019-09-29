
import numpy as np
from numpy import linalg as LA


def get_eigen_vectors(inputMatrix):
    return LA.eig(inputMatrix)

def get_eigen_vectors_test(inputMatrix):
    """" Depricated """

    # read out dimensions of inputMatrix
    dimension = inputMatrix.shape
    # todo throw error for non-square matrix

    # create unit matrix with numpy
    unit = np.eye( dimension[0], dimension[1] )

    determinante = np.linalg.det()

    print(unit)
