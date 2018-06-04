# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:42:00 2018

@author: shahongzhou
"""


def round(wine_num, drink_num, empty_num):
    drink_num += wine_num
    empty_num += wine_num
    new_wine_num = int(empty_num/3)
    empty_num = empty_num%3
    if new_wine_num > 0:
        print(new_wine_num, drink_num, empty_num)
        round(new_wine_num, drink_num, empty_num)

def drink_beer(wine_num):
    drink_num = 0
    empty_num = 0
    round(wine_num, drink_num, empty_num)

drink_beer(354)