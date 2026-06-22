# PhonePe-Performance-Dashboard

## Project Overview

The **PhonePe Performance Dashboard** is an end-to-end data analytics project focused on analyzing digital payment transactions and generating actionable business insights. The project demonstrates the complete analytics workflow, from data cleaning and transformation in Python to interactive dashboard development in Power BI.

## Project Workflow

### Data Cleaning and Preparation

The raw PhonePe transaction dataset contained unsorted records and inconsistencies. Data preprocessing was performed using **Python (Jupyter Notebook)** to ensure data quality and accuracy.

Key preprocessing tasks included:

* Data sorting and validation
* Handling missing values
* Removing duplicate records
* Standardizing data formats
* Preparing the dataset for reporting and visualization

The cleaned dataset was then imported into Power BI for further analysis.

## Data Model

### Date Table

A dedicated Date Table was created to enable efficient time-based analysis and reporting.

**Fields Included:**

* Date
* Year
* Month
* Quarter
* Weekday
* Day Number

### PhonePe Transaction Table

The transaction dataset contains the following attributes:

* Transaction ID
* User ID
* Amount
* Service
* Service Type
* Payment Status
* Payment Method
* Reason
* Date
* Age Group

## Dashboard Features

### KPI Cards

The dashboard includes six key performance indicators (KPIs):

1. Total Transaction Value
2. Total Transactions
3. Success Rate (%)
4. Total Users
5. Month-over-Month (MoM) Transaction Growth
6. Month-over-Month (MoM) Transaction Value Growth

## Visualizations

### Line Chart

**Total Transaction Value by Month and Year**

* Displays transaction value trends over time.
* Helps identify growth patterns and seasonal fluctuations.

### Stacked Column Chart

**Total Transaction Value by Service**

* Compares transaction value across different services.
* Highlights the most utilized services.

### Stacked Column Chart

**Total Transactions by Month and Payment Status**

* Shows transaction distribution by payment status.
* Enables monitoring of successful and failed transactions over time.

### Donut Chart

**Total Transactions by Weekday/Weekend**

* Compares transaction activity between weekdays and weekends.
* Reveals customer transaction behavior patterns.

### Donut Chart

**User Distribution by Age Group**

* Visualizes the number of users across different age categories.
* Helps understand customer demographics.

## Interactive Filters (Slicers)

The dashboard includes dynamic slicers for:

* Month
* Payment Method

These filters allow users to explore and analyze data interactively.

## Key Business Insights

The dashboard provides valuable insights such as:

* Overall transaction performance and revenue trends
* Month-over-Month growth analysis
* Service-wise transaction value contribution
* Success and failure rate monitoring
* Customer transaction behavior during weekdays and weekends
* User demographic analysis based on age groups
* Payment method preferences and trends

## Tools & Technologies

* Python
* Jupyter Notebook
* Power BI
* Excel
* Data Cleaning
* Data Modeling
* Data Visualization

## Project Outcome

This project showcases practical skills in data cleaning, transformation, business intelligence, dashboard design, and data storytelling. The interactive Power BI dashboard enables stakeholders to monitor payment performance, identify trends, and make data-driven business decisions effectively.
