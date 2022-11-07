# -*- coding: utf-8 -*-
"""
@author: Harpreet Singh
"""

import numpy as np 
import pandas as pd 
import os  


gen_1 = pd.read_csv("\\Plant_1_Generation_Data.csv")

gen_1.drop('PLANT_ID', 1,inplace = True)

sens_1 = pd.read_csv("\\Plant_1_Weather_Sensor_Data.csv")


sens_1.drop("PLANT_ID",1,inplace = True)

#Lets format the date and time 

gen_1['DATE_TIME'] = pd.to_datetime(gen_1['DATE_TIME'],format = '%d-%m-%Y %H:%M') 
sens_1['DATE_TIME'] = pd.to_datetime(sens_1['DATE_TIME'],format = '%Y-%m-%d %H:%M:%S')


os.makedirs('folder/subfolder', exist_ok=True)  
gen_1.to_csv('folder/subfolder/gen_1.csv')  
sens_1.to_csv('folder/subfolder/sens_1.csv') 