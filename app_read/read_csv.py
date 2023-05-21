#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 07:07:39 2023

@author: fredy
"""
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        # nombre de las columnas
        header = next(reader)
        data =[]
        for row in reader :
            iterable = zip (header, row) # convierte en lista de tuplas 
            #print(list(iterable))
            # transformar el archivo en formato de diccionarios
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
    

# a partir de de un archivo csv convertirlo a un diccionario
# datos reales de https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
if __name__ == '__main__':
    country = read_csv('data.csv')
    print(country)