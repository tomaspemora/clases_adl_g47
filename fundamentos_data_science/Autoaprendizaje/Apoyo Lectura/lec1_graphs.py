#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: lec1_graphs.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description: Ancilliary file for lecture 1 - Data Science adl
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# !head alumnos.csv -> powershell -> gc alumnos.csv | select -first 10
# !tail alumnos.csv -> powershell -> gc log.txt | select -last 10  # tail


def graph_normal_distribution(xaxis, mu, sigma):
    """docstring for graph_normal_distribution"""
    plt.plot(xaxis, stats.norm.pdf(xaxis, mu, sigma), color='dodgerblue')
    plt.axvline(x=mu, color='tomato', lw=2)


df = pd.read_csv('alumnos.csv')
df.head()
