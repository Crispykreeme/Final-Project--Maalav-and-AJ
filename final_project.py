import data
from dataclasses import dataclass

def total_consumption(counties: list[dict])-> float:
    total = 0
    for county in counties:
        total += county["res_consumption_mwh"] + county["commercial_consumption_mwh"] + county["ind_consumption_mwh"]
    return total

print(total_consumption(data.counties))

def county_consumption(counties: list[dict], county_name: str)-> float:
    total = 0
    for electric in counties:
       if electric["county_name"].lower() == county_name.lower():
           total += electric["res_consumption_mwh"] + electric["commercial_consumption_mwh"] + electric["ind_consumption_mwh"]
    return total

print(county_consumption(data.counties,"Los Angeles County"))