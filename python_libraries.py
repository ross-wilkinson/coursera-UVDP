#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:43:05 2021

@author: rosswilkinson
"""

# =============================================================================
# NUMPY
# =============================================================================

import numpy as np

### Numpy Array

# Create a 3x1 numpy array
a = np.array([1,2,3])

# Print object type
print(type(a))

# Print shape
print(a.shape)

# Print some values in a
print(a[0], a[1], a[2])

# Create a 2x2 numpy array
b = np.array([[1,2],[3,4]])

# Print shape
print(b.shape)

# Print some values in b
print(b[0,0], b[0,1], b[1,1])

# Create a 3x2 numpy array
c = np.array([[1,2],[3,4],[5,6]])

# Print shape
print(c.shape)

# Print some values in c
print(c[0,1], c[1,0], c[2,0], c[2,1])

# 2x3 zero array 
d = np.zeros((2,3))
print(d)

# 4x2 array of ones
e = np.ones((4,2))
print(e)

# 2x2 constant array
f = np.full((2,2), 9)
print(f)

# 3x3 random array
g = np.random.random((3,3))
print(g)

### Array Indexing

# Create 3x4 array
h = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])
print(h)

# Slice array to make a 2x2 sub-array
i = h[:2, 1:3]
print(i)

print(h[0,1])

# Modify the slice
i[0,0] = 1738

# Print to show how modifying the slice also changes the base object
print(h[0,1])

### Datatypes in Arrays

# Integer
j = np.array([1, 2])
print(j.dtype)  

# Float
k = np.array([1.0, 2.0])
print(k.dtype)         

# Force Data Type
l = np.array([1.0, 2.0], dtype=np.int64)
print(l.dtype)



