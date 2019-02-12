#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imitation Learning for Point Process

A Hawkes processes based model for generating marked spatial-temporal points.

References:

Dependencies:
- Python 3.6.7
- tensorflow==1.5.0
"""

class MarkedSpatialTemporalHawkesProcess(object):
    """
    Marked Spatial Temporal Hawkes Process

    A stochastic marked spatial temporal points generator based on Hawkes process.
    """

    def __init__(self, T, m_dim):
        """
        Params:
        - T:     maximum time
        - m_dim: number of categories of marks
        """
        
