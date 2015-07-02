'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency': 'agency', 
                         'raceethnicity': 'race'}, inplace=True)

# 2. Show the count of missing values in each column

killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"

killings.fillna('Unknown', inplace=True)
killings.isnull().sum()

# 4. How many killings were there so far in 2015?

killings.groupby(['year']).count()
killings.shape #total rows and columns

# 5. Of all killings, how many were male and how many female?

killings[killings.gender == 'Male'].count()
killings[killings.gender == 'Female'].count()

# 6. How many killings were of unarmed people?

killings[killings.armed == 'No'].count()

# 7. What percentage of all killings were unarmed?

#NA_avg = sum(NA_beers) / len(NA_beers)
#EU_avg = sum(EU_beers) / len(EU_beers)

killings[killings.armed == 'No'].count() / killings.shape[0]
    
# 8. What are the 5 states with the most killings?

killings.state.value_counts().head()
#killings.groupby(['state']).count().sort(ascending=True).head(5)

# 9. Show a value counts of deaths for each race

killings.race.value_counts()

# 10. Display a histogram of ages of all killings

import matplotlib as pd
killings.age.hist()
#killings.age.hist(bins=200)

# 11. Show 6 histograms of ages by race

killings.age.hist(by=killings.race)

# 12. What is the average age of death by race?

killings.groupby(['race']).age.mean()

# 13. Show a bar chart with counts of deaths every month

#killings.age.count().plot(kind='bar')
#killings.month.mean().plot(kind='bar')
#killings.plot(kind='bar', by=killings.month)
###################
### Less Morbid ###
###################

majors = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

del majors['Employed_full_time_year_round']   
del majors['Major_code']  

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

majors.sort_index(by='Median', ascending=False).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors.sort_index(by='Median', ascending=False).Median.head(10).\
    plot(kind='bar',title="Bar Chart of Highest Paying Majors")
    
###help(pd.DataFrame.plot) - Cool help menue
### \ = allows you to move a long line down 

# 5. What is the average median salary for each major category?

majors.groupby('Major_category').Median.mean()

# 6. Show only the top 5 paying major categories

majors.groupby('Major_category').Median.mean().order(ascending=False)
help(pd.DataFrame.sort_index)
#majors.groupby(['Major_category']).mean().head(5)

# 7. Plot a histogram of the distribution of median salaries

#How to make it center distributed
majors.sort_index(by='Median', ascending=False).Median.head(10).\
    plot(kind='hist',title="Histogram of Highest Paying Majors")
    
# 8. Plot a histogram of the distribution of median salaries by major category



# 9. What are the top 10 most UNemployed majors?

majors.groupby('Major_category').Unemployed.sum().order(ascending=False).head(10)

# What are the unemployment rates?



# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
