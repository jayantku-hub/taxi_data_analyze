# important library to use for building data_frame
import pandas as pd
import pandas as pd
import numpy as np

df = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv")

print("Done")

# =======================================================================================================================================================================================

# Task 1. Understand the data - Inspect the data

print(df.head(10))
print(df.info())
print(df.describe())

# Question 1 : a. While reviewing df.info output, what do you notice about the diffrent variable? 
#              b. are there any null value? 
#              c. Are all the variable numeric? 
#              d. Does anything else standout?

# Answer :  a. Dtype are  non-numeric 
#           b. no-null value are there in any column
#           c. not all variable are numeric

# ==========================================================================================================================================================================================

# Question 2: a. While reviewing the df.describe() output, what do you notice about the distribution of each variable? 
           #  b. Are there any quationable value

# Answer : a. most fare are in normal range(25%-75%), but MAX = $1000 which is outlier, Negative vaalue(fare cannot be negative) 
#             so there are data errors or outlier
#             most trip are 1-3 miles(normal)              


#===========================================================================================================================================================================================

# Question 3: Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?

df_sort = df.sort_values(by=['trip_distance'], ascending=False)
print(df_sort)

# Answer : The values align with our earlier data discovery, where we noticed that the longest rides are approximately 33 miles.

# ==========================================================================================================================================================================================

# Question 4: Sort by your second variable (`total_amount`), are any values unusual?

df_sort = df.sort_values(by=['total_amount'], ascending=False)
print(df_sort)

# Answer : Yes, the first two values are significantly higher than the others. 

# ==========================================================================================================================================================================================

# Question 5: Are the resulting rows similar for both sorts? Why or why not?

# Answer : The most expensive rides are not necessarily the longest ones. 

# ==========================================================================================================================================================================================

# Sort the data by total amount and print the top 20 values

df_sort = df.sort_values(by=['total_amount'], ascending=False)['total_amount']

print(df_sort.head(20))


# ===========================================================================================================================================================================================

# How many of each payment type are represented in the data?
df_count = df['payment_type'].value_counts()
print(df_count)


# ==========================================================================================================================================================================================

# What is the average tip for trips paid for with credit card?

avg_cc_tip = df[df['payment_type']==1]['tip_amount'].mean()
print('avg tip via credit card:', avg_cc_tip)


avg_cash_tip = df[df['payment_type']==2]['tip_amount'].mean()
print("avg tip via cash :", avg_cash_tip)

# ===================================================================================================================================================================================================

# How many times is each vendor ID represented in the data?

Vendor_count = df['VendorID'].value_counts()
print(Vendor_count)

# ===================================================================================================================================================================================================

# What is the mean total amount for each vendor?

vendor_total_amount = df.groupby['VendorID'].mean(numeric_only = True)[['total_amount']]
print(vendor_total_amount)

#==================================================================================================================================================================================================================

