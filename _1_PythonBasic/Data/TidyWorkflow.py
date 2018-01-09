# The pre exercise code runs code to initialize the user's workspace.
import pandas as pd
url1 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/df1.csv'
url2 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/df2.csv'
url3 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/messy.csv'

df1 = pd.read_csv(url1, sep = ',')
df2 = pd.read_csv(url2, sep = ',')
messy = pd.read_csv(url3, sep=',')

# Import pandas as pd
import pandas as pd
print(df2)
# Melt df2 into new dataframe: df2_melted
df2_melted = pd.melt(df2, id_vars=['Country'])

# print df2_melted
print(df2_melted)