'''
This script creates a single file containing all the scraped 
data from the Covid Data Project Data Scraper.
https://covidtracking.com
'''

from cova_epi_scraper import Scraper
import datetime as dt

def covid_tracking_date_to_date(d):
    return dt.date((d // 10000), ((d % 1000) // 100), (d % 1000) % 100)

class CovidTrackingProjectScraper(Scraper):
    def create_date(self):
        self.df['date'] = self.df.date.apply(covid_tracking_date_to_date)


class CovidUSTrackingProjectScraper(CovidTrackingProjectScraper):
    def create_key(self):
        self.df['key'] = 'US'


## Set up parameters 
pars_state = dict()
pars_state['title'] = "Covid Tracking Project Scraper for US states"
pars_state['load_path'] = "https://covidtracking.com/api/v1/states/daily.csv"

pars_state['output_folder'] = "epi_data/covid-tracking"

pars_state['renames'] = dict()
pars_state['renames']['state'] = "key"
pars_state['renames']['positiveIncrease'] = "new_positives"
pars_state['renames']['negativeIncrease'] = "new_negatives"
pars_state['renames']['totalTestResultsIncrease'] = "new_tests"
pars_state['renames']['hospitalizedIncrease'] = "new_hospitalized"
pars_state['renames']['deathIncrease'] = "new_death"
pars_state['renames']['inIcuCumulative'] = "cum_in_icu"
pars_state['renames']['hospitalizedCumulative'] = "cum_hospitalized"
pars_state['renames']['onVentilatorCumulative'] = "cum_on_ventilator"

pars_state['cumulative_fields'] = dict()
pars_state['cumulative_fields']['cum_in_icu'] = "num_icu"
pars_state['cumulative_fields']['cum_on_ventilator'] = "num_on_ventilator"


pars_state['fields_to_drop'] = [
    "hash",
    "dateChecked",
    "fips",
    "totalTestResults",
    "posNeg",
    "positive",
    "negative",
    "pending",
    "hospitalizedCurrently",
    "inIcuCurrently",
    "onVentilatorCurrently",
    "recovered",
    "hospitalized",
    "total"
]

# Set up US parameters
parameter_us = dict()
parameter_us['title'] = "Covid Tracking Project Scraper for US states"
parameter_us['load_path'] = "https://covidtracking.com/api/v1/us/daily.csv"

pars_state['output_folder'] = "epi_data/covid-tracking"

parameter_us['renames'] = dict()
parameter_us['renames']['positiveIncrease'] = "new_positives"
parameter_us['renames']['negativeIncrease'] = "new_negatives"
parameter_us['renames']['totalTestResultsIncrease'] = "new_tests"
parameter_us['renames']['hospitalizedIncrease'] = "new_hospitalized"
parameter_us['renames']['deathIncrease'] = "new_death"
parameter_us['renames']['inIcuCumulative'] = "cum_in_icu"
parameter_us['renames']['hospitalizedCumulative'] = "cum_hospitalized"
parameter_us['renames']['onVentilatorCumulative'] = "cum_on_ventilator"

parameter_us['cumulative_fields'] = dict()
parameter_us['cumulative_fields']['cum_in_icu'] = "num_icu"
parameter_us['cumulative_fields']['cum_on_ventilator'] = "num_on_ventilator"


parameter_us['fields_to_drop'] = [
    "hash",
    "dateChecked",
    "fips",
    "totalTestResults",
    "posNeg",
    "positive",
    "negative",
    "pending",
    "hospitalizedCurrently",
    "inIcuCurrently",
    "onVentilatorCurrently",
    "recovered",
    "hospitalized",
    "states",
    "total"
]

# Scrape states
CovidTrackingProjectScraper(pars_state).scrape()
# Scrape US
CovidUSTrackingProjectScraper(parameter_us).scrape()


