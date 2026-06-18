import numpy as np
from scipy.ndimage import convolve

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Kernel for 4-way adjacency (excludes the center cell itself)
kernel_4_way = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# 'constant' mode with cval=0 treats out-of-bound edges as zeros
result = convolve(matrix, kernel_4_way, mode='constant', cval=0)

print(result)
# Output will be a matrix where every cell is replaced by its neighbors' sum:
# [[ 6 10 14]
#  [16 20 24]
#  [26 30 34]]