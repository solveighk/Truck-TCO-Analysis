#imports

from random import betavariate
from random import randint as randint
from truck import Truck
import numpy as np


def pert(a, b, c):
  '''Function that generates random number from the PERT-distribution'''
  r = c - a
  alpha = 1 + 4 * (b - a) / r
  beta = 1 + 4 * (c - b) / r
  return a + betavariate(alpha, beta) * r


def get_electricity_parameters():
  ''' Returns electricity prices in NOK/kWh
      Sources: 
      Statnett kortsiktig: https://www.statnett.no/for-aktorer-i-kraftbransjen/planer-og-analyser/kortsiktig-markedsanalyse/
      Statnett lansiktig: https://www.statnett.no/for-aktorer-i-kraftbransjen/planer-og-analyser/langsiktig-markedsanalyse/
  '''
  # Sources el_price: 2023 - 2027 STATNETT kortiktig, 2027 - 2050 STATNETT langsiktig
  el_prices = {
              2023: [0.31, 0.95, 2.55], 2024: [0.20, 0.67, 2.05], 2025: [0.14, 0.52, 1.64], 2026: [0.11, 0.41, 1.30], 2027: [0.14, 0.50, 1.49], #STATNETT KORTSIKTIG
              2028: [0.14, 0.44, 1.18], 2029: [0.14, 0.44, 1.18], 2030: [0.14, 0.44, 1.18], 2031: [0.14, 0.44, 1.18], 2032: [0.14, 0.44, 1.18], #STATNETT langsiktig 2030
              2033: [0.25, 0.52, 0.95], 2034: [0.25, 0.52, 0.95], 2035: [0.25, 0.52, 0.95], 2036: [0.25, 0.52, 0.95], 2037: [0.25, 0.52, 0.95], #STATNETT langsiktig 2035
              2038: [0.19, 0.41, 0.79], 2039: [0.19, 0.41, 0.79], 2040: [0.19, 0.41, 0.79], 2041:[0.19, 0.41, 0.79], 2042:[0.19, 0.41, 0.79], 2043: [0.19, 0.41, 0.79],2045: [0.19, 0.41, 0.79], #STATNETT langsiktig 2040
              2046: [0.18, 0.39, 0.75], 2047: [0.18, 0.39, 0.75], 2048: [0.18, 0.39, 0.75], 2049: [0.18, 0.39, 0.75],  2050: [0.18, 0.39, 0.75] #STATNETT langsiktig 2050
              } 
  return el_prices


def get_charging_surcharge(type = "high_speed", support = "no_support"):
  #support: "no_support", "low_support" or "high_support"
  #type: "high_speed", "low_speed" or "home"
  if type == "low_speed":
    surcharge = {"no_support": 4.65, "low_support": 3.15, "high_support": 1.65}
  elif type == "high_speed":
    surcharge = {"no_support": 6.49, "low_support": 4.99, "high_support": 3.49} 
  else: #type = "home"
    surcharge = {"no_support": 0.00, "low_support": 0.00, "high_support": 0.00}
  other_el_costs = 0.35 #Other el costs parameters - includes transmission, taxes, surcharge 
  for key in surcharge.keys():
    surcharge[key] += other_el_costs
  return surcharge[support]


def get_charging_prices(truck_lifetime, truck_delivery_year=2024, day_charging = "high_speed", night_charging = "home", support = "no_support"):
  ''' Return charging prices for a year in NOK/kWh
        Parameters
        ----------
        truck : Truck
          A battery electric truck
        start_year: int
          year truck is ordered
        truck_delivery_year: int
          Year truck is delivered
        el_surcharge: int
          Extra cost for charging in NOK/kWh that is paid to owner of the charging station
  '''
  el_prices = get_electricity_parameters()
  el_surcharge_day = get_charging_surcharge(day_charging, support) 
  el_surcharge_night = get_charging_surcharge(night_charging, support)

  prices_d = {}
  charging_prices = [0]*truck_lifetime
  for i in range (2023, truck_delivery_year+1):
    # Get energy prices from now until the truck is expected
    prices_d[i] = pert(el_prices[i][0], el_prices[i][1], el_prices[i][2])

  # Gets charging prices for the active years of the truck
  for j in range(truck_delivery_year, truck_lifetime + truck_delivery_year):
    if j == truck_delivery_year:
      start_price = prices_d[j]
      charging_prices[j-truck_delivery_year] = start_price
    else: 
      price  = pert(el_prices[j][0], el_prices[j][1], el_prices[j][2])
      charging_prices[j-truck_delivery_year] = price
  # Adds surcharge costs to the charging cost
  charging_prices_day = charging_prices.copy()
  charging_prices_night = charging_prices.copy()
  
  for j in range(truck_delivery_year, truck_lifetime + truck_delivery_year):
    #charging_prices[j-truck_delivery_year] += el_surcharge
    charging_prices_day[j-truck_delivery_year] += el_surcharge_day
    charging_prices_night[j-truck_delivery_year] += el_surcharge_night

  return charging_prices_day, charging_prices_night


