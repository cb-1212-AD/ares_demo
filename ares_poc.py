import re
import streamlit as st  
import pandas as pd
import numpy as np
import glob
import plotly.express as px
import streamlit.components.v1 as components
from streamlit_cards import show_cards
import base64
from io import BytesIO

def generate_company_list():
    companies = []
    unique_list = []
    file_list = glob.glob("C:/Users/curt.beck/OneDrive/Financial_Mapping/Ares/*.xlsx") # change filepath
    for file in file_list:
        match_obj = re.search("[A-Za-z]+\_\d+|[A-Za-z]+\s+[\&A-Za-z\s\_\d]+", file)
        if match_obj is not None:
            split_str = match_obj.group().split('_')
            split_str_item = split_str[0]
            companies.append(split_str_item)
    
    for company in companies:
        if company not in unique_list:
            unique_list.append(company)
    no_spaces = [company.strip() for company in unique_list]
    clean_list = [company for company in no_spaces if company]
    return clean_list

def plot_chart(df, line_item):
    val_list = []
    filtered_df = df[df[df.columns[0]] == line_item]
    filtered_df = filtered_df.set_index(filtered_df.columns[0])
    vals = filtered_df.values
    new_df = pd.DataFrame({'Period': list(filtered_df.columns[0:]), 'Value': vals[0]})
    fig = px.line(new_df, x='Period', y='Value', title=f'{line_item} Timeseries')
    st.plotly_chart(fig)

def convert_statement_option(statement_type):
    if statement_type == 'Balance Sheet':
        modified_statement_type = 'BS'
    elif statement_type == 'Income Statement':
        modified_statement_type = 'IS'
    elif statement_type == 'Cashflow':
        modified_statement_type = 'CS'
    
    return modified_statement_type

def get_table_download_link(df, company, statement):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{company}_{statement}">Download CSV</a>'
    return href

def clean_data(file):
    df = pd.read_excel(file[0])
    df.fillna(0, inplace=True)
    clean_df = df.rename(columns={df.columns[0]: ''})
    return clean_df

def load_data(company, statement):
    modified_statement = convert_statement_option(statement)
    if modified_statement != 'BS':
        st.write("Data is not yet available")
    else:
        file = glob.glob(f'C:/Users/curt.beck/OneDrive/Financial_Mapping/Ares Output/*{company}*{modified_statement}*.xlsx')
        df = clean_data(file)
        item_dropdown = st.sidebar.selectbox('Reporting Item', df[df.columns[0]].values.tolist())
        show_cards(company, file_count(company), df.columns[-1])
        st.markdown(f"<h3>{dropdown}'s {statement_type} - {report_type}</h3>", unsafe_allow_html=True)
        st.dataframe(df)
        st.markdown(get_table_download_link(df, company, statement), unsafe_allow_html=True)
        plot_chart(df, item_dropdown)



def load_as_reported_data(company, statement):

    if statement != 'Balance Sheet':
        st.write("Data is not yet available")
    else:
        file = glob.glob(f'C:/Users/curt.beck/OneDrive/Financial_Mapping/Ares As Reported Ouput/*{company}*{statement}*.xlsx')
        df = clean_data(file)
        item_dropdown = st.sidebar.selectbox('Reporting Item', df[df.columns[0]].values.tolist())
        show_cards(company, file_count(company), df.columns[-1])
        st.markdown(f"<h3>{dropdown}'s {statement_type} - {report_type}</h3>", unsafe_allow_html=True)
        st.dataframe(df)
        st.markdown(get_table_download_link(df, company, statement), unsafe_allow_html=True)
        plot_chart(df, item_dropdown)

def file_count(company):
    files = glob.glob(f"C:/Users/curt.beck/OneDrive/Financial_Mapping/Ares/*{company}*.xlsx")
    return len(files)


companies = generate_company_list()
companies.remove('Hurtigruten')




dropdown = st.sidebar.selectbox('Select a Company', companies)

statement_type = st.sidebar.radio('Statement Type', ('Balance Sheet', 'Income Statement', 'Cashflow'))

report_type = st.sidebar.radio('Report Type', ('Restated', 'As Reported'))

if dropdown:
    if report_type == 'As Reported':
        load_as_reported_data(dropdown, statement_type)
    else:
        load_data(dropdown, statement_type)




