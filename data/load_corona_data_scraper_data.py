'''
This script creates a single file containing all the scraped 
data from the Corona Data Scraper.
'''

from cova_epi_scraper import Scraper

class CoronaDataScraperScraper(Scraper):
    pass

# Set up parameters

pars = dict()
pars['title'] = 'Corona Data Scraper Project Scraper'
pars['load_path'] = 'https://coronadatascraper.com/timeseries.csv'

pars['output_folder'] = 'epi_data/corona-data'

pars['renames'] = dict()
pars['renames']['name'] = 'key'
pars['renames']['cases'] = 'cum_positives'
pars['renames']['deaths'] = 'cum_death'
pars['renames']['tested'] = 'cum_tests'
pars['renames']['hospitalized'] = 'cum_hospitalized'
pars['renames']['discharged'] = 'cum_discharged'
pars['renames']['recovered'] = 'cum_recovered'
pars['renames']['active'] = 'cum_active'

pars['cumulative_fields'] = dict()
pars['cumulative_fields']['cum_positives'] = 'positives'
pars['cumulative_fields']['cum_death'] = 'death'
pars['cumulative_fields']['cum_tests'] = 'tests'
pars['cumulative_fields']['cum_hospitalized'] = 'hospitalized'
pars['cumulative_fields']['cum_discharged'] = 'discharged'
pars['cumulative_fields']['cum_recovered'] = 'recovered'
pars['cumulative_fields']['cum_active'] = 'active'


pars['fields_to_drop'] = [
    'growthFactor',
    'city',
    'county',
    'state',
    'country',
    'lat',
    'long',
    'url',
    'tz',
    'level'
]

CoronaDataScraperScraper(pars).scrape()
