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

#import functions and classes from other files:
from cost_functions import get_bet_capital_cost, get_dt_capital_cost
from truck import Truck
from run_simulations import monte_carlo_simulation
import matplotlib
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
driving_length = "mixed_haul" # short_haul, long_haul, mixed_haul
if driving_length == "short_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_SHORT
    yearly_distance = GLOB_VAR.YEARLY_DIST_SHORT 
if driving_length == "mixed_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_MIXED
    yearly_distance = GLOB_VAR.YEARLY_DIST_MIXED
if driving_length == "long_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_LONG
    yearly_distance = GLOB_VAR.YEARLY_DIST_LONG 


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

# BETs 
bet_2023 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment = 1)
bet_2025 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2025, residual_rate = 0.2, comparable_DT_value = dt_price_2025, segment = 1)
bet_2027 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2027, residual_rate = 0.2, comparable_DT_value = dt_price_2027, segment = 1)
bet_2028 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment = 1)
bet_2029 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2029, residual_rate = 0.2, comparable_DT_value = dt_price_2029, segment = 1)
bet_2031 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2031, residual_rate = 0.2, comparable_DT_value = dt_price_2031, segment = 1)
bet_2033 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2031, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment = 1)

# DTs
dt_2023 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2025 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2025, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2027 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2027, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2029 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2029, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2031 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2031, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)


