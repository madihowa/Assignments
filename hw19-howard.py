"""
Madison Howard
Create  plots of all data vs time as well as the avg vs time
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
from datetime import datetime

#Problem 1
#This data is from data I took using a phone's app to create a foucault pendulum. Because I took the data myself, I don't have a URL.

df = pd.read_csv('try.csv',skiprows=1)

df['Date'] = pd.to_datetime(df['Date'])

#print(df.info())
#exit(0)
for column in  df.columns:
    if column != 'Date':
        if column != "Heart Rate":
            mean_name = "Avg_{}".format(column)
            rolling_name = "Rolling_avg_{}".format(column)
            df[mean_name] = df[column].mean()
            df[rolling_name] = df[column].rolling(window=500).mean()
            #print(name) #new column names print
            #I plotted each column against time and adjusted the figure and font size for aesthetic reasons :) 
            plt.figure(figsize=(12, 9))
            #plt.plot(df["Date"].values, df[column].values)#ordered as x, y
            df[column].plot()
            df[mean_name].plot()
            df[rolling_name].plot()
            plt.title('{} vs Time'.format(column), fontsize=20)
            plt.xlabel('Time', fontsize=14)
            plt.ylabel(column, fontsize=14)
            plt.legend()
            plt.show()

print("The data from a foucault pendulum should show some sort of oscillatory tendencies. Generally these type of data sets would be more usefully analyzed with a Fourier Transform. The average doesn't provide much useful information other than what the lowest point of the pendulum would be. The rolling average is able to provide slightly more significant information. For example, at high values for the window on the rolling average, we can see a more general curve on plots with very chaotic/'spikey' motion. This could also be used to get a more readable represenation of the overall curve of the data.")
print("Also, note that when taking the data the phone had a distinct wobble before it settled at a rest point. This is observed in the plots for X, Y, Heading, and Z.")

