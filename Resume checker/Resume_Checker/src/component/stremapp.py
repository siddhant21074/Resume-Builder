import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os
# Creating Class
class HandleData:
    def __init__(self):
        self.df = pd.DataFrame(columns=[
            'UserId', 'First Name', 'Last Name', 'Contact No', 'Email',
            'Resident Address', 'Education', 'Project', 'Experience',
            'Skills', 'Certificate', 'Achievement', 'Summary'
        ])
        self.save_path = '../OutputCSV/saved_data.csv'
        
    def Handler(self, data):
        row = {col: data.get(col, None) for col in self.df.columns}
        self.df.loc[len(self.df)] = row 
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        self.df.to_csv(self.save_path, index=False)
       



# Defining Variables 
handle = HandleData()
count = 0 
df = pd.DataFrame(columns=[
    'UserId', 'First Name', 'Last Name', 'Contact No', 'Email',
    'Resident Address', 'Education', 'Project', 'Experience',
    'Skills', 'Certificate', 'Achievement', 'Summary'
])

### WEBAPP ###

# Title for app 
titile = st.markdown("# Welcome to Resume Builder")

# Adding basic information 
st.subheader("Basic Information Section")
input_first_name = st.text_input("First Name : ")
input_last_name = st.text_input("Last Name : ")
summary = st.text_area("Summary About You : ")
mobile_no = st.text_input("Contact Number : ")
email = st.text_input("Email Address : ")
address = st.text_input("Address : ")

# Education 
st.subheader("Education Section")

with st.form("edu_form"):
    st.markdown("##### 🎓 Add Education Details")
    college_name1 = st.text_input("1.Higest Education College Name:")
    year_passing1 = st.text_input("Education Year (Start - End):")
    college_name2 = st.text_input("2.   College Name:")
    year_passing2 = st.text_input("Year (Start - End):")
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Added: {college_name1} ({year_passing1})  {college_name2}(  {year_passing2})")

# Project Section
st.subheader("Project Section")

with st.form("project_form"):
    project_name = st.text_input("Project Titlel : ")
    project_info = st.text_area("Project Description : ")
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Project Detail Saved")

# Experience 
st.subheader("Experience Section")

with st.form("Exp_form"):
    job_title = st.text_input("Job Title : ")
    job_discription = st.text_area("Job discription : ")
    job_duration = st.text_input('Duration(Star - End) : ')
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Experience Detail Saved")
                
# Skills 
st.subheader("Skills Section")
st.text("For Multiple Skill Use Comma(,)")
with st.form("Skill_form"):
    skill = st.text_input("Skill : ")
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Skill Detail Saved")

# Certificates 
st.subheader("Certification Section")
st.text("For Multiple Certificate Use Comma(,)")

with st.form("Cert_form"):
    cert_name = st.text_input("Certification Title : ")
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Certificate Detail Saved")
                
# Achievements Or Activities
st.subheader("Acheivements Section")
st.text("For Multiple Acheivement Use Comma(,)")

with st.form("Achieve_form"):
    acheive_data = st.text_input("Description : ")
    submitted = st.form_submit_button("Save Data")

    if submitted:
        st.success(f"✅ Acheivements Detail Saved")
                
# Calling the handler function and storing the data in dataframe 
data_dict = {
    'First Name': input_first_name,
    'Last Name': input_last_name,
    'Summary': summary,
    'Contact No': mobile_no,
    'Email': email,
    'Resident Address': address,
    'Education': {
        'collage1': [college_name1, year_passing1],
        'collage2': [college_name2, year_passing2]
    },
    'Project': {
        'Project Title': project_name,
        'Project Description': project_info
    },
    'Experience': {
        'Job Title': job_title,
        'Job Duration': job_duration,
        'Job Description': job_discription
    },
    'Skills': skill,
    'Certificate': cert_name,
    'Achievement': acheive_data
}

# Generate Resume 
# Generate Resume 
generate_resume = st.button("Generate Resume")
if generate_resume:
    handle.Handler(data=data_dict)

