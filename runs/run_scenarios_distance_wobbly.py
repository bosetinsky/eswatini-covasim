'''
Simple script for running Covasim scenarios
'''

import covasim as cv

# Run options
do_plot = 1
do_show = 1
verbose = 1
to_excel= 1  
do_save = 1         

# Sim options
basepars = dict(
  pop_size = 100000,
  verbose = verbose,
)


# For saving
version     = 'distance_8wobbly'
date        = '2020may11'
folder      = 'results'
basename    = f'{folder}/{date}_{version}'
fig_path    = f'{basename}.png'
obj_path    = f'{basename}.scens'
xlsx_path   = f'{basename}.xlsx'
#json_path   = f'{basename}.json'

# Scenario metaparameters
metapars = dict(
    n_runs    = 3, # Number of parallel runs; change to 3 for quick, 11 for real
    noise     = 0.1, # Use noise, optionally
    noisepar  = 'beta',
    rand_seed = 1,
    quantiles = {'low':0.1, 'high':0.9},
)

# Define the actual scenarios
interv_day = '2020-03-27'
s_close = '2020-03-17'
s_open = '2020-09-01'
interv_eff_40 = 0.6
interv_eff_50 = 0.5
interv_eff_60 = 0.4
interv_eff_70 = 0.3
interv_eff_80 = 0.2
 
scenarios = {'baseline': {
              'name':'Baseline',
              'pars': {
                  'interventions': None,
                  }
              }, 
             'distance1': {
              'name':'Stable Work Beta',
              'pars': {
                  'interventions': [
                                    cv.change_beta(days=interv_day, changes=0.75, layers='c'), 
                                    cv.change_beta(days=interv_day, changes=interv_eff_60, layers='w'), 
                                    cv.change_beta([s_close, s_open], [0, 1], layers='s'),    
                                    ]
                    }
             },         
             'distance2': {
              'name':'unstable work beta',
              'pars': {
                  'interventions': [
                                    cv.change_beta(days=interv_day, changes=0.75, layers='c'), 
                                    cv.change_beta(days=s_close, changes=0, layers='s'), 
                                    cv.change_beta([12, 20, 28, 39, 48, 59, 70, 90, 130], [.4, .8, 0.5, 0.7, 0.6, .5, 0.8, 0.6, 1], layers='w'), 
                                    ]
                    }
             },                   
             }

# Run the scenarios -- this block is required for parallel processing on Windows
if __name__ == "__main__":

    scens = cv.Scenarios(basepars=basepars, metapars=metapars, scenarios=scenarios)
    scens.run(verbose=verbose)
    scens.to_excel(xlsx_path)        
    if do_save:
         scens.save(scenfile=obj_path)
        
    if do_plot:
        fig1 = scens.plot(do_show=do_show)

