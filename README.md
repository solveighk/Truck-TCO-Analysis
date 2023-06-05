# Truck-TCO-Analysis

## Overview
This repo contains the source code for our master thesis "A TCO Study of the Transition to Battery Electric Trucks in Norway". We use Monte Carlo simulations to calculate the Total cost of Ownership (TCO) of owning Battery Electric Trucks (BETs) and Diesel Trucks (DTs). The resulats of the simulations are used to evaluate when investing in BETs is competitive with DTs, in different infrastructure scenarios and for different transport distances.  

## Files

- **run_simulations.py:** this is the main file used for running one round of TCO simulations. One round of simulations consist of 20 000 monte carlo simualtions, and is for a specific truck type, invesment year, infrastructure scenario, company size and transport distance. 
- **infrastructure.py:** calculates refueling inconvenience (RI), which is used to calculate the cost of waiting due to insufficient charging infrastucture. RI i varies depending on company size and infrastructure scenario. 
-**cost_functions.py:** functions used to calculate opex and capex.
- **energy_costs.py:** used to estimate charging and diesel costs.
- **truck.py:** initializes a truck object (BET or DT) that is used in the simulations.


### Plotting

The folder plotting/ are used to plot the main findings in our thesis. 

- **plot_histograms.py:** plots histograms with relative frequencies of TCO simulations for BETs and DTs in three different investment years
- **plot_company_sizes_mixed.py:** plots the develoment of average TCO for companies doing mixed transportations, and compares how TCO is affected by infrastructure development scenario and company size. 
- **plot_confidence_intervals.py:** plots development of average TCO with 90% confidence interval
- **plot_cost_split.py:** plots how costs are divided on components for BETs and DTs.
- **waiting_cost.py:** plots refueling inconvenience costs (waiting costs) for different transport distances and investment years