def get_diesel_returns(delivery_year):
  '''Returns a list of the international diesel returns
  '''
  # eia.gov forecast for crude oil, in dollars per barrel
  crude_oil_forecast = {2023: [43, 92, 169], 2024: [44, 93, 169], 2025:[44, 87, 172], 2026: [45, 88, 172], 2027: [45, 88, 172], 2028: [45, 89, 175], 2029: [46, 89, 176], 2030: [46, 90, 178], 2031: [47, 91, 180], 2032: [47, 92, 179], 2033: [48, 92, 181], 2034: [48, 93, 184], 2035: [48, 94, 184], 2036: [49, 94, 184], 2037: [49, 95, 187], 2038: [50, 95, 183], 2039: [50, 96, 183], 2040: [49, 96, 183], 2041: [49, 97, 185], 2042: [49, 96, 186], 2043: [49, 98, 186], 2044: [50, 98, 187], 2045: [50, 99, 187]}  

  # constants to convert to NOK/L
  dollar_to_nok = 10
  barrel_to_liter = 158.987294928

  # constants to get international diesel price
  jan_crude_oil_2023 = (82.50 * dollar_to_nok) / barrel_to_liter # avg crude oil pris september 2022 in NOK/liter
  refinery = (jan_crude_oil_2023 / 0.40) * 0.28# Refing and crude oil represent 28 and 40% of the oil price January 2023

  international_diesel_forecast = {2023: [0,0,0], 2024: [0,0,0], 2025: [0,0,0], 2026: [0,0,0], 2027: [0,0,0], 2028: [0,0,0], 2029: [0,0,0], 2030: [0,0,0], 2031: [0,0,0], 2032: [0,0,0], 2033: [0,0,0], 2034: [0,0,0], 2035: [0,0,0], 2036: [0,0,0], 2037: [0,0,0], 2038: [0,0,0], 2039: [0,0,0], 2040: [0,0,0],  2041: [0,0,0],  2042: [0,0,0],  2043: [0,0,0],  2044: [0,0,0],  2045: [0,0,0]}

  for year in crude_oil_forecast.keys():
    for i in range(3):
      # Get forecast in NOK/liter
      crude_oil_forecast[year][i] = crude_oil_forecast[year][i]*dollar_to_nok / barrel_to_liter
      # get international diesel price by adding crude oil and refinery costs
      international_diesel_forecast[year][i] = crude_oil_forecast[year][i] + refinery 

  # Diesel price returns based on international diesel price
  international_diesel_ret = {}
  max_year = max(list(international_diesel_forecast.keys()))
  for key in range(delivery_year, max_year+1):
    if key == delivery_year:
      international_diesel_ret[key] = international_diesel_forecast[key]
    else:
      international_diesel_ret[key] = [0,0,0]
      international_diesel_ret[key][1] = international_diesel_forecast[key][1] / international_diesel_forecast[key-1][1]
      international_diesel_ret[key][0] = international_diesel_forecast[key][0] / international_diesel_forecast[key-1][1]
      international_diesel_ret[key][2] = international_diesel_forecast[key][2] / international_diesel_forecast[key-1][1]

  return international_diesel_forecast, international_diesel_ret

def get_diesel_costs(truck_lifetime, delivery_year=2024):
  ''' Get diesel costs for lifetime of the truck
      Parameters
      ----------
      truck_lifetime : int
        Lifetime/ operation time of truck in years
      delivery_year
        Year truck arrives/ starts operating 

  '''
  international_diesel_forecast, international_diesel_ret = get_diesel_returns(delivery_year)
  veibruksavgift = 3.52
  diesel_cost_list = [0]*truck_lifetime # Initializes empty list for dieselcost
  d_price = {}
  
  d_price[delivery_year] = international_diesel_ret[delivery_year][1]
  # Starts collecting relevant diesel prices from delivery year and onwards 
  for j in range(delivery_year, truck_lifetime + delivery_year):
    if j == delivery_year:
      start_price = d_price[j]
      diesel_cost_list[j-delivery_year] = start_price
    else: 
      dist_parameter = pert(international_diesel_ret[j][0], international_diesel_ret[j][1], international_diesel_ret[j][2])
      price  = diesel_cost_list[j-delivery_year-1] * dist_parameter
      diesel_cost_list[j-delivery_year] = price
      if price > international_diesel_forecast[j][2]:
        price = international_diesel_forecast[j][2]
      elif price < international_diesel_forecast[j][0]:
        price = international_diesel_forecast[j][0]

  co2_avgift_dict = {2021: 1.58, 2022: 2.05, 2023: 2.53, 2024: 2.40, 2025: 2.76, 2026: 3.18, 2027: 3.65, 2028: 4.20, 2029: 4.83, 2030: 5.56, 2031: 5.56, 2032: 5.56, 2033: 5.56, 2034: 5.56, 2035: 5.56, 2036: 5.56, 2037: 5.56, 2038: 5.56, 2039: 5.56, 2040: 5.56, 2041: 5.56, 2042: 5.56, 2043: 5.56, 2044: 5.56, 2045: 5.56} 
  # Adds additional taxes to get the Norwegian diesel price 
  for k in range(delivery_year, truck_lifetime + delivery_year):
    pumpepris = (diesel_cost_list[k-delivery_year] + veibruksavgift + co2_avgift_dict[k])/0.9 
    diesel_cost_list[k-delivery_year] = pumpepris #*0.75 # deducting VAT

  return diesel_cost_list
