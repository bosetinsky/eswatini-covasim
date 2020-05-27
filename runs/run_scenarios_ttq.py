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
version     = 'TTQ_5'
date        = '2020may15'
folder      = 'results'
basename    = f'{folder}/covasim_scenarios_{date}_{version}'
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
test_day = '2020-05-20'
s_close = '2020-03-17'
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
               'Distance only': {
              'name':'Distancing Only',
              'pars': {
                  'interventions': [
                        cv.change_beta(days=interv_day, changes=interv_eff_60, layers='c'), 
                            cv.clip_edges(start_day=interv_day, change={'w':0.4}),
                            cv.clip_edges(start_day=s_close, change={'s':0.2}), 
                    ]
                  }
              },   
               't&qSymptomatic': {
              'name':'Test-and-quarantine Symptomatic',
              'pars': {
                  'interventions': [
                        cv.change_beta(days=interv_day, changes=interv_eff_60, layers='c'), 
                            cv.clip_edges(start_day=interv_day, change={'w':0.4}),
                            cv.clip_edges(start_day=s_close, change={'s':0.2}), 
                        cv.test_prob(start_day=test_day, symp_prob=0.1, asymp_prob=0.01, test_sensitivity=0.9, test_delay=1.0), 
                    ]
                  }
              },              
            't&q all': {
              'name':'Test-and-quarantine ALL',
              'pars': {
                  'interventions': [
                        cv.change_beta(days=interv_day, changes=interv_eff_60, layers='c'), 
                                    cv.clip_edges(start_day=interv_day, change={'w':0.4}),
                                    cv.clip_edges(start_day=s_close, change={'s':0.2}), 
                        cv.test_prob(start_day=test_day, symp_prob=0.5, asymp_prob=0, test_sensitivity=0.9, test_delay=1.0), 
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

