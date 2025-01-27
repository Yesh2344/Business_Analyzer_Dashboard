import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def clean_numeric_column(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def perform_analysis(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    stats = df[numeric_columns].describe()
    corr_matrix = df[numeric_columns].corr()
    return stats, corr_matrix

def generate_visualizations(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    if 'NetWorth' in numeric_columns:
        # Histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        df['NetWorth'].hist(bins=50, ax=ax)
        plt.title('Distribution of Net Worth')
        plt.xlabel('Net Worth')
        plt.ylabel('Frequency')
        st.pyplot(fig)

        # Scatter plot
        if 'Age' in numeric_columns:
            fig = px.scatter(df, x='Age', y='NetWorth', hover_data=['Name', 'Country'])
            fig.update_layout(title='Age vs Net Worth')
            st.plotly_chart(fig)

    # Heatmap of correlation matrix
    if len(numeric_columns) > 1:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
        plt.title('Correlation Heatmap')
        st.pyplot(fig)

def main():
    st.set_page_config(page_title="Business Data Analyzer", layout="wide")
    st.title("Business Data Analyzer Dashboard")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            st.success("Data loaded successfully!")
            
            st.header("Data Overview")
            st.write(df.head())

            st.header("Data Cleaning")
            numeric_columns = st.multiselect("Select columns to convert to numeric", df.columns)
            for column in numeric_columns:
                df = clean_numeric_column(df, column)
            
            st.header("Basic Statistics")
            stats, corr_matrix = perform_analysis(df)
            st.write(stats)

            st.header("Visualizations")
            generate_visualizations(df)

            st.header("Top 10 Rows")
            sort_column = st.selectbox("Select column to sort by", df.columns)
            st.write(df.nlargest(10, sort_column))

            st.header("Data Explorer")
            columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist()[:5])
            st.write(df[columns])

if __name__ == "__main__":
    main()

