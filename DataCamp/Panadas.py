import pandas as pd
import numpy as np
import matplotlib.pyplot as ply

pd.set_option('display.width', 200)
dates = pd.date_range('20150101', periods=5)
print(dates)


df = pd.DataFrame(np.random.randn(5, 4),index=dates,columns=list('ABCD'))
print(df)

print(dates)


print("Head of this DataFrame:")
print(df.head())
print("Tail of this DataFrame:")
print(df.tail(3))

print(df.shape)

print(df.describe())

print(df['Cherry'].value_counts()) #Catelog inspection

#bar plot for discret data
df[df.population >100000] #outline errors

#Histogram for continous data

#Box plot for visual basic summary statistics
df.boxplot(column ='population', by ='continent')

#Tidy up the data with metlt

#usr .pivot_table instead of pivot



