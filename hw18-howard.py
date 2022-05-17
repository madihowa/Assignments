import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Load the csv file into a Pandas DataFrame.
df = pd.read_csv('lubbock-mean-temps.csv', index_col=0)
#This will print some information about the DataFrame:
#print(df.describe())
#This will print the first 5 rows:
#print(df.head(5))

#Problem 1
#Create a new column named Summer which contains the average temperature of the months Jun, Jul and Aug.
df['Summer'] = (df['Jun'] + df['Jul'] + df['Aug'])/3
#problem 2
df['5YMA'] = df['Summer'].rolling(window=5).mean()

#Problem 3
#Use the numpy, polyfit and poly1d methods to obtain a least squares linear fit for the Summer data. Create a new column named lfit containing the values of that polynomial at each index value. Plot the resulting line

coefs = np.polyfit(df.index, df['Summer'], 1)
f = np.poly1d(coefs) #creates a polynom object from coefs
df['lfit'] = f(df.index)

#Problem 4
#Repeat the previous problem using a least squares linear fit for the data before 1970. Name the column lfit1 so we don’t replace the data produced by the previous problem.
df_Before1970 = df.loc[:1969]
coefs_1 = np.polyfit(df_Before1970.index, df_Before1970['Summer'], 1) #for data before 1970
f_1 = np.poly1d(coefs_1) #creates a polynom object from coefs_1
df['lfit1'] = f_1(df.index)

#Problem 5
#Repeat the previous problem using a least squares linear fit for the data since 1970. Name the column lfit2 so we don’t replace the data produced by the previous problem.
df_Since1970 = df.loc[1970:]
coefs_2 = np.polyfit(df_Since1970.index, df_Since1970['Summer'], 1) #for data after 1970
f_2 = np.poly1d(coefs_2) #creates a polynom object from coefs_1
df['lfit2'] = f_2(df.index)

# Plot the 'Jun' values as a scatter plot:
#df['Jun'].plot(style='o',markersize=3)
df['Summer'].plot(style='*', markersize=4) #Replace the scatter plot for Jun with one for the Summer column.

#compute a new column named 5YMA to compute a 5 year moving average of the Summer column and add it to the plot as a curve.
df['5YMA'].plot()
df['lfit'].plot()
df['lfit1'].plot()
df['lfit2'].plot()
# Show the legend
plt.legend()

# Show the plot
plt.show()

#Problem 6
#Is the trend of average temperatures increasing, decreasing, or stable? Is it accelerating or decelerating?
#The trend of the average temperatures is increasing. It is accelerating since 1970. 
