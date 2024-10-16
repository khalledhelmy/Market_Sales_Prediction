# Market Sales Prediction

This project focuses on predicting sales for a variety of products using machine learning models. The goal is to explore relationships between different features, apply feature engineering techniques, and develop predictive models to forecast sales more accurately.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Streamlit App](#Streamlit-App)


## Project Overview
The Market Sales Prediction project is a data science solution aimed at predicting sales for products across various outlets. By understanding the key drivers behind sales performance, this project helps optimize inventory management, pricing strategies, and promotional efforts.

## Dataset
The dataset used in this project can be found on Kaggle: [Big Mart Sales Prediction Dataset](https://www.kaggle.com/datasets/shivan118/big-mart-sales-prediction-datasets)

The dataset used in this project has the following columns:
- **Item_Identifier**: Unique identifier for each item.
- **Item_Weight**: Weight of the item (some missing values).
- **Item_Fat_Content**: Indicates whether the item is low fat or regular.
- **Item_Visibility**: Percentage visibility of the item in the store.
- **Item_Type**: Category/type of the item (e.g., Dairy, Meat).
- **Item_MRP**: Maximum retail price of the item.
- **Outlet_Identifier**: Unique identifier for each outlet.
- **Outlet_Establishment_Year**: Year when the outlet was established.
- **Outlet_Size**: Size of the outlet (some missing values).
- **Outlet_Location_Type**: Tiered categorization of the outlet's location.
- **Outlet_Type**: Type of outlet (e.g., Grocery Store, Supermarket).
- **Item_Outlet_Sales**: Sales of the item at the respective outlet (target variable).

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/khalledhelmy/Market_Sales_Prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Market_Sales_Prediction
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Exploratory Data Analysis
The exploratory data analysis (EDA) includes:
- Distribution analysis of numerical features
- Correlation analysis between features and sales
- Visualization of sales trends by product type and outlet type

## Feature Engineering
In this project, we performed several feature engineering steps:
- Imputation of missing values for `Item_Weight`
- Imputation of missing values for `Outlet_Size`
- Handling categorical variables with encoding techniques

## Modeling
We trained and evaluated several machine learning models:
- Linear Regression
- Decision Trees
- Random Forest
- Gradient Boosting

The performance of these models was evaluated using metrics like RMSE (Root Mean Square Error) and R².

## Results
The best-performing model was **Ridge**, achieving an R2 of **0.75** on the test data.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Streamlit App
You can interact with the Market Sales Prediction application through the following link: [Market Sales Prediction App]([https://market-sales-prediction.streamlit.app/v](https://market-sales-prediction.streamlit.app/])
