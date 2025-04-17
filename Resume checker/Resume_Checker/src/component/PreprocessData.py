import pandas as pd
import ast
import pickle
import string
import os

# Define file paths
df = pd.read_csv('Resume_Checker\src\OutputCSV\saved_data.csv')

# --- Basic Info ---
first_name = df['First Name'].iloc[0]
last_name = df['Last Name'].iloc[0]
name = string.capwords(f"{first_name} {last_name}")
mob_no = df['Contact No'].iloc[0]
email = df['Email'].iloc[0]

# --- Education ---
data = df['Education'].iloc[0]
sample = ast.literal_eval(data)
count = 1
for values in sample.values():
    if count == 1:
        col1_name = string.capwords(values[0])
        col1_duration = values[1]
        count += 1
    else:
        col2_name = string.capwords(values[0])
        col2_duration = values[1]

# --- Project ---
data = df['Project'].iloc[0]
sample = ast.literal_eval(data)
count = 1
for values in sample.values():
    if count == 1:
        proj_title = string.capwords(values)
        count += 1
    else:
        proj_disc = string.capwords(values)

# --- Experience ---
data = df['Experience'].iloc[0]
sample = ast.literal_eval(data)
count = 1
for values in sample.values():
    if count == 1:
        job_title = string.capwords(values)
        count += 1
    elif count == 2:
        job_durn = values
        count += 1
    else:
        job_disc = values

# --- Lists ---
skill_list = str(df['Skills'].iloc[0]).split(',') if pd.notna(df['Skills'].iloc[0]) else []
acheive_list = str(df['Achievement'].iloc[0]).split(',') if pd.notna(df['Achievement'].iloc[0]) else []
cert_list = str(df['Certificate'].iloc[0]).split(',') if pd.notna(df['Certificate'].iloc[0]) else []

# --- Summary ---
summary = df['Summary'].iloc[0]


