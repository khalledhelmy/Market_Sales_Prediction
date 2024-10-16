import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title='Sales Prediction',
    page_icon="👋"
)

st.write("# Welcome to Our Page! 👋")

st.write("""
    This application allows you to predict the sales of items in retail outlets based on various input features.
    
    **Main Features:**
    1. **Sales Prediction**: Predict sales based on item details such as weight, fat content, visibility, and price.
    2. **Data Visualizations**: Explore insightful visualizations that highlight sales performance by outlet type, location, size, and more.
    
    Use the radio buttons above to navigate through the different sections. Start predicting or explore the data through the visualizations!
    
    Enjoy using the app, and feel free to experiment with the custom visualization feature to create your own analysis.
    """)

tab1,tab2 = st.tabs(['Predict','Data Visualization'])


with tab1:
        # Load model and data
        try:
            reg = pickle.load(open('Ridge_Regression_best_model.pkl', 'rb'))
            clean_df = pd.read_csv('cleaned_data.csv')
        except FileNotFoundError as e:
            st.error(f"Error loading files: {e}")
            st.stop()

        # App Title and Description
        st.title('Sales Prediction App')
        st.write("This app predicts the sales of items in retail outlets based on various input features. Fill out the details below and click 'Predict Sales' to see the predicted value.")

        # Input fields
        st.header("Item Details")
        item_id = st.selectbox('Item ID', clean_df['Item_Identifier'].unique(), help="Select the unique identifier for the item.")
        weight = st.number_input('Weight (in kg)',
                                min_value=float(clean_df['Item_Weight'].min()),
                                max_value=float(clean_df['Item_Weight'].max()),
                                help="Enter the weight of the item.")
        fat_content = st.selectbox('Fat Content', clean_df['Item_Fat_Content'].unique(), help="Select the fat content of the item.")
        visibility = st.number_input('Visibility (percentage)',
                                    min_value=float(clean_df['Item_Visibility'].min()),
                                    max_value=float(clean_df['Item_Visibility'].max()),
                                    help="Enter the visibility percentage of the item in stores.")
        item_type = st.selectbox('Item Type', clean_df['Item_Type'].unique(), help="Select the type of the item.")
        item_price = st.number_input('Item Price',
                                    min_value=float(clean_df['Item_MRP'].min()),
                                    max_value=float(clean_df['Item_MRP'].max()),
                                    help="Enter the maximum retail price of the item.")

        st.header("Outlet Details")
        outlet_id = st.selectbox('Outlet ID', clean_df['Outlet_Identifier'].unique(), help="Select the outlet identifier.")
        year = st.number_input('Year of Establishment',
                            min_value=int(clean_df['Outlet_Establishment_Year'].min()),
                            max_value=int(clean_df['Outlet_Establishment_Year'].max()),
                            help="Enter the year the outlet was established.")
        size = st.selectbox('Outlet Size', clean_df['Outlet_Size'].unique(), help="Select the size of the outlet.")
        location = st.selectbox('Outlet Location Type', clean_df['Outlet_Location_Type'].unique(), help="Select the location type of the outlet.")
        outlet_type = st.selectbox('Outlet Type', clean_df['Outlet_Type'].unique(), help="Select the type of the outlet.")

        # Prediction button
        if st.button('Predict Sales'):
            # Create new data for prediction
            new_data = pd.DataFrame({
                'Item_Identifier': [item_id],
                'Item_Weight': [weight],
                'Item_Fat_Content': [fat_content],
                'Item_Visibility': [visibility],
                'Item_Type': [item_type],
                'Item_MRP': [item_price],
                'Outlet_Identifier': [outlet_id],
                'Outlet_Establishment_Year': [year],
                'Outlet_Size': [size],
                'Outlet_Location_Type': [location],
                'Outlet_Type': [outlet_type]
            })

            # Prediction and output
            try:
                pred = reg.predict(new_data)
                price = np.exp(pred)
                st.success(f"The predicted sales for Item ID {item_id} is ₹{price[0].round(2)}")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

