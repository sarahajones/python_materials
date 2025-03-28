# =============================================================================
# Lab 7 - Monday 10/21/2024 - Pandas (Lectures 14)
# Computing in Context 2024: HPM Context - Dr Sarah Ashcroft-Jones

# This script should help revise the content of Lecture 14
# =============================================================================

# Pandas is an excellent module for reading, wrangling, and analyzing data.
# It is speedy (because it uses numpy under the hood - more on this later).
# It is also intuitive (mostly) and versatile.
# We will use Pandas in our context lectures/labs moving forward
# but this is a good taster to start with!

import pandas as pd  # standard to import as pd for speed

# Let's follow Prof. Cannon's idea of making a dict

contacts_list = []  # first we make the empty list
# now populate it with dictionaries
contacts_list.append({'name': 'Fiachra', 'email': 'fiachra@irish.email'})
contacts_list.append({'name': 'Niamh', 'email': 'niamh@irish.email'})
contacts_list.append({'name': 'Sorcha', 'email': 'sorcha@irish.email'})
contacts_list.append({'name': 'Fionn', 'email': 'fionn@irish.email'})
# now use a for loop to create a dictionary of dictionaries
contacts_dict = {}
for contact in contacts_list:
    contacts_dict[contact['name']] = contact

contacts_dict  # we now have a dict of dicts with contact info
contacts_list[2]['email']  # this is the list
contacts_dict['Sorcha']['email']  # this is the dictionary

# However, a more intuitive way to view, search and splice these data ...
# is a dataframe that we can create using pandas
my_contacts = pd.DataFrame(contacts_list)
my_contacts.loc[2]  # this calls the row of interest by index
my_contacts.loc[2]['email']  # just like with our dict above

# we can index based on any column of interest
my_contacts = my_contacts.set_index('name')
my_contacts  # note index col is gone now

# Let's look at a basic data set:
# import os
# curr_path = os.chdir(os.path.dirname((os.path.abspath(__file__))))

df = pd.read_csv("income_data.csv")  # load in data
df = df.set_index('index')  # remove automatic index col

df.shape  # check what's in the data

df.head()  # check first 5 rows
df.tail(2)  # check last 2 rows

# subset your data = just look at certain cols
df_slim = df[['annual_income_category', 'annual_income']]
df_slim.columns

# look at some values
income = df_slim[['annual_income']]
income.min()
income.max()
income.mean()
income.median()
income.describe()

df_slim.describe()

# filter our dataframe based on some values
zero_sum = (df_slim['annual_income'] == 0)
filter_df = df_slim[zero_sum]  # this is also known as masking
# zero_sum is the boolean mask, which we use to filter df_slim

# We will spend a lot of time expanding on pandas in the coming weeks.
# For now let's just take this knowledge and complete Lab 7!
