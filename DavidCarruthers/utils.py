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
    
    Putting this in utils so it's standardized across scripts
    """
    return 'ontrol' in x