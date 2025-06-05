# Automation and machine learning drive rapid optimization of isoprenol production in Pseudomonas putida

### <b>Citation</b>

This github repo describes the data analysis for the paper: Automation and machine learning drive rapid optimization of isoprenol production in Pseudomonas putida

In this project, automation and active learning were combined to dramatically increase isoprenol titer in Pseudomonas Putida by identifying combinations of genes to target using CRISPRi.  We performed 7 DBTL cycles, over which we achieved a titer increase of ~5x compared to the control. In each cycle, we used automation to construct a large set (60 or more) of strains expressing different combinations of CRISPRi sgRNA targeting different genes. We then evaluated their isoprenol produciton and measured their proteomics profiles. Using the proteomics data, we identified which strains successfully downregulated their targets, and filtered out strains which didn't exhibit proper downregulation. Using the accumulated filtered data, we trained an Automated Recommendataion Tool (ART) model to predict titer based on sgRNA combination in each strain, and used the model to propose designs for the next cycle. The repo is broken down into several principal directories that include the ART notebooks, dispense file generation, proteomics analysis, and the notebooks/data used to generate publication and supplementary figures.

<b> DBTL ART </b> For each cycle (except the first and last), there are 4 notebooks:
- DBTLX_A_normalize_and_recommend.ipynb: Analyze proteomics data to filter strains. 
- DBTLX_B_art_modeling_and_recommend.ipynb: Train an ART model, generate a set of all possible designs to use in the next cycle, and predict their titer using the model.  
- DBTLX_C_filter_recommendations.ipynb: Filter the recommendations to get a final list of 60 recommendations. 
- DBTLX_D_analyze_recs.ipynb: Visualize the predicted titers.
  
<b> DBTL Cycle Dispensing </b>
- DBTL Cycle Dispensing includes notebooks for the ECHO dispense list generation. A selection of new sgRNA arrays (2 to 4 sgRNAs) can be input alongside the set of placeholder plasmids harboring those sgRNAs.
- Notebook "A" computes the dispense lists for the simultaneous ligation and digestion step from a given set of recommendations for a given DBTL cycle.
- Notebook "B" computes the dispense list for the assembly. A final notebook "C" includes Fig. 2B, Fig. 2C, and Fig. S2.

<b> DBTL Proteomics Analysis </b>
- DBTL0_Heatmaps contains files for generating the DBTL0 heatmaps ultimately used in Fig. 5B and Fig. S8. Any pathway can be downloaded from, for example, Biocyc and formatted for the notebook to generate a new heatmap populated with statistically significant proteins that are significantly up/downregulated in a given pathway. The thresholds for p-val and fold-change may be altered accordingly. The current notebook is set to only consider those sgRNAs elucidated from the parent-child analysis.
- DBTLX_Heatmaps are analogous to DBTL0 however take into account all data from across the study.
- Figure_Data includes all the Top3.csv files, which are also available on the Environmental Data Depot (EDD) at JBEI as well as through the PRIDE database (https://www.ebi.ac.uk/pride/)

<b> Other Figures </b>
- Specific figure notebooks are annotated
- COG Analysis includes the initial COG categories that ultimately became Fig. 3A




