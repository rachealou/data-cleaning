import pandas as pd
import numpy as np

df = pd.read_csv('DataAnalyst.csv')
# data set from Kaggle: https://www.kaggle.com/andrewmvd/data-analyst-jobs

# drop unnamed column
df = df.drop(df.columns[0], axis=1)

# get rid of -1 values in different categories
df = df[df['Salary Estimate'] != -1]
df = df[df['Rating'] != -1]
df = df[df['Founded'] != -1]
df = df[df['Industry'] != '-1']

# SALARY
# get numeric values of salary 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

# get rid of $ and - 
no_dollar_dash = salary.apply(lambda x: x.replace('$', '').replace('K', ''))

# update salary estimate in df
df['Salary Estimate'] = salary

# get minimum and maximum salary values
min_salary = no_dollar_dash.apply(lambda x: x.split('-')[0])
max_salary = no_dollar_dash.apply(lambda x: x.split('-')[1])

# concatenate min and max salary series to df
df['Minimum Salary'] = min_salary
df['Maximum Salary'] = max_salary

# COMPETITORS
# change competitors to -1 and 0 (want integers OR strings)
comp_mod = df['Competitors'].apply(lambda x: 0 if x == '-1' else 1)
df['Competitors'] = comp_mod

# EASY APPLY
# change easy apply to -1 and 0 (consistency)
easy_apply_mod = df['Easy Apply'].apply(lambda x: 0 if x == '-1' else 1)
df['Easy Apply'] = easy_apply_mod

print(df['Rating'].dtype)
print(df['Company Name'].dtype)

# the following does not work bc in df['Company Name'] there is no 'Rating' to iterate over
# comp_name_mod = df['Company Name'].apply(lambda x: x if x['Rating'] < 0 else x['Company Name'][:-3])

# need to add axis = 1 to iterate through rows, and not down each column
# will give error "KeyError: 'Rating' as it won't find ratings going through each column but will through each row

# Filter for text only in Company Name
comp_mod = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
df['Company Name'] = comp_mod

# REVENUE
# remove (USD))
remove_usd = df['Revenue'].apply(lambda x: 'NaN' if x == 'Unknown / Non-Applicable' else x[:-5])
remove_dollar = remove_usd.apply(lambda x: x.replace('$', ''))
df['Revenue'] = remove_dollar

# LOCATION
# split Location into City and State
city = df['Location'].apply(lambda x: x.split(',')[0])
state = df['Location'].apply(lambda x: x.split(',')[1])
df['City'] = city
df['State'] = state

# FOUNDED
# find company age
comp_age = df['Founded'].apply(lambda x: 'NaN' if x < 0 else 2021 - x)
df['Company Age'] = comp_age

# FIND DIFFERENT KEY WORDS IN JOB TITLE
# data analyst
has_data_analyst = df['Job Title'].apply(lambda x: 1 if 'data analyst' in x.lower() else 0)
df['Data Analyst?'] = has_data_analyst

# analyst
has_analyst = df['Job Title'].apply(lambda x: 1 if 'analyst' in x.lower() else 0)
df['Analyst?'] = has_analyst

# product
has_product = df['Job Title'].apply(lambda x: 1 if 'product' in x.lower() else 0)
df['Product'] = has_product

# data entry
has_data_entry = df['Job Title'].apply(lambda x: 1 if 'data entry' in x.lower() else 0)
df['Data Entry?'] = has_data_entry

# data science
has_data_science = df['Job Title'].apply(lambda x: 1 if 'data science' in x.lower() else 0)
df['Data Science?'] = has_data_science

# data engineer
has_data_engineer = df['Job Title'].apply(lambda x: 1 if 'data engineer' in x.lower() else 0)
df['Data Engineer?'] = has_data_engineer

# senior / sr
has_senior = df['Job Title'].apply(lambda x: 1 if 'senior' or 'sr' in x.lower() else 0)
df['Senior?'] = has_senior

# junior / jr
has_junior = df['Job Title'].apply(lambda x: 1 if 'junior' or 'jr' in x.lower() else 0)
df['Junior'] = has_junior

# FIND DIFFERENT KEY WORDS(CODING LANGUAGES/SOFTWARE) IN JOB DESCRIPTION
# note: Just because a job has the following language/software, does not mean it is required
# python
has_python = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['Python?'] = has_python

# java
has_java = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['Java?'] = has_java

# R
has_R = df['Job Description'].apply(lambda x: 1 if ' R ' in x else 0)
df['R?'] = has_R

# SQL
has_SQL = df['Job Description'].apply(lambda x: 1 if 'SQL' in x else 0)
df['SQL?'] = has_SQL

# tableau
has_tableau = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['Tableau?'] = has_tableau
