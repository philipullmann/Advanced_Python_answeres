#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:30:16 2024

@author: philip
"""

import numpy as np
import scipy


mat = np.array([[1, -2, 3],
                [4, 5, 6],
                [7, 1, 9]])

vec = np.array([1, 2, 3])


solv = scipy.linalg.solve(mat,vec)
print("Solution:  ", solv)
print("Vecotr b calculated ", np.dot(mat,solv))

ra_mat = np.random.randint(1,10,9).reshape(3,3)
solv = scipy.linalg.solve(mat,ra_mat)
print("Solution:  ", solv)
print("Random Mat: ", np.dot(mat,solv))


eig_val, eig_vec = scipy.linalg.eig(mat)

print("Eigenvalues of A: ", eig_val)
print("Eigenvectors of A: ", eig_vec)

inverse = scipy.linalg.inv(mat)
print("Inverse of A: ", inverse)
determinate = scipy.linalg.det(mat)
print("Determinate of A: ", determinate)


norm1 = scipy.linalg.norm(mat, ord=1)
norm2 = scipy.linalg.norm(mat, ord=2)
print("Norm of A (order1): ", norm1)
print("Norm of A (order2): ", norm2)