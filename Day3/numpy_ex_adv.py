#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:49:53 2024

@author: philip
"""

import numpy as np


inp_mat = np.array([[1.0, 2.0, 10],
           [3.0, 4.0, 20],
           [5.0, 6.0, 30],
           [7.0, 8.0, 40]])

for i in range(0, len(inp_mat)):    
    inp_mat[i] = inp_mat[i]/inp_mat[i][-1]
    


# Fancy indexing

mat3x3 = np.random.random(9).reshape(3,3)
print(mat3x3)
rows = np.array([0, 1, 2])
cols = np.array([0, 1, 2])
print(mat3x3[rows, cols])

print("-----------")

# 10x3 
mat10x3 = np.random.random(30).reshape(10,3)
print(mat10x3)
mat10x3_temp = 1/np.abs(mat10x3-0.75)
mat_res = np.argmax(mat10x3_temp, axis=1)

print("Index in rows:", mat_res)

print("-----------")

# Empty with dimension 10x8x6
x = np.empty((10, 8, 6))

# Select from first dimension(3 times)
idx0 = np.zeros((3, 8)).astype(int)
# Select from second dimension
idx1 = np.zeros((3, 1)).astype(int)
# Select third dimension (0) -> 1 Dimension
idx2 = np.zeros((1, 1)).astype(int)

x[idx0, idx1, idx2]

# Explanation:
# idx0 will create array (3, 8)
# idx1 will create array (3, 1)
# Both broadcasted together -> (3,8)
# idx2 will create array (1, 1)
# Broadcasted with first output will yield (3,8)

# 1:(3, 8)
# 2:(3, 1)
# --------------
# R:(3, 8)
# 3:(1 ,1)
# --------------
# R:(3, 8)


### Very Advanced
# x is stored in 48 bytes in memory (12*4[int32])
# Stide give number of bytes to go to move to next axis position
# x.strides (16,4). 4 bytes go to next column, 16 bytes to go to next row

def as_strided(mat, shape, strides):
    return np.lib.stride_tricks.as_strided(mat, shape=shape,
                                           strides=strides)

x_c = np.arange(12, dtype=np.int32).reshape((3, 4), order="C")
x_f = np.arange(12, dtype=np.int32).reshape((3, 4), order="F")

"""
x_c = np.array([[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]], dtype=np.int32)

x_f = np.array([[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]], dtype=np.int32, order="F")
"""


Z_c = as_strided(x_c, shape=(2,3,2,2), strides = (16, 4, 16, 4))
Z_f = as_strided(x_f, shape=(2,3,2,2), strides = (16, 4, 16, 4))

# Shape defines Z shape=(2,3,2,2)
# strides define the memory borders to create new array
# Z.strides=(16, 4, 16, 4)
# 16 [4 num] to go first Dimension e.g. 0(idx=0,0) -> 4(idx=1,0)
# 4 [1 num]  to go second Dimension e.g 0(idx=0,0) -> 1(idx=0,1)
# 16 [4 num] to go third Dimension e.g  0(idx=0,0) -> 4(idx=1,0)
# 4 [1 num]  to go fourth Dimension e.g 0(idx=0,0) -> 1(idx=0,1)
    
# This will create with the shape
# First Dimension [16]
#   [ 0,  1]  move along dim1  [ 4,  5]
#   [ 4,  5]     --->          [ 8,  9]

# Second Dimension [4]
#   [ 0,  1]  move along dim2  [ 1,  2]
#   [ 4,  5]     --->          [ 5,  6]    
    
# Third Dimension [16]
#   [ 0,  1]  move along dim3  [ 4,  5]
#                --->   

# Fourth Dimension [4]
#   [ 0]      move along dim4  [ 4]
#              s   --->   
    


