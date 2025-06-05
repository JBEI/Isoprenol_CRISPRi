import edd_utils as eddu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re 
import random


def find_control(x: str):
    """
    Check if a string contains the string 'ontrol'
    
    Putting this in utils so it's standardized across scripts.
    """
    return 'ontrol' in x


def set_plot_config(return_configs = False):
    line_size = 0.5
    custom_params = {
        'axes.facecolor': 'white',
        'axes.edgecolor': 'black',
        'axes.grid': False,
        'axes.axisbelow': 'line',
        'axes.labelcolor': 'black',
        'figure.facecolor': 'white',
        'axes.spines.right': True,
        'axes.spines.bottom': True,
        'xtick.direction': 'inout',
        'ytick.direction': 'in',
        'xtick.bottom': True,
        'xtick.minor.visible': False,
        'xtick.major.bottom':  True,
        'xtick.minor.bottom':  True,
        'xtick.major.pad':     7,     # distance to major tick label in points#
        'xtick.minor.pad':     3.4,     # distance to the minor tick label in points#
        'xtick.major.size':    10,
        'ytick.major.size':    4,
        'xtick.major.width':   line_size,
        'ytick.major.width':   line_size,
        'axes.linewidth': line_size,
        'xtick.minor.size':    2,
        'pdf.fonttype': 42
    }
    
    sns.set_theme(
        style="ticks",
        rc=custom_params,
        font="DejaVu Sans",
        font_scale=0.7
    )

    enmax_palette = ["#648FFF", "#FE6100", "#785EF0", "#DC267F", "#FFB000"]
    # enmax_palette = ["#000000", "#FE6100", "#785EF0", "#DC267F", "#FFB000"]

    sns.set_palette(palette=enmax_palette)
    
    if return_configs: 
        return custom_params, enmax_palette