
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint as randint
from statistics import mean
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
toll_rate_dt = GLOB_VAR.TOLL_RATE_DT 
toll_rate_bet = GLOB_VAR.TOLL_RATE_BET
discount_rate = GLOB_VAR.DISCOUNT_RATE
no_simulations = GLOB_VAR.NO_SIMULATIONS # Number of Monte Carlo simulations

font1 = {'family':'serif','color':'black','size':12}

# Parameters to change
#choose with dricing length you want to plot:
driving_length = "mixed_haul" # short_haul, long_haul, mixed_haul

if driving_length == "short_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_SHORT
    yearly_distance = GLOB_VAR.YEARLY_DIST_SHORT
    y_low = 4
    y_high = 8
if driving_length == "mixed_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_MIXED
    yearly_distance = GLOB_VAR.YEARLY_DIST_MIXED
    y_low = 6
    y_high = 10
if driving_length == "long_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_LONG
    yearly_distance = GLOB_VAR.YEARLY_DIST_LONG
    y_low = 7
    y_high = 14.5

# Truck prices 
bet_price_2023 = get_bet_capital_cost(2023)
bet_price_2024 = get_bet_capital_cost(2024)
bet_price_2025 = get_bet_capital_cost(2025)
bet_price_2026 = get_bet_capital_cost(2026)
bet_price_2027 = get_bet_capital_cost(2027)
bet_price_2028 = get_bet_capital_cost(2028)
bet_price_2029 = get_bet_capital_cost(2029)
bet_price_2030 = get_bet_capital_cost(2030)
bet_price_2031 = get_bet_capital_cost(2031)
bet_price_2032 = get_bet_capital_cost(2032)
bet_price_2033 = get_bet_capital_cost(2033)

dt_price_2023 = get_dt_capital_cost(2023)
dt_price_2024 = get_dt_capital_cost(2024)
dt_price_2025 = get_dt_capital_cost(2025)
dt_price_2026 = get_dt_capital_cost(2026)
dt_price_2027 = get_dt_capital_cost(2027)
dt_price_2028 = get_dt_capital_cost(2028)
dt_price_2029 = get_dt_capital_cost(2029)
dt_price_2030 = get_dt_capital_cost(2030)
dt_price_2031 = get_dt_capital_cost(2031)
dt_price_2032 = get_dt_capital_cost(2032)
dt_price_2033 = get_dt_capital_cost(2033)

# BETs - time development
bet_2023 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment = 1)
bet_2024 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2024, residual_rate = 0.2, comparable_DT_value = dt_price_2024, segment = 1)
bet_2025 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2025, residual_rate = 0.2, comparable_DT_value = dt_price_2025, segment = 1)
bet_2026 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2026, residual_rate = 0.2, comparable_DT_value = dt_price_2026, segment = 1)
bet_2027 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2027, residual_rate = 0.2, comparable_DT_value = dt_price_2027, segment = 1)
bet_2028 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment = 1)
bet_2029 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2029, residual_rate = 0.2, comparable_DT_value = dt_price_2029, segment = 1)
bet_2030 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2030, residual_rate = 0.2, comparable_DT_value = dt_price_2030, segment = 1)
bet_2031 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2031, residual_rate = 0.2, comparable_DT_value = dt_price_2031, segment = 1)
bet_2032 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2032, residual_rate = 0.2, comparable_DT_value = dt_price_2032, segment = 1)
bet_2033 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment = 1)

# DTs - time development
dt_2023 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2024 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2024, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2025 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2025, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2026 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2026, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2027 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2027, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2029 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2029, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2030 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2030, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2031 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2031, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2032 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2032, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
# Simulations 

# BETs for different scenarios, by company size

