
import random
import matplotlib.pyplot as plt
import numpy as np
random.seed(488)
np.random.seed(555)

#import functions and classes from other files
from energy_costs import get_charging_prices, get_diesel_costs
from cost_functions import get_opex, get_tco, get_bet_capital_cost, get_dt_capital_cost
from infrastructure import RI
from truck import Truck
import GLOB_VAR

# Monte Carlo simulation of total ownership costs with uncertainty 
def monte_carlo_simulation(truck, no_simulations, toll_rate, discount_rate, delivery_year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.4, case = "slow", length = "short_haul", co_size = "large", waiting_cost_scen = "base", charger_scen="base"):
  ''' Run montecarlo simulations generate TCO distribution for trucks
      Parameters
      ----------
      truck_el : Truck
        A battery electric truck
      truck_diesel : Truck
        A diesel truck
      simulation_type : String
        "el" for electric and "diesel" for diesel
      no_simulations : Int
        Number of monte carlo simulations
      el_surcharge : Int
        extra surcharge in NOK/kWh to charging station owner
      toll : int
        Yearly toll cost in NOK for a diesel truck
      discount_rate : float
        Discount rate
  '''
  tco_list = []
  total_energy_list = []
  total_other_opex_list = []
  total_capex_list = []
  total_ri_list = []
  toll = truck.yearly_dist*toll_rate
  for i in range(no_simulations):
    if truck.fueltype == "el":
    #  refueling_inconvenience_list = refueling_inconvenience(truck.lifetime, delivery_year, "med")
      refueling_inconvenience_list = RI(lifetime = truck.lifetime, start_year = delivery_year, case=case, length=length, co_size = co_size, waiting_cost=waiting_cost_scen, charger_scen = charger_scen) # alternative formula for infrastructure
      # Generates relevant energy prices and opex for electric truck
      charging_prices_day, charging_prices_night = get_charging_prices(truck.lifetime, delivery_year, day_charging, night_charging, support)
      other_opex_list_el, energy_cost_list_el = get_opex(truck, toll, charging_prices_day, charging_prices_night, amount_day_charge)
      tco, other_opex, energy, ri, capex = get_tco(truck, other_opex_list_el, energy_cost_list_el, discount_rate, refueling_inconvenience_list)
      tco_list.append(tco)
      total_energy_list.append(energy)
      total_other_opex_list.append(other_opex)
      total_capex_list.append(capex)
      total_ri_list.append(ri)
    elif truck.fueltype == "diesel": # Simulation_type = "diesel"
      refueling_inconvenience_list = [0]*truck.lifetime
      energy_prices_diesel = get_diesel_costs(truck.lifetime, delivery_year) # returns a list of diesel prices for the different years
      other_opex_list, energy_cost_list = get_opex(truck,toll,energy_prices_diesel) 
      tco, other_opex, energy, ri, capex = get_tco(truck, other_opex_list, energy_cost_list, discount_rate, refueling_inconvenience_list)
      tco_list.append(tco)
      total_energy_list.append(energy)
      total_other_opex_list.append(other_opex)
      total_capex_list.append(capex)
      total_ri_list.append(0) # for å få til å lage figur
  return tco_list, total_energy_list, total_other_opex_list, total_capex_list, total_ri_list

# Creates a histogram of TCO values
def histogram(mcs,title, x_low, x_high, y_high):
  plt.xlabel("TCO")
  plt.ylabel("Occurences")
  title = "Monte Carlo Simulation: " + title
  plt.title(title)
  plt.hist(mcs, bins = 250)
  plt.ylim(0,y_high)
  plt.xlim(x_low,x_high)
  plt.show()

#fixed values
toll_rate_bet = GLOB_VAR.TOLL_RATE_BET # toll rates
toll_rate_dt = GLOB_VAR.TOLL_RATE_DT
discount_rate = GLOB_VAR.DISCOUNT_RATE 
no_simulations = GLOB_VAR.NO_SIMULATIONS# Number of Monte Carlo simulations

#Initialize trucks objects
bet_price_2023 = get_bet_capital_cost(2023)
# bet_price_2028 = get_bet_capital_cost(2028)
# bet_price_2033 = get_bet_capital_cost(2033)
dt_price_2023 = get_dt_capital_cost(2023)
# dt_price_2028 = get_dt_capital_cost(2028)


el_truck_2023 = Truck(yearly_dist = 80000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
#diesel_truck_2023 = Truck(yearly_dist = 80000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

mcs_el_2023_case1, _, _, _, _ = monte_carlo_simulation(el_truck_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium", waiting_cost_scen = "base", charger_scen="base")
mcs_el_2023_case2, _, _, _, _ = monte_carlo_simulation(el_truck_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium", waiting_cost_scen = "verylow", charger_scen="base")


# mcs_el_2023_case2, _, _, _, _ = monte_carlo_simulation(el_truck_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium", waiting_cost_scen = "verylow", charger_scen="base")
# histogram(mcs_el_2023_case1, "Mixed, 2023 investment - base wait cost", 4000000, 14000000, 1000)
# histogram(mcs_el_2023_case2, "Mixed-haul, 2023 investment - low wait costs", 4000000, 10000000, 1000)

# histogram(mcs_el_2023_case3, "Short-haul, 2023 investment, rapid development", 4000000, 10000000, 1000)


#Simulations for BETs with different delivery years (surcharge NOK 2/ kWh)

#Simulations for DTs with different delivery years
#tco_diesel_2028, _, _, _, _ = monte_carlo_simulation( diesel_truck_2028, no_simulations, toll_rate_dt,  discount_rate, 2028)

#visualize the results
# histogram(mcs_el_2023_case1, "Long-haul, 2023 investment, rapid development", 4000000, 14000000, 1000)
# histogram(mcs_el_2023_case2, "Mixed-haul, 2023 investment, rapid development", 4000000, 10000000, 1000)
# histogram(mcs_el_2023_case3, "Short-haul, 2023 investment, rapid development", 4000000, 10000000, 1000)

# histogram(tco_diesel_2023, "mcs_diesel_2024", 3000000, 7000000, 2000)
#histogram(tco_diesel_2028, "mcs_diesel_2028", 3000000, 7000000, 2000)