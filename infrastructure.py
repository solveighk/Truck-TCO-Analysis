operation_days = 230
battery_size = 540 #kWh

#SA-parameters
stage_1 = {"short_haul": {"small": 3, "medium": 3,"large": 3}, 
            "long_haul": {"small": 5, "medium": 5,"large": 5}, 
            "mixed_haul": {"small": 5, "medium": 4,"large": 3}}
stage_2 = {"short_haul": {"small": 2, "medium": 2,"large": 2}, 
           "long_haul": {"small": 3, "medium": 3,"large": 3}, 
           "mixed_haul": {"small": 3, "medium": 2.5,"large": 2}}
stage_3 = {"short_haul": {"small": 1, "medium": 1,"large": 1}, 
           "long_haul": {"small": 1, "medium": 1,"large": 1}, 
           "mixed_haul": {"small": 1, "medium": 1,"large": 1}}

# Extended version of refueling_inconvenience. Formula inspired by Lajevardi et. al (2022): case of British Columbia
def RI(lifetime, start_year, case= "slow", length= "short_haul", co_size = "large", waiting_cost = "base", charger_scen = "base"):
    
    #SA-parameters for different stages
    sa_dict = {"stage 1": {"short_haul": {"small": 3, "medium": 3,"large": 3}, 
                "long_haul": {"small": 5, "medium": 5,"large": 5}, 
                "mixed_haul": {"small": 5, "medium": 4,"large": 3}},
   "stage 2": {"short_haul": {"small": 2, "medium": 2,"large": 2}, 
            "long_haul": {"small": 3, "medium": 3,"large": 3}, 
            "mixed_haul": {"small": 3, "medium": 2.5,"large": 2}},
    "stage 3": {"short_haul": {"small": 1, "medium": 1,"large": 1}, 
            "long_haul": {"small": 1, "medium": 1,"large": 1}, 
            "mixed_haul": {"small": 1, "medium": 1,"large": 1}}
    }
    
    #stages for different development speeds
    slow_development = {2023: "stage 1", 2024: "stage 1", 2025: "stage 1", 2026: "stage 1", 2027: "stage 1", 2028: "stage 2", 2029: "stage 2", 2030: "stage 2", 2031: "stage 2", 2032: "stage 2", 2033: "stage 2", 2034: "stage 2", 2035: "stage 2", 2036: "stage 2",  2037: "stage 2", 2038: "stage 3",  2039: "stage 3", 2040: "stage 3", 2041: "stage 3", 2042: "stage 3", 2043: "stage 3", 2044: "stage 3", 2045: "stage 3"}
    medium_development = {2023: "stage 1", 2024: "stage 1", 2025: "stage 1", 2026: "stage 1", 2027: "stage 2", 2028: "stage 2", 2029: "stage 2", 2030: "stage 2", 2031: "stage 2", 2032: "stage 2", 2033: "stage 3", 2034: "stage 3", 2035: "stage 3", 2036: "stage 3",  2037: "stage 3", 2038: "stage 3",  2039: "stage 3", 2040: "stage 3", 2041: "stage 3", 2042: "stage 3", 2043: "stage 3", 2044: "stage 3", 2045: "stage 3"}
    rapid_development = {2023: "stage 1", 2024: "stage 1", 2025: "stage 1", 2026: "stage 2", 2027: "stage 2", 2028: "stage 3", 2029: "stage 3", 2030: "stage 3", 2031: "stage 3", 2032: "stage 3", 2033: "stage 3", 2034: "stage 3", 2035: "stage 3", 2036: "stage 3", 2037: "stage 3", 2038: "stage 3",  2039: "stage 3", 2040: "stage 3", 2041: "stage 3", 2042: "stage 3", 2043: "stage 3", 2044: "stage 3", 2045: "stage 3"}
    perfect_development =  {2023: "stage 3", 2024: "stage 3", 2025: "stage 3", 2026: "stage 3", 2027: "stage 3", 2028: "stage 3", 2029: "stage 3", 2030: "stage 3", 2031: "stage 3", 2032: "stage 3", 2033: "stage 3", 2034: "stage 3", 2035: "stage 3", 2036: "stage 3", 2037: "stage 3", 2038: "stage 3",  2039: "stage 3", 2040: "stage 3", 2041: "stage 3", 2042: "stage 3", 2043: "stage 3", 2044: "stage 3", 2045: "stage 3"}
  
    

    station_availability = {}
    if case == "slow":
        stage_dict = slow_development
    elif case =="medium":
        stage_dict = medium_development
    elif case == "rapid":
        stage_dict = rapid_development
    elif case =="perfect":
        stage_dict = perfect_development

    if case =="slow" or  case =="medium" or  case == "rapid" or case =="perfect":
        for year in stage_dict.keys():
            stage = stage_dict[year]
            station_availability_no = sa_dict[stage][length][co_size]
            station_availability[year] = station_availability_no 

    # Lagt til for sensitivitetsanalyse på SA
    elif case =="SA5":
        station_availability = {2023: 5, 2024: 5, 2025: 5, 2026: 5, 2027: 5, 2028: 5, 2029: 5, 2030: 5, 2031: 5, 2032: 5, 2033: 5, 2034: 5, 2035: 5, 2036: 5,  2037:5, 2038: 5,  2039: 5, 2040: 5}
    elif case =="SA3":
        station_availability = {2023: 3, 2024: 3, 2025: 3, 2026: 3, 2027: 3, 2028: 3, 2029: 3, 2030: 3, 2031: 3, 2032: 3, 2033: 3, 2034: 3, 2035: 3, 2036: 3,  2037:3, 2038: 3,  2039: 3, 2040: 3}
    elif case =="SA2":
        station_availability = {2023: 2, 2024: 2, 2025: 2, 2026: 2, 2027: 2, 2028: 2, 2029: 2, 2030: 2, 2031: 2, 2032: 2, 2033: 2, 2034: 2, 2035: 2, 2036: 2,  2037:2, 2038: 2,  2039: 2, 2040: 2}
    elif case =="SA4":
        station_availability = {2023: 4, 2024: 4, 2025: 4, 2026: 4, 2027: 4, 2028: 4, 2029: 4, 2030: 4, 2031: 4, 2032: 4, 2033: 4, 2034: 4, 2035: 4, 2036: 4,  2037:4, 2038: 4,  2039: 4, 2040: 4}        

    # Se excelark for beregninger

    if charger_scen=="base":
        if length == "short_haul": #driving distance 60000 km
            refueling_time = 0.3 
        elif length == "mixed_haul": #driving distance 80000 km
            refueling_time = 0.8
        elif length == "long_haul": #driving distance 100000 km
            refueling_time = 1.4
    if charger_scen=="150kw":
        if length == "short_haul": #driving distance 60000 km
            refueling_time = 0.42 
        elif length == "mixed_haul": #driving distance 80000 km
            refueling_time = 1.41
        elif length == "long_haul": #driving distance 100000 km
            refueling_time = 2.39
    if charger_scen=="350kw":
        if length == "short_haul": #driving distance 60000 km
            refueling_time = 0.18 
        elif length == "mixed_haul": #driving distance 80000 km
            refueling_time = 0.6
        elif length == "long_haul": #driving distance 100000 km
            refueling_time = 1.03
    if charger_scen=="450kw":
        if length == "short_haul": #driving distance 60000 km
            refueling_time = 0.14 
        elif length == "mixed_haul": #driving distance 80000 km
            refueling_time = 0.47
        elif length == "long_haul": #driving distance 100000 km
            refueling_time = 0.8
    if charger_scen=="550kw":
        if length == "short_haul": #driving distance 60000 km
            refueling_time = 0.12 
        elif length == "mixed_haul": #driving distance 80000 km
            refueling_time = 0.38
        elif length == "long_haul": #driving distance 100000 km
            refueling_time = 0.65


    if waiting_cost == "base":
        hourly_waiting_cost = 750
    elif waiting_cost == "low":
        hourly_waiting_cost = 500
    elif waiting_cost == "high":
        hourly_waiting_cost = 1000
    elif waiting_cost == "verylow":
        hourly_waiting_cost = 250
    

    if length == "short_haul": #driving distance 60000 km
        refueling_time = 0.3 
    elif length == "mixed_haul": #driving distance 80000 km
        refueling_time = 0.8
    elif length == "long_haul": #driving distance 100000 km
        refueling_time = 1.4

    break_time = 0.75
    refueling_inconvenience_list = []
    for year in range(start_year, start_year + lifetime):
        ri_yearly = hourly_waiting_cost * (refueling_time * station_availability[year] - break_time) * operation_days
        if ri_yearly <0.0: 
            ri_yearly = 0
        refueling_inconvenience_list.append(ri_yearly)  
    
    return refueling_inconvenience_list
