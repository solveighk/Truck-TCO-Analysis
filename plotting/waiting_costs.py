import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint as randint
random.seed(488)
np.random.seed(555)

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import matplotlib

#import functions and classes from other files:
from cost_functions import get_bet_capital_cost, get_dt_capital_cost
from truck import Truck
from run_simulations import monte_carlo_simulation
import GLOB_VAR
#fixed values
toll_rate_dt = GLOB_VAR.TOLL_RATE_DT #yearly toll costs
toll_rate_bet = GLOB_VAR.TOLL_RATE_BET
discount_rate = GLOB_VAR.DISCOUNT_RATE
no_simulations = GLOB_VAR.NO_SIMULATIONS # Number of Monte Carlo simulations

#fonts
font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':10}

# Parameters to change
#scenario = "slow" # slow, medium, rapid
size = "medium" # small, large

day_charge_ratio_short = GLOB_VAR.DAY_CHARGE_RATIO_SHORT
day_charge_ratio_mix = GLOB_VAR.DAY_CHARGE_RATIO_MIXED
day_charge_ratio_long = GLOB_VAR.DAY_CHARGE_RATIO_LONG
yearly_dist_short = GLOB_VAR.YEARLY_DIST_SHORT
yearly_dist_mixed = GLOB_VAR.YEARLY_DIST_MIXED
yearly_dist_long = GLOB_VAR.YEARLY_DIST_LONG


# Truck prices 
bet_price_2023 = get_bet_capital_cost(2023)
bet_price_2025 = get_bet_capital_cost(2025)
bet_price_2027 = get_bet_capital_cost(2027)
bet_price_2028 = get_bet_capital_cost(2028)
bet_price_2029 = get_bet_capital_cost(2029)
bet_price_2031 = get_bet_capital_cost(2031)
bet_price_2033 = get_bet_capital_cost(2033)

dt_price_2023 = get_dt_capital_cost(2023)
dt_price_2025 = get_dt_capital_cost(2025)
dt_price_2027 = get_dt_capital_cost(2027)
dt_price_2028 = get_dt_capital_cost(2028)
dt_price_2029 = get_dt_capital_cost(2029)
dt_price_2031 = get_dt_capital_cost(2031)
dt_price_2033 = get_dt_capital_cost(2033)

#truck objects 2023
bet_2023_short = Truck(yearly_dist = yearly_dist_short, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
bet_2023_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
bet_2023_long = Truck(yearly_dist = yearly_dist_long, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
dt_2023_short = Truck(yearly_dist = yearly_dist_short, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2023_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2023_long = Truck(yearly_dist = yearly_dist_long, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

#truck objects 2028
bet_2028_short = Truck(yearly_dist = yearly_dist_short, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
bet_2028_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
bet_2028_long = Truck(yearly_dist = yearly_dist_long, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
dt_2028_short = Truck(yearly_dist = yearly_dist_short, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028_long = Truck(yearly_dist = yearly_dist_long, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

#truck objects 2033

bet_2033_short = Truck(yearly_dist = yearly_dist_short, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
bet_2033_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
bet_2033_long = Truck(yearly_dist = yearly_dist_long, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
dt_2033_short = Truck(yearly_dist = yearly_dist_short, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033_mixed = Truck(yearly_dist = yearly_dist_mixed, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033_long = Truck(yearly_dist = yearly_dist_long, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)


def get_ri_costs(size):
    ''' Plot waiting cost for BETs with in short, base and rapid infrastructure development when investing in 2023, 2028 and 2033.
        
        Parameters
        ----------
        size : str
           size of the company: "small", "medium" or "large"
    '''
    
    year = 2023
    tco_bet_short, _, _, _ , ri_bet_short_23 = monte_carlo_simulation(bet_2023_short, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_short, case = "medium", length = "short_haul", co_size = size)
    tco_bet_mixed, _, _, _ ,  ri_bet_mix_23 = monte_carlo_simulation(bet_2023_mixed, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_mix, case = "medium", length = "mixed_haul", co_size = size)
    tco_bet_long, e_, _, _ ,  ri_bet_long_23 = monte_carlo_simulation(bet_2023_long, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_long, case = "medium", length = "long_haul", co_size = size)
    
    year = 2028
    
    tco_bet_short, _, _, _ , ri_bet_short_28 = monte_carlo_simulation(bet_2028_short, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_short, case = "medium", length = "short_haul", co_size = size)
    tco_bet_mixed, _, _, _ ,  ri_bet_mix_28 = monte_carlo_simulation(bet_2028_mixed, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_mix, case = "medium", length = "mixed_haul", co_size = size)
    tco_bet_long, e_, _, _ ,  ri_bet_long_28 = monte_carlo_simulation(bet_2028_long, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_long, case = "medium", length = "long_haul", co_size = size)
    
    year = 2033
    tco_bet_short, _, _, _ , ri_bet_short_33 = monte_carlo_simulation(bet_2033_short, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_short, case = "medium", length = "short_haul", co_size = size)
    tco_bet_mixed, _, _, _ ,  ri_bet_mix_33 = monte_carlo_simulation(bet_2033_mixed, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_mix, case = "medium", length = "mixed_haul", co_size = size)
    tco_bet_long, e_, _, _ ,  ri_bet_long_33 = monte_carlo_simulation(bet_2033_long, no_simulations, toll_rate_bet, discount_rate, year, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio_long, case = "medium", length = "long_haul", co_size = size)
    
    tco_means = {
    "Short-haul": (np.mean(ri_bet_short_23)/1000000, np.mean(ri_bet_short_28)/1000000, np.mean(ri_bet_short_33)/1000000),
    "Mixed": (np.mean(ri_bet_mix_23)/1000000, np.mean(ri_bet_mix_28)/1000000, np.mean(ri_bet_mix_33)/1000000),
    "Long-haul": (np.mean(ri_bet_long_23)/1000000, np.mean(ri_bet_long_28)/1000000, np.mean(ri_bet_long_33)/1000000)
    }

    colors = {
    "Mixed": ("#fcb653", "#fcb653", "#fcb653"),
    "Short-haul": ("#8c552d","#8c552d","#8c552d"), #e6be8f
    "Long-haul": ("#f5671b", "#f5671b", "#f5671b")
    }
    
    fig, ax = plt.subplots(layout='constrained')
    fig.set_figheight(4)
    fig.set_figwidth(7)
    fig.set_constrained_layout(True)
    matplotlib.rcParams['savefig.dpi'] = 360
    matplotlib.rcParams["figure.dpi"] = 360

    years = ["2023", "2028", "2033"]
    x = np.arange(len(years))  # the label locations
    width = 0.3  # the width of the bars
    multiplier = 0
    
    labels = []
    
    for transport_type, cost in tco_means.items():
        print(transport_type, cost)
        offset = width * multiplier
        rects = ax.bar(x + offset, cost, width, label = transport_type, color = colors[transport_type])
        
        labels = []
        for item in cost:
            if item == 0:
                labels.append("0")
            else: 
                labels.append("~" + str(float(round(item,1))))
        ax.bar_label(rects, labels = labels,  padding = 3)
        multiplier += 1
    
    ax.set_ylabel('RI cost (MNOK)', fontdict = font1)
    ax.set_xticks(x + width, years, fontsize = 12, fontfamily = "serif")
    ax.legend(loc='upper right', ncols=3, frameon = False)
    ax.set_ylim(0, 6)
    plt.savefig(fname = "waiting_costs")
    plt.show()

#Get refueling inconvenience plot/ waiting cost plot for medium sized companies
get_ri_costs("medium")






