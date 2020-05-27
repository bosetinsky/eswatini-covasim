import synthpops as sp

sp.validate()

datadir = sp.datadir # this should be where your demographics data folder resides

location = 'seattle_metro'
state_location = 'Washington'
country_location = 'usa'
sheet_name = 'United States of America'


npop = 10000 # how many people in your population
sp.generate_synthetic_population(npop,datadir,location=location,
                                 state_location=state_location,country_location=country_location,
                                 sheet_name=sheet_name)