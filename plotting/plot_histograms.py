import random
import matplotlib.pyplot as plt
import numpy as np
from random import randint as randint
from statistics import mean, median, stdev
import matplotlib
random.seed(488)
np.random.seed(555)
import matplotlib.ticker as ticker

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from run_simulations import monte_carlo_simulation
from cost_functions import get_bet_capital_cost, get_dt_capital_cost
from truck import Truck
import GLOB_VAR

#fixed values
toll_rate_dt = GLOB_VAR.TOLL_RATE_DT #yearly toll costs
toll_rate_bet = GLOB_VAR.TOLL_RATE_BET
discount_rate = GLOB_VAR.DISCOUNT_RATE
no_simulations = GLOB_VAR.NO_SIMULATIONS # Number of Monte Carlo simulations

#fonts
font1 = {'family':'serif','color':'black','size':10}

size = "medium" # small, large


#truck prices
bet_price_2023 = get_bet_capital_cost(2023)
bet_price_2028 = get_bet_capital_cost(2028)
bet_price_2033 = get_bet_capital_cost(2033)
dt_price_2023 = get_dt_capital_cost(2023)
dt_price_2028 = get_dt_capital_cost(2028)
dt_price_2033 = get_dt_capital_cost(2033)

#truck objects 2023
bet_2023_short = Truck(yearly_dist = 60000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
bet_2023_mixed = Truck(yearly_dist = 80000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
bet_2023_long = Truck(yearly_dist = 100000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2023, residual_rate = 0.2, comparable_DT_value = dt_price_2023, segment=1)
dt_2023_short = Truck(yearly_dist = 60000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2023_mixed = Truck(yearly_dist = 80000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2023_long = Truck(yearly_dist = 100000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2023, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

#truck objects 2028
bet_2028_short = Truck(yearly_dist = 60000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
bet_2028_mixed = Truck(yearly_dist = 80000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
bet_2028_long = Truck(yearly_dist = 100000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2028, residual_rate = 0.2, comparable_DT_value = dt_price_2028, segment=1)
dt_2028_short = Truck(yearly_dist = 60000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028_mixed = Truck(yearly_dist = 80000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2028_long = Truck(yearly_dist = 100000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2028, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

#truck objects 2033

bet_2033_short = Truck(yearly_dist = 60000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
bet_2033_mixed = Truck(yearly_dist = 80000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
bet_2033_long = Truck(yearly_dist = 100000, fueltype = "el", consumption_per_km = 1.7, lifetime = 7, truck_value = bet_price_2033, residual_rate = 0.2, comparable_DT_value = dt_price_2033, segment=1)
dt_2033_short = Truck(yearly_dist = 60000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033_mixed = Truck(yearly_dist = 80000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)
dt_2033_long = Truck(yearly_dist = 100000, fueltype = "diesel", consumption_per_km = 0.4, lifetime = 7, truck_value = dt_price_2033, residual_rate = 0.2, comparable_DT_value=0, segment = 1)

#SHORT-HAUL
tco_el_2023_short, _,_,_,_  = monte_carlo_simulation(bet_2023_short, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.14, case = "medium", length = "short_haul", co_size = "medium")
tco_dt_2023_short,_,_,_,_  = monte_carlo_simulation(dt_2023_short, no_simulations, toll_rate_dt,  discount_rate, 2023)
tco_el_2028_short, _,_,_,_  = monte_carlo_simulation(bet_2028_short, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.14, case = "medium", length = "short_haul", co_size = "medium")
tco_dt_2028_short,_,_,_,_  = monte_carlo_simulation(dt_2028_short, no_simulations, toll_rate_dt,  discount_rate, 2028)
tco_el_2033_short, _,_,_,_  = monte_carlo_simulation(bet_2033_short, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.14, case = "medium", length = "short_haul", co_size = "medium")
tco_dt_2033_short,_,_,_,_  = monte_carlo_simulation(dt_2033_short, no_simulations, toll_rate_dt,  discount_rate, 2033)

#MIXED
tco_el_2023_mixed,  _,_,_,_   = monte_carlo_simulation(bet_2023_mixed, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium")
tco_dt_2023_mixed,_,_,_,_  = monte_carlo_simulation(dt_2023_mixed, no_simulations, toll_rate_dt,  discount_rate, 2023)
tco_el_2028_mixed,  _,_,_,_   = monte_carlo_simulation(bet_2028_mixed, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium")
tco_dt_2028_mixed,_,_,_,_  = monte_carlo_simulation(dt_2028_mixed, no_simulations, toll_rate_dt,  discount_rate, 2028)
tco_el_2033_mixed,  _,_,_,_   = monte_carlo_simulation(bet_2033_mixed, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.36, case = "medium", length = "mixed_haul", co_size = "medium")
tco_dt_2033_mixed,_,_,_,_  = monte_carlo_simulation(dt_2033_mixed, no_simulations, toll_rate_dt,  discount_rate, 2033)

#LONG-HAUL
tco_el_2023_long,  _,_,_,_   = monte_carlo_simulation(bet_2023_long, no_simulations, toll_rate_bet, discount_rate, 2023, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.49, case = "medium", length = "long_haul", co_size = "medium")
tco_dt_2023_long,_,_,_,_  = monte_carlo_simulation(dt_2023_long, no_simulations, toll_rate_dt,  discount_rate, 2023)
tco_el_2028_long,  _,_,_,_   = monte_carlo_simulation(bet_2028_long, no_simulations, toll_rate_bet, discount_rate, 2028, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.49, case = "medium", length = "long_haul", co_size = "medium")
tco_dt_2028_long,_,_,_,_  = monte_carlo_simulation(dt_2028_long, no_simulations, toll_rate_dt,  discount_rate, 2028)
tco_el_2033_long,  _,_,_,_   = monte_carlo_simulation(bet_2033_long, no_simulations, toll_rate_bet, discount_rate, 2033, day_charging = "high_speed", night_charging = "home", support = "no_support", amount_day_charge = 0.49, case = "medium", length = "long_haul", co_size = "medium")
tco_dt_2033_long,_,_,_,_  = monte_carlo_simulation(dt_2033_long, no_simulations, toll_rate_dt,  discount_rate, 2033)


def plot_histogram(bet_list, dt_list, bet_label_list, dt_label_list, x_min, x_max, filename, y_max):
    '''Plot histogram with relative frequencies for TCO simulations of BETs and DTs. Numbers in MNOK.
    
        Parameters
        ----------
        bet_list : list of strings
            2d list with tcos after simulations in three investment years. 
        dt_list : list of strings
            2d list with tcos after simulations in three investment years. 
        bet_label_list : list of strings
            label list for each investment year for BETs
        bet_label_list : list of strings
            label list for each investment year for DTs
        x_min : float
            Minimum x value of the plot
        x_max : float
            Maximum x value of the plot
        filename : str
           filename for the saved plot
        y_max : float
            Maximum y value of the plot
    '''
    
    font1 = {'family':'serif','color':'black','size':10}
    matplotlib.rcParams['savefig.dpi'] = 360
    bet_colors =["teal", "darkorange", "darkred"]
    dt_colors  = ["teal", "darkorange", "darkred"]

    fig = plt.figure(
    figsize = [7,4], constrained_layout=False)
    plt.subplots_adjust(left=0.2, right=0.95, bottom=0.15, top=0.95)
    bins = np.linspace(4, 15, 1200)
    ax = fig.add_subplot()
    for i in range(len(bet_list)):
        bet = np.array(bet_list[i])
        bet /= 1000000
        bet = bet.tolist()
        bet_list[i] = bet
        dt = np.array(dt_list[i])
        dt /= 1000000
        dt = dt.tolist()
        dt_list[i] = dt
    
    ax.hist(bet_list[2], alpha=0.9, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = bet_colors[2], label = bet_label_list[2], weights=[np.ones_like(np.array(bet_list[2])) / len(np.array(bet_list[2]))])
    ax.hist(bet_list[1], alpha=1, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = bet_colors[1], label = bet_label_list[1], weights=[np.ones_like(np.array(bet_list[1])) / len(np.array(bet_list[1]))])
    ax.hist(bet_list[0], alpha=1, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = bet_colors[0], label = bet_label_list[0], weights=[np.ones_like(np.array(bet_list[0])) / len(np.array(bet_list[0]))])
    
    ax.hist(dt_list[2], alpha=0.6, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = dt_colors[2], label = dt_label_list[2], weights=[np.ones_like(np.array(dt_list[2])) / len(np.array(dt_list[2]))])
    ax.hist(dt_list[1], alpha=0.7, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = dt_colors[1], label = dt_label_list[1], weights=[np.ones_like(np.array(dt_list[1])) / len(np.array(dt_list[1]))])
    ax.hist(dt_list[0], alpha=0.6, bins=bins, histtype='stepfilled', rwidth=1, lw = 1, color = dt_colors[0], label = dt_label_list[0], weights=[np.ones_like(np.array(dt_list[0])) / len(np.array(dt_list[0]))])
    
    
    plt.ylim(0,y_max)
    ax.set_ylabel('Relative frequency', fontdict=font1, labelpad = 0.04)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        
    plt.legend(loc="upper right", fontsize=10, frameon = False, ncol=2)
    ax.set_xlabel('TCO (MNOK)', fontdict=font1)
    fig.set_dpi(360)
    plt.xlim(x_min,x_max)
    #plt.savefig(fname = filename)
    plt.show()


#color_list = ["#00817c","orange","darkred"] 

#all BET in one chart
#Plot historgram short-haul, medium company, base (medium) infrastructure development
plot_histogram( [tco_el_2033_long, tco_el_2028_long, tco_el_2023_long],[tco_dt_2033_long, tco_dt_2028_long, tco_dt_2023_long],["BET 2033", "BET 2028", "BET 2023"], ["DT 2033", "DT 2028", "DT 2023"], 7.5, 14.5,filename="hist_long_haul", y_max = 0.08)
#Plot historgram mixed, medium company, base (medium) infrastructure development
plot_histogram( [tco_el_2033_mixed, tco_el_2028_mixed, tco_el_2023_mixed],[tco_dt_2033_mixed, tco_dt_2028_mixed, tco_dt_2023_mixed],["BET 2033", "BET 2028", "BET 2023"], ["DT 2033", "DT 2028", "DT 2023"], 5.5, 10,filename="hist_mixed", y_max = 0.10)
#Plot historgram long-haul, medium company, base (medium) infrastructure development
plot_histogram( [tco_el_2033_short, tco_el_2028_short, tco_el_2023_short],[tco_dt_2033_short, tco_dt_2028_short, tco_dt_2023_short],["BET 2033", "BET 2028", "BET 2023"], ["DT 2033", "DT 2028", "DT 2023"], 4, 8,filename="hist_short_haul", y_max = 0.12)


def get_properties(tco, name = ""):
    '''Get descriptive statistics of the distributions.
    '''
    #plot_histogram(tco, type)
    mean1 = round(mean(tco)/1000000, 2)
    median1 =round((median(tco)/1000000), 2)
    variance1 = round(stdev(tco)/1000000,2)
    min_value = round(min(tco)/1000000,2)
    max_value = round(max(tco)/1000000,2)
    print("Stats for " + name)
    print("Mean:", float(mean1))
    print("Median:", float(median1))
    print("Max value:", float(max_value))
    print("Min", float(min_value))
    print("Standard deviation:", float(variance1))
    print("----- END -----")

#GET statistics
#stats short-haul

#get_properties(tco_el_2023_short, name = "BET SHORT 2023")
#get_properties(tco_el_2028_short, name = "BET SHORT 2028")
# get_properties(tco_el_2033_short, name = "BET SHORT 2033")
# get_properties(tco_dt_2023_short, name = "DT SHORT 2023")
# get_properties(tco_dt_2028_short, name = "DT SHORT 2028")
# get_properties(tco_dt_2033_short, name = "DT SHORT 2033")

#stats mixed
# get_properties(tco_el_2023_mixed, name = "BET MIXED 2023")
# get_properties(tco_el_2028_mixed, name = "BET MIXED 2028")
# get_properties(tco_el_2033_mixed, name = "BET MIXED 2033")
# get_properties(tco_dt_2023_mixed, name = "DT MIXED 2023")
# get_properties(tco_dt_2028_mixed, name = "DT MIXED 2028")
# get_properties(tco_dt_2033_mixed, name = "DT MIXED 2033")

#stats long
# get_properties(tco_el_2023_long, name = "BET LONG 2023")
# get_properties(tco_el_2028_long, name = "BET LONG 2028")
# get_properties(tco_el_2033_long, name = "BET LONG 2033")
# get_properties(tco_dt_2023_long, name = "DT LONG 2023")
# get_properties(tco_dt_2028_long, name = "DT LONG 2028")
# get_properties(tco_dt_2033_long, name = "DT LONG 2033")


