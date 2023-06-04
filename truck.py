# Initializes a truck
class Truck():
  ''' Class to hold info about the trucks. Can be expanded to include different segments
  '''
  def __init__(self,  yearly_dist, fueltype, consumption_per_km, lifetime, truck_value, residual_rate,  comparable_DT_value = 0, segment = 1, support_scenario ="base"):
    ''' Class to set parameters for a new truck
    
        Parameters
        ----------
        yearly_dist : int
            Yearly driving distance in km
        fueltype : str, "el" or "diesel
            If the truck is battery electric or diesel truck
        consumption_per_km : str
            Consumption in kWh/km for electric trucks, and l/km for diesel trucks
        lifetime : int
            Estimated lifetime of the vehicle in years
        truck_value: int
            Estimated value of the truck in NOK
        residual_rate : float
            Residual value of the truck after it has exeeced its lifetime, as decimal: eg. 40% = 0.4
        comparable_DT_value : int, optional
            Value of comparable truck diesl truck, used to calculate ENOVA support for el trucks (default is 0)
       
    '''
    self.yearly_dist = yearly_dist
    self.fueltype = fueltype
    self.consumption_per_km = consumption_per_km
    self.lifetime = lifetime
    self.truck_value = truck_value
    self.comparable_DT_value = comparable_DT_value
    
    #maintenance rate and other_cost rate in NOK/km
    if fueltype == "el":
      self.maintenance_rate = 1
      self.other_cost_rate = 1
      self.residual_rate = 0.2
    elif fueltype == "diesel":
      self.maintenance_rate = 1.5 
      self.other_cost_rate = 1 
      self.residual_rate = 0.2
    
    if support_scenario == "base":
      if comparable_DT_value <= self.truck_value and comparable_DT_value != 0 and fueltype == "el": 
        enova_support = 0.4 * (self.truck_value-comparable_DT_value)
      else:
        enova_support = 0
    elif support_scenario=="full":
      if comparable_DT_value <= self.truck_value and comparable_DT_value != 0 and fueltype == "el": 
        enova_support = 1.0 * (self.truck_value-comparable_DT_value)
      else:
        enova_support = 0
    elif support_scenario =="higher":
      if comparable_DT_value <= self.truck_value and comparable_DT_value != 0 and fueltype == "el": 
        enova_support = 0.7 * (self.truck_value-comparable_DT_value)
      else:
        enova_support = 0

    self.residual_value = residual_rate*self.truck_value
    self.investment_cost = self.truck_value - enova_support 
    self.name = fueltype + "-truck_Segment:" + str(segment) 

  
  def set_maintenance_rate(self, maintenance_rate):
    '''Change maintenance rate of truck to maintenance_rate (NOK/km)'''
    self.maintenance_rate = maintenance_rate
  
  def set_other_cost_rate(self, other_cost_rate):
    '''Change other cost rate of truck to other_cost_rate (NOK/km)'''
    self.other_cost_rate = other_cost_rate
  
  def set_name(self, name):
    '''Change name of the truck'''
    self.name = name
  
  def get_segment_from_number(segment_no):
    segments = {1: "Agricultural, forestry, and fishing products", 2: "Food products, beverages, tobacco, and animal fodder", 3: "Coal, oil and chemical products", 4: "Metal ores, stone, sand, gravel, clay, salt, cement, lime, and other manufactured construction materials and waste", 5: "Other manufactured goods and grouped goods"}  
    return segments.get(segment_no)
  
  def __str__(self): 
    return self.name

  