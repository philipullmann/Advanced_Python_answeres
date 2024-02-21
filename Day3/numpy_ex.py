#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:43:02 2024

@author: philip
"""

import numpy as np

vec = np.zeros(10)
vec[5] = 1


vec_10_49 = np.arange(10,50,1)
vec_49_10 = np.flip(vec_10_49)

vec_3x3 = np.arange(0,9).reshape(3,3)


# Indices Search
vec_search = np.array([1,2,0,0,4,0])
vec_index = np.where(vec_search == 0)


# Random
vec_random = np.random.random(30)
mean_of_vr = np.mean(vec_random)


# Vector 2D
vector_2d = np.zeros(25).reshape(5,5)
vector_2d[0,:] = 1
vector_2d[4,:] = 1
vector_2d[:,0] = 1
vector_2d[:,4] = 1


# Checkboard
vector_8x8 = np.zeros(64)
vector_8x8[::2] = 1
vector_8x8 = vector_8x8.reshape(8, 8)
vector_8x8[1::2] = vector_8x8[1::2, ::-1]

# Chessboard Tile
a = np.array([[0,1],
             [1,0]])
vector_tile = np.tile(a,(4,4))


# Negate
Z = np.arange(11)
Z[(Z > 3) & (Z < 8)] *= -1


# Sort
Y = np.random.random(10)
Y = np.sort(Y)

# Compare
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

equal_tot = np.array_equal(A, B)
equal_pos = np.equal(A,B)
print("Array equal?:", equal_tot)
print("Array elements equal?:", equal_pos)


Z_convert = np.arange(10, dtype=np.int32)
print(Z_convert.dtype)

Z_convert = Z_convert.astype(np.float32)
print(Z_convert.dtype)

