#victor 
#08/01/2018 
#Created @ 2018-01-08 23:05

# Define recode_sex()
# Recoding variables is a common data cleaning task. Functions provide a mechanism for you to abstract away complex bits of code as well as     # reuse code. This makes your code more readable and less error prone.
# You can use the .apply() method to apply a function across entire rows or columns of DataFrames. However, note that each column of a DataFrame # is a pandas Series. Functions can also be applied across Series. Here, you will apply your function over the 'sex' column.

def recode_sex(sex_value):
    # Return 1 if sex_value is 'Male'
    if sex_value == 'Male':
        return 1

    # Return 0 if sex_value is 'Female'
    elif sex_value == 'Female':
        return 0

    # Return np.nan
    else:
        return np.nan


# Apply the function to the sex column
tips['sex_recode'] = tips.sex.apply(recode_sex)

# Print the first five rows of tips
print(tips.head())

# Write the lambda function using replace
tips['total_dollar_replace'] = tips['total_dollar'].apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips['total_dollar'].apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())


# The .apply() method can be used on a pandas DataFrame to apply an arbitrary Python function to every element. Use the .apply() method to perform the         # conversion from F to C on the 'Mean TemperatureF' and 'Mean Dew PointF' columns of the weather DataFrame.
# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5 / 9 * (F - 32)


# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())

# The .apply() method when used on a groupby object performs an arbitrary function on each of the groups. These functions can be aggregations, transformations or more complex workflows. The .apply() method will then combine the results in an intelligent way.

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')


# A function (you can ignore this part)
def disparity(gr):
    return pd.DataFrame(x)


# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)


# By using .apply(), you can write functions that filter rows within groups. The .apply() method will handle the iteration over individual groups and then re-combine them back into a Series or DataFrame. In this exercise you'll take the Titanic data set and analyze survival rates from the 'C' deck, which contained the most passengers. To do this you'll group the dataset by 'sex' and then use the .apply() method on a provided user defined function which calculates the mean survival rates on the 'C' deck:

def c_deck_survival(gr):
    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()


# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival and print the result
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)