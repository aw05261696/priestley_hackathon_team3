import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


def alldata():
    
    temperature = []
    moisture = []
    water_usage = []
    ph = []

    temp_min = []
    temp_max = []
    moist_min = []
    moist_max = []
    ph_min = []
    ph_max = []
    
    df = pd.read_csv('hackathon_mock_data.csv')

    df.dropna()
    
    df1 = df.loc[:, "01/01/2024":"31/01/2024"]
    df2 = df.loc[:, "Date"]

    date = df1.iloc[0].index.values.tolist()

    temperature = df1.iloc[0].tolist()
    moisture = df1.iloc[1].tolist()
    water_usage = df1.iloc[2].tolist()
    ph = df1.iloc[3].tolist()

    for day in date:
        temp_min.append(21)
        temp_max.append(28)
        moist_min.append(21)
        moist_max.append(40)
        ph_min.append(6.2)
        ph_max.append(6.8)
        
    figure, axis = plt.subplots(2, 2) 

    # Temperature
    axis[0, 0].plot(date, temperature, label = "Temperature")
    axis[0, 0].plot(date, temp_min, label = "minimum")
    axis[0, 0].plot(date, temp_max, label = "maximum")
    axis[0, 0].legend(loc='upper left')
    axis[0, 0].set_title("Temperature") 
  
    # Moisture%
    axis[0, 1].plot(date, moisture)
    axis[0, 1].plot(date, moist_min, label = "minimum")
    axis[0, 1].plot(date, moist_max, label = "maximum")
    axis[0, 1].set_title("Moisture")

    # soil pH 
    axis[1, 0].plot(date, ph)
    axis[1, 0].plot(date, ph_min, label = "minimum")
    axis[1, 0].plot(date, ph_max, label = "maximum")
    axis[1, 0].set_title("Soil pH") 
  
    # Water used
    axis[1, 1].plot(date, water_usage) 
    axis[1, 1].set_title("Water usage") 

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
  
    # Combine all the operations and display 
    plt.show() 
