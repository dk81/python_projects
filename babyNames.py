# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:52:47 2018

@author: dk
"""

# Baby Names In Python

'''
Website Source: https://www.ssa.gov/oact/babynames/limits.html

Download zip file from National Data

Reference: Python For Data Analysis by Wes McKinney

'''

# Get current working directory: import os; os.getcwd()
# Set current working directory: import os; os.chdir(aPath)

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Set working directory (need double slash not single)
os.chdir("C:\\Users\dk\\Documents\\PythonWork\\Wordpress_Blog\\babynames")


#### 2016 Babynames:

# Import 2016 baby names data:
babynames_2016 = pd.read_csv("yob2016.txt",  names=['Name', 'Sex', 'Births'])

# Preview data with .head and .tail functions:
    
babynames_2016.head(15)

babynames_2016.tail(15)

# Counts For Each Gender:
    
babynames_2016.groupby("Sex").sum()


# Males

males_2016 = babynames_2016[babynames_2016.Sex == "M"]

males_2016.head(15)

# Females

females_2016 = babynames_2016[babynames_2016.Sex == "F"]

females_2016.head(15)

# Bar Graphs From matplotlib:
# Reference: https://matplotlib.org/gallery/lines_bars_and_markers/barh.html
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart

# Male Baby Names 2016

males_2016_15 = males_2016.head(15)

fig, ax = plt.subplots()

people = males_2016_15['Name']
counts = males_2016_15['Births']
y_pos = np.arange(len(people))


ax.barh(y_pos, counts , align='center',
        color = '#99FF99', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Count \n')
ax.set_ylabel('\n Name')
ax.set_title('Popular Male Baby Names Of 2016 \n')
ax.set_xlim([0, 22000])


for i, v in enumerate(counts):
    ax.text(v - 2200, i + 0.3, str(v), color='blue', fontweight='bold')

plt.show()

# Females Baby Names 2016

females_2016_15 = females_2016.head(15)

fig, ax = plt.subplots()

people_f = females_2016_15['Name']
counts_f = females_2016_15['Births']
y_pos_f = np.arange(len(people))

ax.barh(y_pos_f, counts , align='center',
        color = '#FF9999', ecolor='black')
ax.set_yticks(y_pos_f)
ax.set_yticklabels(people_f)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('\n Count')
ax.set_ylabel('\n Female Name')
ax.set_title('Popular Female Baby Names Of 2016 \n')
ax.set_xlim([0, 20000])


for i, v in enumerate(counts):
    ax.text(v - 2200, i + 0.3, str(v), color='#660000', fontweight='bold')

plt.show()



#### -----------------------------------------------

### Babynames as a whole:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reference: Python For Data Analysis By Wes McKinney

### Set working directory (need double slash not single)
os.chdir("C:\\Users\dk\\Documents\\PythonWork\\Wordpress_Blog\\babynames")

### 2016 is the last available year from files

years = range(1880, 2017)
pieces = []
columns = ['Baby_Name', 'Sex', 'Count']

for year in years:
    path = 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
    
### Combine/Concatenate everything into a single Pandas DataFrame

names = pd.concat(pieces, ignore_index = True)

### Preview the names dataframe:

names.head(10)

names.tail(10)

### Total Births by Gender 

total_births_gender = names.groupby("Sex").sum()["Count"]

print(total_births_gender)


### Total Births Per Year With Graph

total_births_perYear = names.groupby(["year"]).sum()

print(total_births_perYear)

# Simple plot of total births per year:

total_births_perYear.plot(title ='Total Births By Year')

# A More Refined Plot:
# Ref: https://matplotlib.org/users/pyplot_tutorial.html

plt.plot(total_births_perYear)
plt.xlabel('\n Year')
plt.ylabel('Number Of Births \n')
plt.title('Baby Births Per Year \n')

plt.show()


### Total Births Per Year By Gender
# References: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html
# https://matplotlib.org/users/legend_guide.html


# Pivot table
                
total_births_gender_year = pd.pivot_table(names, values= 'Count', index = ['year'],
                           columns = ['Sex'], aggfunc=np.sum)
                              
total_births_gender_year.head(10)                          

# Simple Plot:

total_births_gender_year.plot(title = "Total Births Per Year By Gender \n")

# A More fancy and detailed plot:
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html


total_births_male = total_births_gender_year["M"]
total_births_female = total_births_gender_year["F"]

years = range(1880, 2017)

fig, ax = plt.subplots()
ax.plot(years, total_births_female, '#bd404f', label= 'Female')
ax.plot(years, total_births_male, '#4085bd', label= 'Male')

legend = ax.legend(loc='lower right', shadow=True, fontsize='x-large')

#ax.plot(total_births_gender_year)
ax.set_xlabel('\n Year')
ax.set_ylabel('Number Of Births \n')
ax.set_title('Baby Births Per Year \n')
ax.xlim([1880, 2012])

# Put a nicer background color on the legend.

legend.get_frame().set_facecolor('#00FFCC')

plt.show()


#-----------------------------------------------------
##### Popular Baby Names With Bar Graphs

### Popular Baby Names

popular_baby_names = names.groupby(["Baby_Name", "Sex"]).sum()

popular_baby_names = popular_baby_names.sort_values(by = "Count", ascending = False)["Count"]

popular_baby_names.head(10)


### Popular Female Baby Names

female_names = names[names.Sex == 'F']

female_counts = female_names.groupby(["Baby_Name"]).sum().sort_values(by = "Count", ascending = False)

females_names_15 = female_counts.head(15)['Count']

# Ref: https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index

people_f = females_names_15.index.values # Get the names from index values 
counts_f = females_names_15
y_pos_f = np.arange(len(people_f))

fig, ax = plt.subplots()

ax.barh(y_pos_f, counts_f , align='center', color = '#FF9999', ecolor='black')
ax.set_yticks(y_pos_f)
ax.set_yticklabels(people_f)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('\n Count')
ax.set_ylabel('\n Female Name')
ax.set_title('Top 15 Most Common Female Baby Names [1880-2010] \n')
ax.set_xlim([0, 5000000])


for i, v in enumerate(counts_f):
    ax.text(v - 2200, i + 0.3, str(v), color='#660000', fontweight='bold')

plt.show()



### Popular Male Baby Names

male_names = names[names.Sex == 'M']

male_counts = male_names.groupby(["Baby_Name"]).sum().sort_values(by = "Count", ascending = False)

male_names_15 = male_counts.head(15)['Count']


# Ref: https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index

people_m = male_names_15.index.values # Get the names from index values 
counts_m = male_names_15
y_pos_m = np.arange(len(people_m))

fig, ax = plt.subplots()

ax.barh(y_pos_m, counts_m , align='center', color = '#2a5391', ecolor='black')
ax.set_yticks(y_pos_m)
ax.set_yticklabels(people_m)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('\n Count')
ax.set_ylabel('Male Baby Name \n')
ax.set_title('Top 15 Common Male Baby Names [1880-2010] \n')
ax.set_xlim([0, 5900000])


for i, v in enumerate(counts_m):
    ax.text(v - 2200, i + 0.3, str(v), color='#26421f', fontweight='bold')

plt.show()







