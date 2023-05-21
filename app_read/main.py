#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:26:39 2023

@author: fredy
"""
import util_p
import read_csv 
import chart

def run():
    data = read_csv.read_csv('data.csv') 
    country = input('digita pais ->')
    result = util_p.population_by_country(data, country)
     
    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = util_p.get_population(country)
        chart.generate_bar_chart(country['Country/Territory'],labels, values)

    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    chart.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()