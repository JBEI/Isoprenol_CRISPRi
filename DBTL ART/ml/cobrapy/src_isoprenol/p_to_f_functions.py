import numpy as np
from optlang.symbolics import add
import pandas as pd
#import cplex


def get_FBA_solution(model, substrate_uptake_rate = 100, verbose = False):
    with model:
        medium = model.medium
        medium = {key:1000 for (key,value) in model.medium.items()}
            
        # set the glucose uptake rate the specified value
        medium["EX_glc__D_e"] = substrate_uptake_rate
        model.medium = medium
        fba_solution = model.optimize()        
    return fba_solution

def get_isoprenolmax_solution(model, min_growth_rate, prot_df, substrate_uptake_rate = 100):
    with model:
        medium = model.medium
        medium = {key:1000 for (key,value) in model.medium.items()}
            
        # set the glucose uptake rate the specified value
        medium["EX_glc__D_e"] = substrate_uptake_rate
        model.medium = medium
        
        isoprenol_max_solution = Max_Isoprenol(model, prot_df, min_growth_rate)
        
    return isoprenol_max_solution


def Max_Isoprenol(model, prot_df, growth_rate_proportion, verbose = True):
    mi_model = model.copy()
    mi_model.tolerance = 1e-9
    #Calculate EFlux FBA solution
    for rxn in mi_model.reactions:
        if 'EX_' not in str(rxn.id):
            if rxn.gene_reaction_rule:
                if rxn.lower_bound < 0.0:
                    rxn.lower_bound = -prot_value_for_rxn(model, prot_df, rxn)
                else:
                    pass ## Could add some minimal flux through the pathway if transcript is present
                if rxn.upper_bound > 0.0:
                    rxn.upper_bound = prot_value_for_rxn(model, prot_df, rxn)
                else:
                    pass ## Could add some minimal flux through the pathway if transcript is present
            else:
                """When there is no GPR, the arbitrary bounds are removed. 
                Common arbitrary bound value of 1000 for E.coli, might be different depending on the model,
                e.g., 99999.0 for iMM904 yeast  model in BiGG"""
                if rxn.lower_bound <= -1000:
                    rxn.lower_bound = -np.Inf
                if rxn.upper_bound >= 1000:
                    rxn.upper_bound = np.Inf 
    fba_solution = mi_model.optimize()

    print('FBA status', fba_solution.status)
    print('FBA solution', fba_solution.objective_value)

    fba_objective_value = fba_solution.objective_value
    if fba_objective_value < 0:
        fba_objective_value = 0.0
    if verbose:
        display(mi_model.summary(solution=fba_solution))
        print('updating objective coefficients')
        
    for r in mi_model.reactions:
        if r.objective_coefficient:
            r.lower_bound = fba_objective_value*growth_rate_proportion
            r.upper_bound = fba_objective_value/growth_rate_proportion
            if verbose:
                print(r)
    if verbose:
        display(mi_model.objective.expression)
    mi_model.objective = mi_model.problem.Objective(
        add(
            [mi_model.reactions.get_by_id('EX_isoprenol_e').flux_expression]
        ),
        direction = 'max'
    )
    if verbose:
        display(mi_model.objective.expression)
    
    mi_solution = mi_model.optimize()
    if verbose:
        display(mi_model.summary(solution = mi_solution))
    
    print('Max Isoprenol status', mi_solution.status)
    print('Max Isoprenol solution', mi_solution.objective_value)
    print()
        
    return mi_solution, fba_solution

    
    
    
def create_gprdict(model):   
    gpr_dict = dict()
    for rxn in model.reactions:
        if rxn.gene_reaction_rule:
            temp = set()
            for x in [x.strip('() ') for x in rxn.gene_reaction_rule.split(' or ')]:
                temp.add(frozenset(y.strip('() ') for y in x.split(' and ')))
            gpr_dict[rxn.id] = temp
    return gpr_dict



def prot_value_for_rxn(model, prot_df, rxn):
    final_prot_value = 0
    gene_ids = []
    for parallel_gene in create_gprdict(model)[rxn.id]:
        prot_values = []
        for gene in parallel_gene:
            if gene in prot_df.index:
                prot_values.append(prot_df.loc[gene].to_numpy()[0])
#                 print(transcriptomics_df.loc[gene].to_numpy()[0])
            else:
                prot_values.append(np.inf)
            min_prot_val = np.min(prot_values)
        final_prot_value = final_prot_value + min_prot_val
#         if final_transcript_value==newinfbound:
#             display(rxn.id)
#             gene_ids.append(rxn.id)
    return final_prot_value