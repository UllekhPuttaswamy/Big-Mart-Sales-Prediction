# Big Mart Sales Prediction

This project aims to predict the sales of items in various outlets of Big Mart using machine learning techniques. The project involves data analysis, feature engineering, model development using the XGBoost algorithm, and deployment with a Flask-based web UI. Additionally, an interactive dashboard was created using Power BI to visualize insights from the data.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Analysis](#data-analysis)
- [Modeling](#modeling)
- [Web Application](#web-application)
- [Power BI Dashboard](#power-bi-dashboard)
- [Usage](#usage)
- [Results](#results)


## Project Overview

Big Mart operates several outlets and sells a variety of products. The goal of this project is to predict the sales of each product based on historical data, outlet characteristics, and product attributes. The XGBoost algorithm was selected for its performance in handling structured data. The project also includes a user interface for easy interaction with the model, as well as a Power BI dashboard for visualizing data insights.

## Data Analysis

Extensive data analysis was performed to understand the relationships between features and the target variable. The steps included:

- **Data Cleaning:** Handling missing values, correcting inconsistencies.
- **Exploratory Data Analysis (EDA):** Visualizing distributions, correlations, and patterns.
- **Feature Engineering:** Creating new features like `Item_Age`, encoding categorical variables.

## Modeling

The XGBoost algorithm was used for prediction. Key steps included:

- **Feature Selection:** Identifying the most important features.
- **Model Training:** Tuning hyperparameters using cross-validation.
- **Evaluation:** Assessing model performance using metrics such as RMSE.

## Web Application

A Flask web application was developed to provide a user-friendly interface for predictions. Users can input item details, and the model predicts the sales.
### Form

Users can input the item details in the form below to get predictions.

![UI Form](ui_form.png)

### Prediction

After submitting the form, the predicted sales are displayed on the results page.

![UI Results](ui_results.png)


## Power BI Dashboard

An interactive Power BI dashboard was created to visualize insights from the data. The dashboard includes:

- Sales by Outlet Type
- Sales by Item Type
- Outlet Size Analysis
- Sales Distribution
  
![Power BI Dashboard](dashboard_screenshot.png)

[View the Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDVkMWU4ZWEtMTk3YS00MGVjLTkxN2MtNjYxZTRmNDYyMmZjIiwidCI6IjcyNmMyZWUzLWY3NmQtNDA1OS05OWNhLWUxOTI3YWIyMmM2NiJ9)

## Usage

1. Run the Flask web app using `python app.py`.
2. Enter the item details in the web form to predict sales.
3. Explore the dataset and insights using the Power BI dashboard.

## Results

The model successfully predicts sales with a reasonable level of accuracy. The Power BI dashboard provides valuable insights into the sales patterns and outlet characteristics.



