# =========================================
# AIML WEEK 2 ASSIGNMENT
# NumPy, Pandas & Matplotlib
# =========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# SECTION 1: NUMPY
# ===============================

# Create array from 1 to 20
arr = np.arange(1, 21)
print("Array (1 to 20):\n", arr)

# Reshape into 4x5 matrix
matrix = arr.reshape(4, 5)
print("\n4x5 Matrix:\n", matrix)

# Mean, Median, Standard Deviation
print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# Extract even numbers
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers:\n", even_numbers)

# Random 5x5 matrix and transpose
random_matrix = np.random.randint(1, 100, (5, 5))
print("\nRandom 5x5 Matrix:\n", random_matrix)
print("\nTranspose:\n", random_matrix.T)

# ============================
