import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def import_proteomics_data_for_ml(data_file = './data/normalized_proteomics_pivot.csv'):
    #Import data
    omics = pd.read_csv(data_file, index_col = 0)
    # Drop cell lines with missing isoprenol
    omics = omics.dropna(axis = 0, how = 'any', subset=['isoprenol'])
    # Drop proteins with any missing values
    omics = omics.dropna(axis = 1, how = 'any')

    
    # Merge data by replicate
    omics_mean = omics.copy()
    omics_mean['cycle'] = [x[-1] for x in omics_mean.index.values]
    omics_mean['cycle'].value_counts()
    # omics_mean['line_name'] = omics_mean.apply(lambda x: x.index.values.split('-')[0], axis = 1)
    omics_mean['line_name'] = [f"{x.split('-')[0]}_c{x[-1]}" for x in omics_mean.index.values]
    omics_mean['is_control'] = ['ontrol' in x for x in omics_mean['line_name']]
    omics_mean.loc[omics_mean['is_control'], 'line_name'] = omics_mean.loc[
        omics_mean['is_control'], 'line_name'].apply(lambda x: f'Control_c{x[-1]}')
    omics_metadata = omics_mean[['cycle', 'is_control']].copy()
    omics_mean = omics_mean.drop(['cycle', 'is_control'], axis = 1)

    omics_mean = omics_mean.groupby('line_name').mean()
    omics_mean.shape
    
    # Get protein columns:
    protein_measurements = omics.columns[:-1]
    X = omics[protein_measurements]
    y = omics['isoprenol']
    X_mean = omics_mean[protein_measurements]
    y_mean = omics_mean['isoprenol']
    
    output_dict = {}
    output_dict['X'] = X
    output_dict['y'] = y
    output_dict['X_mean'] = X_mean
    output_dict['y_mean'] = y_mean
    
    return output_dict