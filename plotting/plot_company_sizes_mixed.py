import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint as randint
from statistics import mean
random.seed(488)
np.random.seed(555)
import matplotlib

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

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

# Parameters to change
driving_length = "mixed_haul" # short_haul, long_haul, mixed_haul
if driving_length == "short_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_SHORT
    yearly_distance = GLOB_VAR.YEARLY_DIST_SHORT
    consumption_bet = GLOB_VAR.EL_USE_SHORT
    consumption_dt = GLOB_VAR.DIESEL_USE_SHORT
if driving_length == "mixed_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_MIXED
    yearly_distance = GLOB_VAR.YEARLY_DIST_MIXED
    consumption_bet = GLOB_VAR.EL_USE_MIXED
    consumption_dt = GLOB_VAR.DIESEL_USE_MIXED
if driving_length == "long_haul":
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_LONG
    yearly_distance = GLOB_VAR.YEARLY_DIST_LONG
    day_charge_ratio = GLOB_VAR.DAY_CHARGE_RATIO_LONG
    consumption_bet = GLOB_VAR.EL_USE_LONG
    consumption_dt = GLOB_VAR.DIESEL_USE_LONG

# BETs - time development
bet_2023 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2023, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2023, segment = 1)
bet_2024 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2024, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2024, segment = 1)
bet_2025 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2025, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2025, segment = 1)
bet_2026 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2026, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2026, segment = 1)
bet_2027 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2027, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2027, segment = 1)
bet_2028 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2028, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2028, segment = 1)
bet_2029 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2029, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2029, segment = 1)
bet_2030 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2030, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2030, segment = 1)
bet_2031 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2031, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2031, segment = 1)
bet_2032 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2032, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2032, segment = 1)
bet_2033 = Truck(yearly_dist = yearly_distance, fueltype = "el", consumption_per_km = consumption_bet, lifetime = 7, truck_value = GLOB_VAR.bet_price_2033, residual_rate = 0.2, comparable_DT_value = GLOB_VAR.dt_price_2033, segment = 1)

# DTs - time development
dt_2023 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2024 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2024, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2025 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2025, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2026 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2026, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2027 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2027, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2029 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2029, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2030 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2030, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2031 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2031, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2032 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2032, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033 = Truck(yearly_dist = yearly_distance, fueltype = "diesel", consumption_per_km = consumption_dt, lifetime = 7, truck_value = GLOB_VAR.dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
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

def get_all_scenarios():
    #base scenario:
    base_small = get_mcs_bet_list("small", "no_support", "medium")
    base_medium = get_mcs_bet_list("medium", "no_support", "medium")
    base_large = get_mcs_bet_list("large", "no_support", "medium")

    #slow scenario:
    slow_small = get_mcs_bet_list("small", "no_support", "slow")
    slow_medium = get_mcs_bet_list("medium", "no_support","slow")
    slow_large = get_mcs_bet_list("large", "no_support", "slow")

    #rapid scenario:
    rapid_small = get_mcs_bet_list("small", "no_support", "rapid")
    rapid_medium = get_mcs_bet_list("medium", "no_support", "rapid")
    rapid_large = get_mcs_bet_list("large", "no_support", "rapid")

    small_co = [slow_small, base_small, rapid_small]
    medium_co = [slow_medium, base_medium, rapid_medium]
    large_co = [slow_large, base_large, rapid_large]
    return small_co, medium_co, large_co

def line_chart_by_infra_mixed(infra_case, support, labels, ymin, ymax, filename):
    '''Plot avg. TCO each year for mixed companies of different sized in the gives infra-case. Numbers in MNOK.
    
        Parameters
        ----------
        infra_case : str
            "slow", "medium" or "rapid"
        support : str
            "no_support", "low_support" or "high_support"
        labels : list of strings
            labels for plots, [small company, medium company, large company]
        ymax : float
            Maximum y value of the plot
        ymax : float
            Minimum y value of the plot
        filename : str
           filename for the saved plot'''
    small_co = get_mcs_bet_list("small", support, infra_case)
    medium_co = get_mcs_bet_list("medium", support, infra_case)
    large_co = get_mcs_bet_list("large", support,infra_case)
    diesel_list = get_mcs_diesel_list()
    
    small_co_mean = []
    medium_co_mean = []
    large_co_mean = []
    diesel_mean = []
    
    for year in range(2023 - 2023 , 2034 - 2023):
        small_co_mean.append(np.mean(small_co[year])/1000000)
        medium_co_mean.append(np.mean(medium_co[year])/1000000)
        large_co_mean.append(np.mean(large_co[year])/1000000)
        diesel_mean.append(np.mean(diesel_list[year])/1000000)
        
    years = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033]

    fig, ax = plt.subplots()
    fig.set_figheight(2.7)
    fig.set_figwidth(4.1)
    fig.set_constrained_layout(True)
    matplotlib.rcParams['savefig.dpi'] = 360
    matplotlib.rcParams["figure.dpi"] = 360
    
    if infra_case == "rapid":
        ax.plot(years, small_co_mean, label = labels[0], color = "darkgreen", ls = ':')
        ax.plot(years, medium_co_mean,  label = labels[1], color = "darkgreen", ls = '-')
        ax.plot(years, large_co_mean,  label = labels[2], color = "darkgreen", ls = '-.')
    elif infra_case == "medium":
        ax.plot(years, small_co_mean, label = labels[0], color = "mediumblue", ls = ':')
        ax.plot(years, medium_co_mean,  label = labels[1], color ="mediumblue", ls = '-')
        ax.plot(years, large_co_mean,  label = labels[2], color = "mediumblue", ls = '-.')
    elif infra_case == "slow":
        ax.plot(years, small_co_mean, label = labels[0], color = "darkorange", ls = ':')
        ax.plot(years, medium_co_mean,  label = labels[1], color = "darkorange", ls = '-')
        ax.plot(years, large_co_mean,  label = labels[2], color = "darkorange", ls = '-.')
    ax.plot(years, diesel_mean, label = labels[3], color = "#696969")
    plt.ylim(ymin,ymax)
    plt.xlim(2023,2033)
    plt.legend(fontsize = 8, frameon = False)
    plt.xlabel("Year", fontdict=font1)
    plt.ylabel("Average TCO (MNOK)", fontdict=font1)
    plt.savefig(fname = filename)
    plt.show()

labels = ["BET: Small company", "BET: Medium company", "BET: Large company", "DT: All company sizes"]

line_chart_by_infra_mixed("slow", "no_support", labels, 6, 11, "mixed_infra_slow")
line_chart_by_infra_mixed("medium", "no_support", labels,6, 11, "mixed_infra_base")
line_chart_by_infra_mixed("rapid", "no_support", labels,6, 11, "mixed_infra_rapid")




