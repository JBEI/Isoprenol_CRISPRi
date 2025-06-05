# Automation of a CRISPRi platform for enhanced isoprenol production in Pseudomonas putida (working title)

This github repo describes the data analysis for the paper: XXX

In this project, automation and active learning were combined to dramatically increase isoprenol titer in Pseudomonas Putida by identifying combinations of genes to target using CRISPRi.  We performed 7 DBTL cycles, over which we achieved a titer increase of ~5x compared to the control. In each cycle, we used automation to construct a large set (60 or more) of strains expressing different combinations of CRISPRi sgRNA targeting different genes. We then evaluated their isoprenol produciton and measured their proteomics profiles. Using the proteomics data, we identified which strains successfully downregulated their targets, and filtered out strains which didn't exhibit proper downregulation. Using the accumulated filtered data, we trained an Automated Recommendataion Tool (ART) model to predict titer based on sgRNA combination in each strain, and used the model to propose designs for the next cycle. 

For each cycle (except the first and last), there are 4 notebooks:
- DBTLX_A_normalize_and_recommend.ipynb: Analyze proteomics data to filter strains. 
- DBTLX_B_art_modeling_and_recommend.ipynb: Train an ART model, generate a set of all possible designs to use in the next cycle, and predict their titer using the model.  
- DBTLX_C_filter_recommendations.ipynb: Filter the recommendations to get a final list of 60 recommendations. 
- DBTLX_D_analyze_recs.ipynb: Visualize the predicted titers.


This repo also includes folders to generate publication figures and store data related to the project. 

