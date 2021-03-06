from numba import njit
import numpy as np

@njit
def SignsToSector(signs):
    """Takes a boolean array and returns the integer given by those binary digits."""
    sum = 0
    for i in range(signs.shape[0]):
        if signs[i]: sum += 1 << i
    return sum

@njit
def SignsToSectors(signs):
    """Takes a boolean array and returns the integer given by those binary digits."""
    sum = np.zeros(signs.shape[0], dtype=np.int8)
    for i in range(signs.shape[0]):
        for j in range(signs.shape[1]):
            if signs[i,j]: sum[i] += 1 << j
    return sum

@njit
def Dist(x1,x2):
    """Distance between two points"""
    sum = 0.0
    for i in range(x1.shape[0]):
        dx = x1[i] - x2[i]
        sum += dx*dx
    return np.sqrt(sum)
