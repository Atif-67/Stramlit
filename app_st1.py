#impoting the pakages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#add title 
st.title("DATA SCIENCE ANALYSIS APP")

#add sub_title
st.subheader("This app is made by @ATIF")

#load data sets
df= sns.load_dataset('tips')

# Create a dropdown list to select from multiple datasets
datasets = ["tips", "iris", "titanic", "diamonds", "anscombe", "longley", "fmri", "exercise"]
selected_dataset = st.sidebar.selectbox("Select a dataset", datasets)

# Load the selected dataset
if selected_dataset:
    df = sns.load_dataset(selected_dataset)

# Add a button to upload a custom dataset
uploaded_file = st.file_uploader("Upload your own dataset (CSV or Excel file)", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)

# Display the loaded dataset
if df is not None:
    st.write(df)

#display  the number of rows od data sets
st.write(f"**Number of rows and columns in the dataset**: {df.shape[0]}")
st.write(f"**Number of columns and columns in the dataset**: {df.shape[1]}")

#disply the data type
st.write('Columns names asnd dtat types:',df.dtypes)

#printing the null values if they are >0
if  df.isnull().sum().sum():
    st.write('Null Values:', df.isnull().sum())
else:
    st.write('No null values')

#display the summury of selected data
st.write('Summary Statistics:'  , df.describe())

#display the correlation matrix of selected  data
#st.write('Correlation Matrix:' ,df.corr())

#Create a  pair plot
st.subheader("Pairplot")
hue_column= st.selectbox ( 'Select the coulmn used in hue:',df.columns)
st.pyplot(sns.pairplot(df, hue=hue_column))
#It will take some time to plot

#Create the heat map
st.subheader("Heatmap")
import plotly.graph_objs as go

#Select the columns which are numerics and then create a co_matrix
numeric_columns = df.select_dtypes(include=np.number).columns
corr_metrix= df [numeric_columns].corr()
numeric_columns=  df.select_dtypes(include=np.number).columns
corr_metrix= df [numeric_columns].corr()

#convert the heatmap into pyplotly figure
heatmap_fig = go.Figure(data=go.Heatmap(z=corr_metrix.values,
                                       x=corr_metrix.columns,
                                       y=corr_metrix.columns,
                                       colorscale='viridis'))
st.plotly_chart(heatmap_fig)