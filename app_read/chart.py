#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:08:56 2023

@author: fredy
"""

import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/chart{name}_bar.png')
    plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels =labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/chart_pie.png')
    plt.close()

        

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [20,25,80]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)