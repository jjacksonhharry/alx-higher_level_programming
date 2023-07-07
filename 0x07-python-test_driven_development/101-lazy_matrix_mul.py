#!/usr/bin/python3
""" Module containing function that multiplies two matrices """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Return products of two matrices

    Args:
         m_a (list of lists) = 1st matrix
         m_b (list of lists) = 2nd matrix
    """

    return  (np.matmul(m_a, m_b))