with tab2:

    df = pd.read_csv('cleaned_data.csv')

    st.title('Data Visualization')

    visualization_choice = st.selectbox(
            "Choose Your Visualization Adventure:",
            ['Price Impact on Sales', 'Comparative Sales Across Outlet Types', 
            'Sales Performance by Location', 'Impact of Outlet Size on Sales', 
            "Fat Content's Influence on Sales", 'Sales Breakdown by Item Type', 
            'Impact of Outlet Age on Sales Performance', 'Build Your Custom Visualization'] 
        )

    def plot_scatter():
        st.subheader('Relationship Between Item Price and Sales Performance')
        fig = px.scatter(df, x='Item_MRP', y='Item_Outlet_Sales', color='Outlet_Size')
        st.plotly_chart(fig)

    def plot_bar_outlet_type_sales():
        st.subheader('Outlet Type vs. Sales')
        type_sales = df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean().reset_index()
        fig = px.bar(type_sales, x='Outlet_Type', y='Item_Outlet_Sales', 
                    color='Outlet_Type')
        st.plotly_chart(fig)

    def plot_bar_outlet_location_sales():
        st.subheader('Outlet Location vs. Sales')
        location_sales = df.groupby('Outlet_Location_Type')['Item_Outlet_Sales'].mean().reset_index()
        fig = px.bar(location_sales, x='Outlet_Location_Type', y='Item_Outlet_Sales',
                    color='Outlet_Location_Type')
        st.plotly_chart(fig)

    def plot_bar_outlet_size():
        st.subheader('Outlet Size: Barplot and Boxplot')
        size_sales = df.groupby('Outlet_Size')['Item_Outlet_Sales'].mean().reset_index()

        # Barplot
        bar_fig = px.bar(size_sales, x='Outlet_Size', y='Item_Outlet_Sales', 
                        color='Outlet_Size')

        # Boxplot
        box_fig = px.box(df, x='Outlet_Size', y='Item_Outlet_Sales', color='Outlet_Location_Type')

        st.plotly_chart(bar_fig)
        st.plotly_chart(box_fig)

    def plot_bar_fat_content_sales():
        st.subheader('Item Fat Content vs. Sales')
        fat_sales = df.groupby('Item_Fat_Content')['Item_Outlet_Sales'].mean().reset_index()
        fig = px.bar(fat_sales, x='Item_Fat_Content', y='Item_Outlet_Sales', 
                    color='Item_Fat_Content')
        st.plotly_chart(fig)

    def plot_bar_item_type_sales():
        st.subheader('Item Type vs. Sales')
        item_type_sales = df.groupby('Item_Type')['Item_Outlet_Sales'].mean().reset_index()
        fig = px.bar(item_type_sales, x='Item_Type', y='Item_Outlet_Sales', 
                    color='Item_Type')
        st.plotly_chart(fig)

    def plot_line_establishment_year_sales():

        st.subheader('Outlet Establishment Year vs. Sales')
        year_sales = df.groupby('Outlet_Establishment_Year')['Item_Outlet_Sales'].mean().reset_index()
        fig = px.line(year_sales, x='Outlet_Establishment_Year', y='Item_Outlet_Sales')
        st.plotly_chart(fig)

    def create_custom_visualization():
        st.subheader("Create Your Own Visualization")

        # Create tabs for different chart types
        tab1, tab2, tab3, tab4 = st.tabs(['Scatter Plot', 'Histogram', 'Line Chart', 'Bar Plot'])
        numerical_columns = df.select_dtypes(include=np.number).columns

        # Scatter Plot Tab
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                x_column = st.selectbox('Select X-axis Column', numerical_columns, key='scatter_x')
            with col2:
                y_column = st.selectbox('Select Y-axis Column', numerical_columns, key='scatter_y')
            with col3:
                color = st.selectbox('Select Color Column', df.columns, key='scatter_color')

            # Create and display the scatter plot with a spinner
            with st.spinner("Generating Scatter Plot..."):
                fig = px.scatter(df, x=x_column, y=y_column, color=color)
                st.plotly_chart(fig)

        # Histogram Tab
        with tab2:
            hist_column = st.selectbox('Choose Feature for Histogram', numerical_columns, key='histogram_column')

            # Create and display the histogram with a spinner
            with st.spinner("Generating Histogram..."):
                hist = px.histogram(df, x=hist_column)
                st.plotly_chart(hist)

        # Line Chart Tab
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col1:
                x_column = st.selectbox('Select X-axis Column', numerical_columns, key='line_x')
            with col2:
                y_column = st.selectbox('Select Y-axis Column', numerical_columns, key='line_y')
            with col3:
                color = st.selectbox('Select Color Column', df.columns, key='line_color')

            # Create and display the line chart with a spinner
            with st.spinner("Generating Line Chart..."):
                fig = px.line(df, x=x_column, y=y_column, color=color)
                st.plotly_chart(fig)

        # Bar Plot Tab
        with tab4:
            col1, col2, col3 = st.columns(3)
            with col1:
                x_column = st.selectbox('Select X-axis Column', df.columns, key='bar_x')
            with col2:
                y_column = st.selectbox('Select Y-axis Column', df.columns, key='bar_y')
            with col3:
                color = st.selectbox('Select Color Column', df.columns, key='bar_color')

            # Create and display the bar plot with a spinner
            with st.spinner("Generating Bar Plot..."):
                bar = px.bar(df, x=x_column, y=y_column, color=color)
                st.plotly_chart(bar)


    if visualization_choice == 'Price Impact on Sales':
        plot_scatter()
    elif visualization_choice == 'Comparative Sales Across Outlet Types':
        plot_bar_outlet_type_sales()
    elif visualization_choice == 'Sales Performance by Location':
        plot_bar_outlet_location_sales()
    elif visualization_choice == 'Impact of Outlet Size on Sales':
        plot_bar_outlet_size()
    elif visualization_choice == "Fat Content's Influence on Sales":
        plot_bar_fat_content_sales()
    elif visualization_choice == 'Sales Breakdown by Item Type':
        plot_bar_item_type_sales()
    elif visualization_choice == 'Impact of Outlet Age on Sales Performance':
        plot_line_establishment_year_sales()
    elif visualization_choice == 'Build Your Custom Visualization':
        create_custom_visualization() 