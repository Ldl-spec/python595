# 50 pts.
# You are the data scientist at an accounting firm.
# A new client gives you their inventory logs,
# but they are in horrible condition.
# No two files match!
#
# Your task is to write a generic parser that
# can extract relevant data.
#
# There are a few constants.  Phew!
# Assume every file is comma-separated.
# And that the headers use the same words:
# "Clientname"
# "Quantity"
# "Price"
# "Date"

# But, the casing is sometimes different (!!!).
# This means "date" and "dAte" sometimes
# appear.  And!
# client names also have random capitalization.

# Your script will be run from the command line.
# python accounting.py old_file0312202.csv
# with the script and the csv file.

# Your task is to print:
# largest client by revenue = quantity*price (20 pts.)
# aggregate sales revenue (20 pts.)
# month-end sales revenue (10 pts.)

# Note that month-end sales revenue includes all transactions
# for one month only, and should be dated the last day of the month.
# You are given three test files.
# Your code will have to correctly complete the task for the three csv's
# in this folder,
# and a secret fourth file of the same type.

# Bonus (+10pts)
# Have your script accept any number of inputs:
# python accounting.py old_data0312202.csv old_data032231d.csv new_data231.csv 
# and print the first three tasks on the aggregate parsed data.
# What else needs to change?
#
# Bonus (+10pts)
# If you can implement the bonus by adding
# one line of code and marginally modifying another line
# you get 10 more points.
# use comments to tell me about your design.
#
# Good luck!


import sys
import pandas as pd
import numpy as np

def parse_command_line(raw_command_line):
    return raw_command_line[1:]

def parse_csv(filename):
    '''
    :param filename: The path to the incoming file
    A third-party library is used pandas and numpy
    Added two columns to the data, grouped in years and months,
    and added income as a column
    Turn the column name into a lesser case
    '''

    # Sets the number of outputs
    number = 3

    df = pd.read_csv(filename)

    # Turn the column name into a lesser case
    df.columns = df.columns.map(lambda x: x.lower())

    # Read the file and sort it by time
    df = df.sort_values("date")

    # Add a column to the data (year, month)
    temp_list = df["date"].str[:7].tolist()
    df["date_tmp"] = pd.DataFrame(np.array(temp_list).reshape((df.shape[0], 1)))

    # Get the quantity and price
    quanTity = df["quantity"]
    price = df["price"]

    # Add a column of revenue to the data (revenue = quantity*price)
    revenue = quanTity * price
    df["total"] = pd.DataFrame(np.array(revenue).reshape((df.shape[0], 1)))

    # Turn scientific notation into float
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    # total revenue
    revenue_sum = revenue.sum()

    # Group by year and month
    grouped = df.groupby(by=df["date_tmp"]).sum()["total"].astype("float")

    # get the most revenue
    max_total = df[df["total"] == df["total"].max()]
    print("*" * 50)
    print("The name and total number of the largest earner{}  {}".format(max_total["clientname"].values, max_total["total"].values))
    print("*" * 50)
    print("Revenue {}".format(revenue_sum))
    print("*" * 50)
    print("Income from the top {}".format(number))
    print(df["total"].sort_values(ascending=False).head(number).values)
    print("*" * 50)
    print("Income for the first {} months".format(number))
    print(grouped.head(number))

if __name__ == "__main__":
    files_to_parse = parse_command_line(sys.argv)
    last_file = files_to_parse[-1]
    print("Beginning parse of", last_file)
    parse_csv(last_file)
    
