# Returns a list of the operational costs for the active years of the truck
def get_opex(truck, toll, energy_prices_day, energy_prices_night = None, amount_day_charge = None):
  ''' Method to get opex for a truck
        Parameters
        ----------
        truck : Truck
          Target truck
        toll: int
          Yearly toll costs in NOK
        energy_prices: list
          Filling/charging prices per year, NOK/kWh for el and NOK/l for diesel. In real NOK
        waiting_cost_list: list
          Waiting cost for charging per year in NOK
  '''
  toll_cost = toll
  opex = []
  energy = []
  maintenance = truck.yearly_dist * truck.maintenance_rate
  other_cost = truck.yearly_dist * truck.other_cost_rate
  
  if truck.fueltype == "diesel":

    for i in range (len(energy_prices_day)):
      energy_costs = truck.consumption_per_km*truck.yearly_dist*energy_prices_day[i]
      opex_yearly = maintenance + toll_cost + other_cost 
      energy.append(energy_costs)
      opex.append(opex_yearly)
  elif truck.fueltype =="el":
    for i in range (len(energy_prices_day)):
      energy_costs_day = truck.consumption_per_km*truck.yearly_dist*energy_prices_day[i] * amount_day_charge
      energy_costs_night = truck.consumption_per_km*truck.yearly_dist*energy_prices_night[i] * (1-amount_day_charge)
      opex_yearly = maintenance + toll_cost + other_cost 
      energy_costs = energy_costs_day + energy_costs_night
      energy.append(energy_costs)
      opex.append(opex_yearly)
    
  return opex, energy


# Returns the total cost of ownership per year 
# Formula from Wu et al
def get_tco(truck, opex_list, energy_cost_list, i, waiting_cost_list):
  ''' Get tco for the truck
        Parameters
        ----------
        truck : Truck
          The truck
        pvf : float
          present value factor
        crf : float
          capital recovery factor
        opex_list: list
          list of opex for each year (nominal values)
        energy_cost_list: lis
          list of energy cost for each year (real 2022 values)
        i: float
          discount rate
  '''
  other_opex = 0
  energy = 0
  waiting_cost = 0
  for n in range (len(opex_list)): 
    other_opex += opex_list[n] / ((1+i)**n) # diskontering 
    energy += energy_cost_list[n] / ((1+i)**n)
    waiting_cost += waiting_cost_list[n] / ((1+i)**n)
  capex = truck.investment_cost - truck.residual_value /((1+i)**truck.lifetime) #diskonterer restverdien
  tco = capex + other_opex + energy + waiting_cost
  return tco, other_opex, energy, waiting_cost, capex 


def get_bet_chassis_cost(year):
    #prices in NOK
    #the results of the exponential fit are saved as a dicationary to avoid high run-time. Prices in NOK
    cost_d = {2023: 2719725.6019056723, 2024: 2567959.1526549193, 2025: 2427683.9030353045, 2026: 2298029.7815019335, 2027: 2178192.5951403026, 2028: 2067429.0415777108, 2029: 1965052.0985744733, 2030: 1870426.762698395, 2031: 1782966.1106512104, 2032: 1702127.6588169544, 2033: 1627409.9984519957, 2034: 1558349.6856461582, 2035: 1494518.3667645946, 2036: 1435520.1215406673, 2037: 1380989.0073401115, 2038: 1330586.7893645158, 2039: 1284000.8427154813, 2040: 1240942.2133068019, 2041: 1201143.825597266, 2042: 1164358.826027372, 2043: 1130359.0518849404, 2044: 1098933.6161026217, 2045: 1069887.5992093452, 2046: 1043040.8403224192, 2047: 1018226.8196812759, 2048: 995291.6257916726, 2049: 974093.0007739472, 2050: 954499.4579940086}
    return cost_d[year]

def get_dt_chassis_cost(year):
    price_prediction = 1450000 #number from truck manufacturer
    return price_prediction

def get_battery_price_in_year(year):
    #price in NOK/kWh
    #results after fitting an exponential function are are saved a a dictionary to avoid high run time
    price_dict = {2010: 10077.96774289395, 2011: 8300.69998124355, 2012: 6879.944797720442, 2013: 5744.187240494891, 2014: 4836.2579619289545, 2015: 4110.455549580527, 2016: 3530.246105731713, 2017: 3066.424281769875, 2018: 2695.643201482352, 2019: 2399.2392756711893, 2020: 2162.2927541061144, 2021: 1972.8767268786037, 2022: 1821.4567729849164, 2023: 1700.4110369257016, 2024: 1603.646575959055, 2025: 1526.2926665112643, 2026: 1464.4556320558202, 2027: 1415.0228515080623, 2028: 1375.5060827269929, 2029: 1343.9162146760177, 2030: 1318.6631437833366, 2031: 1298.475734691228, 2032: 1282.3378365486988, 2033: 1269.4371341717676, 2034: 1259.1242594499006, 2035: 1250.8801048355665, 2036: 1244.2896936128907, 2037: 1239.0212916825756, 2038: 1234.8097094365623, 2039: 1231.4429532077202, 2040: 1228.7515543836373, 2041: 1226.6000390561478, 2042: 1224.8801088239572, 2043: 1223.5051894981189, 2044: 1222.406073314693, 2045: 1221.527435301563, 2046: 1220.8250484476903, 2047: 1220.263557497924, 2048: 1219.814699315384, 2049: 1219.4558802318043, 2050: 1219.1690387755293}
    return price_dict[year]

def get_bet_capital_cost(delivery_year, truck_body_cost = 1000000, charging_equipment = 40000, kwh_bat = 540): 
  '''Get BET capex in the delivery year'''
  battery_cost = get_battery_price_in_year(delivery_year)*kwh_bat
  chassis_excl_battery = get_bet_chassis_cost(delivery_year)
  price = battery_cost + chassis_excl_battery + truck_body_cost + charging_equipment
  return price

def get_dt_capital_cost(delivery_year, truck_body_cost = 1000000):
  chassis_cost = get_dt_chassis_cost(delivery_year)
  price = chassis_cost + truck_body_cost
  return price
