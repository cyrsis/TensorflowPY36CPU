#Resampling frequencies

# Input                     Description
# ***********				  **************
# 'min', 'T'                minute
# 'H'						  hour
# 'D'						  day
# 'B'						  business day
# 'W'						  week
# 'M'						  month
# 'Q'						  quarter
# 'A'						  year


# Pandas provides methods for resampling time series data. When downsampling (going from minute to hourly for ex.) or upsampling (going from hourly to minute), the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.
#
# For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().
import pandas as pd

df = pd.DataFrame()
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()



# Extract temperature data for August: august
august = df['Temperature']['2010-August']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature']['2010-February']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()





# Below is an exercise in chaining the rolling() function to creating a rolling or moving average. This can be chained along w/ a resample to up/down-sample data.

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed': smoothed, 'unsmoothed': unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()