def get_mcs_bet_list(co_size, support, infra_case):
    #infra_case = "medium"
    mcs_bet_2023_s, _ , _, _, _ = monte_carlo_simulation(bet_2023, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2024_s, _ , _, _, _ = monte_carlo_simulation(bet_2024, no_simulations, toll_rate_bet, discount_rate, 2024, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2025_s, _ , _, _, _ = monte_carlo_simulation(bet_2025, no_simulations, toll_rate_bet, discount_rate, 2025, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2026_s, _ , _, _, _ = monte_carlo_simulation(bet_2026, no_simulations, toll_rate_bet, discount_rate, 2026, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2027_s, _ , _, _, _ = monte_carlo_simulation(bet_2027, no_simulations, toll_rate_bet, discount_rate, 2027, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2028_s, _ , _, _, _ = monte_carlo_simulation(bet_2028, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2029_s, _ , _, _, _ = monte_carlo_simulation(bet_2029, no_simulations, toll_rate_bet, discount_rate, 2029, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2030_s, _ , _, _, _ = monte_carlo_simulation(bet_2030, no_simulations, toll_rate_bet, discount_rate, 2030, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2031_s, _ , _, _, _ = monte_carlo_simulation(bet_2031, no_simulations, toll_rate_bet, discount_rate, 2031, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2032_s, _ , _, _, _ = monte_carlo_simulation(bet_2032, no_simulations, toll_rate_bet, discount_rate, 2032, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_bet_2033_s, _ , _, _, _ = monte_carlo_simulation(bet_2033, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = support, amount_day_charge = day_charge_ratio, case = infra_case, length = driving_length, co_size = co_size)
    mcs_list = [mcs_bet_2023_s, mcs_bet_2024_s, mcs_bet_2025_s, mcs_bet_2026_s, mcs_bet_2027_s, mcs_bet_2028_s, mcs_bet_2029_s, mcs_bet_2030_s, mcs_bet_2031_s, mcs_bet_2032_s, mcs_bet_2033_s]
    return mcs_list

def get_mcs_diesel_list():
    mcs_dt_2023, _, _, _, _ = monte_carlo_simulation(dt_2023, no_simulations, toll_rate_dt, discount_rate, 2023)
    mcs_dt_2024, _, _, _, _ = monte_carlo_simulation(dt_2024, no_simulations, toll_rate_dt, discount_rate, 2024)
    mcs_dt_2025, _, _, _, _ = monte_carlo_simulation(dt_2025, no_simulations, toll_rate_dt, discount_rate, 2025)
    mcs_dt_2026, _, _, _, _ = monte_carlo_simulation(dt_2026, no_simulations, toll_rate_dt, discount_rate, 2026)
    mcs_dt_2027, _, _, _, _ = monte_carlo_simulation(dt_2027, no_simulations, toll_rate_dt, discount_rate, 2027)
    mcs_dt_2028, _, _, _, _ = monte_carlo_simulation(dt_2028, no_simulations, toll_rate_dt, discount_rate, 2028)
    mcs_dt_2029, _, _, _, _ = monte_carlo_simulation(dt_2029, no_simulations, toll_rate_dt, discount_rate, 2029)
    mcs_dt_2030, _, _, _, _ = monte_carlo_simulation(dt_2030, no_simulations, toll_rate_dt, discount_rate, 2030)
    mcs_dt_2031, _, _, _, _ = monte_carlo_simulation(dt_2031, no_simulations, toll_rate_dt, discount_rate, 2031)
    mcs_dt_2032, _, _, _, _ = monte_carlo_simulation(dt_2032, no_simulations, toll_rate_dt, discount_rate, 2032)
    mcs_dt_2033, _, _, _, _ = monte_carlo_simulation(dt_2033, no_simulations, toll_rate_dt, discount_rate, 2033)
    mcs_diesel_list = [mcs_dt_2023, mcs_dt_2024, mcs_dt_2025, mcs_dt_2026, mcs_dt_2027, mcs_dt_2028, mcs_dt_2029, mcs_dt_2030, mcs_dt_2031, mcs_dt_2032, mcs_dt_2033]
    return mcs_diesel_list


def line_chart_confidence(tco):
    scenario_mean = []
    conf_upper = []
    conf_lower = []

    for i in range(2023-2023, 2034-2023):
        scenario_mean.append(np.mean(tco[i])/1000000)
        conf_lower.append(np.percentile(np.array(tco[i]),5)/1000000)
        conf_upper.append(np.percentile(np.array(tco[i]),95)/1000000)
    return scenario_mean, conf_lower, conf_upper

def plot_confidence_intervals(filename):
    '''Plot avg. TCO each year for a driving length and save the plot. Driving lengths are changed at the beginning of the file

        filename : str
           filename for the saved plot'''
    year = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]
    colors = ["darkorange", "mediumblue", "darkgreen", "#696969"]
    rapid_bet = get_mcs_bet_list("medium", "no_support", "rapid")
    base_bet = get_mcs_bet_list("medium", "no_support", "medium")
    slow_bet = get_mcs_bet_list("medium", "no_support", "slow")
    diesel = get_mcs_diesel_list()
    tcos = [slow_bet,  base_bet, rapid_bet, diesel]
    labels = ["BET: Slow scenario", "BET: Base scenario", "BET: Rapid scenario", "DT: All scenarios"]

    matplotlib.rcParams['savefig.dpi'] = 360
    matplotlib.rcParams["figure.dpi"] = 360
    
    fig = plt.figure(
    figsize = [7,4], constrained_layout=True)
    ax = fig.add_subplot()
    
    scenario_mean_slow, conf_lower_slow, conf_upper_slow = line_chart_confidence(tcos[0])
    scenario_mean_base, conf_lower_base, conf_upper_base = line_chart_confidence(tcos[1])
    scenario_mean_rapid, conf_lower_rapid, conf_upper_rapid = line_chart_confidence(tcos[2])
    scenario_mean_diesel, conf_lower_diesel, conf_upper_diesel = line_chart_confidence(tcos[3])
    ax.plot(year, scenario_mean_diesel, label = labels[3], color=colors[3])
    ax.fill_between(year, conf_lower_diesel, conf_upper_diesel, color=colors[3], alpha=.2)
    ax.plot(year, scenario_mean_slow, label = labels[0], color=colors[0])
    ax.fill_between(year, conf_lower_slow, conf_upper_slow, color=colors[0], alpha=.1)
    ax.plot(year, scenario_mean_base, label = labels[1], color=colors[1])
    ax.fill_between(year, conf_lower_base, conf_upper_base, color=colors[1], alpha=.1)
    ax.plot(year, scenario_mean_rapid, label = labels[2], color=colors[2])
    ax.fill_between(year, conf_lower_rapid, conf_upper_rapid, color=colors[2], alpha=.1)

    plt.legend(frameon = False, loc = "upper right")
    plt.xlabel("Year", fontdict=font1)
    plt.ylabel("Average TCO (MNOK)", fontdict=font1)
    plt.xlim(2023,2033)
    plt.ylim(y_low,y_high)
    #plt.savefig(fname = filename)
    plt.show()     

filename = driving_length + "_infra"
plot_confidence_intervals(filename)