# BETs simulations medium scenario
mcs_bet_2023_m, _ , _, _, _ = monte_carlo_simulation(bet_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2025_m, _ , _, _, _ = monte_carlo_simulation(bet_2025, no_simulations, toll_rate_bet, discount_rate, 2025, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2027_m, _ , _, _, _ = monte_carlo_simulation(bet_2027, no_simulations, toll_rate_bet, discount_rate, 2027, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2028_m, _ , _, _, _ = monte_carlo_simulation(bet_2028, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2029_m, _ , _, _, _ = monte_carlo_simulation(bet_2029, no_simulations, toll_rate_bet, discount_rate, 2029, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2031_m, _ , _, _, _ = monte_carlo_simulation(bet_2031, no_simulations, toll_rate_bet, discount_rate, 2031, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
mcs_bet_2033_m, _ , _, _, _ = monte_carlo_simulation(bet_2033, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)


# DTs simulations
mcs_dt_2023, dieselprice23, _, _, _ = monte_carlo_simulation(dt_2023, no_simulations, toll_rate_dt, discount_rate, 2023)
mcs_dt_2025, dieselprice25 , _, _, _ = monte_carlo_simulation(dt_2025, no_simulations, toll_rate_dt, discount_rate, 2025)
mcs_dt_2027, dieselprice27, _, _, _ = monte_carlo_simulation(dt_2027, no_simulations, toll_rate_dt, discount_rate, 2027)
mcs_dt_2028, dieselprice27, _, _, _ = monte_carlo_simulation(dt_2028, no_simulations, toll_rate_dt, discount_rate, 2028)
mcs_dt_2029, dieselprice29, _, _, _ = monte_carlo_simulation(dt_2029, no_simulations, toll_rate_dt, discount_rate, 2029)
mcs_dt_2031, dieselprice31, _, _, _ = monte_carlo_simulation(dt_2031, no_simulations, toll_rate_dt, discount_rate, 2031)
mcs_dt_2033, dieselprice31, _, _, _ = monte_carlo_simulation(dt_2033, no_simulations, toll_rate_dt, discount_rate, 2033)

def tco_bar_chart_bet(filename = "Cost_split_BET"):
    '''Plot bar chart of cost split of avg. TCO for BET. Numbers in MNOK.
    
        Parameters
        ----------
        filename : str
           filename for the saved plot'''
           
    tco_bet_2033_m, energy_bet_2033, other_opex_bet_2033, capex_bet_2033, ri_bet_2033 = monte_carlo_simulation(bet_2033, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "rapid", length = driving_length, co_size = size)
    tco_bet_2028_m, energy_bet_2028, other_opex_bet_2028, capex_bet_2028, ri_bet_2028 = monte_carlo_simulation(bet_2028, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)
    tco_bet_2023_m, energy_bet_23, other_opex_bet_23, capex_bet_23, ri_bet_23 = monte_carlo_simulation(bet_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = day_charge_ratio, case = "medium", length = driving_length, co_size = size)

    energy_1, otheropex_1, capex_1, ri_1 = energy_bet_23, other_opex_bet_23, capex_bet_23, ri_bet_23
    energy_2, otheropex_2, capex_2, ri_2 = energy_bet_2028, other_opex_bet_2028, capex_bet_2028, ri_bet_2028
    energy_3, otheropex_3, capex_3, ri_3 = energy_bet_2033, other_opex_bet_2033, capex_bet_2033, ri_bet_2033
    labels = ["BET 2023", "BET 2028", "BET 2033"]
    capex_mean = np.array([np.mean(capex_1)/1000000, np.mean(capex_2)/1000000, np.mean(capex_3)/1000000])
    othercosts_mean = np.array([np.mean(otheropex_1)/1000000, np.mean(otheropex_2)/1000000, np.mean(otheropex_3)/1000000])
    energy_mean = np.array([np.mean(energy_1)/1000000, np.mean(energy_2)/1000000, np.mean(energy_3)/1000000])
    ri_mean = np.array([np.mean(ri_1)/1000000, np.mean(ri_2)/1000000, np.mean(ri_3)/1000000])

    capex_std = np.array([np.std(capex_1)/1000000, np.std(capex_2)/1000000, np.std(capex_3)/1000000])
    other_std = np.array([np.std(otheropex_1)/1000000, np.std(otheropex_2)/1000000, np.std(otheropex_3)/1000000])
    energy_std = np.array([np.std(energy_1)/1000000, np.std(energy_2)/1000000, np.std(energy_3)/1000000])
    ri_std = np.array([np.std(ri_1)/1000000, np.std(ri_2)/1000000, np.std(ri_3)/1000000])
    width = 0.8    

    fig, ax = plt.subplots()
    fig.set_figheight(3)
    fig.set_figwidth(4)
    fig.set_constrained_layout(True)
    matplotlib.rcParams['savefig.dpi'] = 360
    matplotlib.rcParams["figure.dpi"] = 360

    ax4 = ax.bar(labels, ri_mean, width, yerr=ri_std, bottom = capex_mean+othercosts_mean+energy_mean, label='Refueling inconvenience costs', color = "#fcb653")
    ax3 = ax.bar(labels, energy_mean, width, yerr=energy_std, bottom = capex_mean+othercosts_mean, label='Energy costs',color =  "#00817c" ) #color =  "#00817c"
    ax2 = ax.bar(labels, othercosts_mean, width, yerr=other_std, bottom = capex_mean, label='Other operational costs', color = "#73a85a") #color = "#73a85a"
    ax1 = ax.bar(labels, capex_mean, width, yerr=capex_std, label='Capital costs',  color = "#295269") #dargreen 
    ax.set_ylabel('Cost (MNOK)', fontdict=font1)


    for r1, r2, r3, r4 in zip(ax1, ax2, ax3, ax4):
        h1 = r1.get_height()
        h2 = r2.get_height()
        h3 = r3.get_height()
        h4 = r4.get_height()
        if not h4 == 0.0:
            plt.text(r4.get_x() + r4.get_width() /2. , h1 + h2 + h3 + h4 / 2., "~"+str(float(round(h4, 1))), ha="center", va="center", color="black", fontsize=9)
        plt.text(r3.get_x() + r3.get_width() / 2., h1 + h2 + h3 / 2., "~"+str(float(round(h3, 1))), ha="center", va="center", color="black", fontsize=9)
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "~"+str(float(round(h2, 1))), ha="center", va="center", color="black", fontsize=9)
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2.,  "~"+str(float(round(h1, 1))), ha="center", va="center", color="white", fontsize=9)
        
        
    ax.legend(fontsize = 9, frameon = False, loc = "upper right")
    plt.ylim(0, 12)
    plt.savefig(fname = filename)
    plt.show()
    
def tco_bar_chart_dt(filename = "Cost_split_DT"):
    '''Plot bar chart of cost split of avg. TCO for DT. Numbers in MNOK.
    
        Parameters
        ----------
        filename : str
            filename for the saved plot
    '''
    tco_diesel_2023_base, energy_dt_23, other_opex_dt_23, capex_dt_23, ri_dt_23 = monte_carlo_simulation(dt_2023, no_simulations, toll_rate_dt, discount_rate, 2023)
    tco_diesel_2028_base, energy_dt_28, other_opex_dt_28, capex_dt_28, ri_dt_28 = monte_carlo_simulation(dt_2028, no_simulations, toll_rate_dt, discount_rate, 2028)
    tco_diesel_2033_base, energy_dt_33, other_opex_dt_33, capex_dt_33, ri_dt_33 = monte_carlo_simulation(dt_2033, no_simulations, toll_rate_dt, discount_rate, 2033)
    
    energy_1, otheropex_1, capex_1 = energy_dt_23, other_opex_dt_23, capex_dt_23
    energy_2, otheropex_2, capex_2 =  energy_dt_28, other_opex_dt_28, capex_dt_28
    energy_3, otheropex_3, capex_3 = energy_dt_33, other_opex_dt_33, capex_dt_33
    
    labels = ["DT 2023", "DT 2028", "DT 2033"]
    capex_mean = np.array([np.mean(capex_1)/1000000, np.mean(capex_2)/1000000, np.mean(capex_3)/1000000])
    othercosts_mean = np.array([np.mean(otheropex_1)/1000000, np.mean(otheropex_2)/1000000, np.mean(otheropex_3)/1000000])
    energy_mean = np.array([np.mean(energy_1)/1000000, np.mean(energy_2)/1000000, np.mean(energy_3)/1000000])
   
    capex_std = np.array([np.std(capex_1)/1000000, np.std(capex_2)/1000000, np.std(capex_3)/1000000])
    other_std = np.array([np.std(otheropex_1)/1000000, np.std(otheropex_2)/1000000, np.std(otheropex_3)/1000000])
    energy_std = np.array([np.std(energy_1)/1000000, np.std(energy_2)/1000000, np.std(energy_3)/1000000])

    width = 0.8   

    fig, ax = plt.subplots()
    fig.set_figheight(3)
    fig.set_figwidth(4)
    fig.set_constrained_layout(True)
    matplotlib.rcParams['savefig.dpi'] = 360
    matplotlib.rcParams["figure.dpi"] = 360
    
    ax3 = ax.bar(labels, energy_mean, width, yerr=energy_std, bottom = capex_mean+othercosts_mean, label='Energy costs',color = "#00817c")
    ax2 = ax.bar(labels, othercosts_mean, width, yerr=other_std, bottom = capex_mean, label='Other operational costs', color = "#73a85a")
    ax1 = ax.bar(labels, capex_mean, width, yerr=capex_std, label='Capital costs',  color = "#295269")
    ax.set_ylabel('Cost (MNOK)', fontdict=font1)

    for r1, r2, r3 in zip(ax1, ax2, ax3):
        h1 = r1.get_height()
        h2 = r2.get_height()
        h3 = r3.get_height()
        plt.text(r3.get_x() + r3.get_width() / 2., h1 + h2 + h3 / 2., "~"+str(float(round(h3, 1))), ha="center", va="center", color="black", fontsize=9)
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "~"+str(float(round(h2, 1))), ha="center", va="center", color="black", fontsize=9)
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2.,  "~"+str(float(round(h1, 1))), ha="center", va="center", color="white", fontsize=9)
        
    ax.legend(fontsize = 9, frameon = False, loc = "upper right")
    plt.ylim(0, 12)
    plt.savefig(fname = filename)
    plt.show()

#plot cost splot for BETs
tco_bar_chart_bet("Cost_split_BET")
#plot cost splot for DTs
tco_bar_chart_dt( "Cost_split_DT")



