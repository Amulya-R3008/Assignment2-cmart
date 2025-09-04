# Assignment2-cmart

## Overview
This repository contains two main projects for practicing Python programming and data analysis:

1. **Python Practice** – Small Python programs demonstrating fundamental concepts like string manipulation, list comprehension, DataFrame operations, random number generation, and basic data filtering.  
2. **Assessment – ETRM Data Analysis with Pandas & Visualization** – Hands-on assignment to practice data ingestion, transformation, exploratory analysis, and visualization using synthetic ETRM trade data across multiple file formats.

---

## Python Practice

### Purpose
Practice Python basics, **pandas**, and **NumPy** for data manipulation and analysis.

### Included Programs
- **Palindrome Checker** – Validates if a string entered by the user is a palindrome.  
- **List Comprehension – Squares** – Generates squares from a given list of numbers.  
- **Students DataFrame** – Creates a DataFrame of 5 students and filters those who scored more than 80.  
- **Random 5x5 NumPy Array** – Generates a 5x5 array of random integers between 1 and 100.  
- **Products DataFrame** – Manages product details, calculates discounted prices, and filters products cheaper than 500.  

### Technologies Used
- Python 3  
- pandas  
- NumPy  

### Key Learning Outcomes
- Working with strings, lists, and arrays.  
- Creating, manipulating, and filtering pandas DataFrames.  
- Applying basic calculations and logic in Python.  

---

## ETRM Data Analysis with Pandas & Visualization

### Objective
Practice **data ingestion, cleaning, transformation, analysis, and visualization** using Pandas and Python plotting libraries (**Matplotlib, Seaborn, Plotly**).

### Task Description
Synthetic ETRM trade data is provided in six formats:
- CSV (`etrm_trades.csv`)  
- JSON (`etrm_trades.json`)  
- Excel (`etrm_trades.xlsx`)  
- Text (pipe-delimited) (`etrm_trades.txt`)  
- HTML (`etrm_trades.html`)  
- XML (`etrm_trades.xml`)  

Each file contains **100 synthetic trades** with the following fields:
- `TradeID`  
- `Trader`  
- `Commodity`  
- `Volume`  
- `Price`  
- `Currency`  
- `DeliveryStart`  
- `DeliveryEnd`  
- `Periodicity`  

---

## Steps Performed

### 1️. Data Ingestion
- Loaded all six file formats into **pandas DataFrames**.  
- Verified consistency across datasets by checking **column names** and **data types**.  

### 2️. Data Cleaning & Transformation
- Converted `DeliveryStart` and `DeliveryEnd` columns to **datetime** for accurate date operations.  

### 3️. Exploratory Data Analysis (EDA)
- Average price per commodity  
- Distribution of trades by currency  
- Trade periodicity breakdown (Daily, Weekly, Monthly)  

### 4️. Data Visualization
- **Bar chart:** Volume by trade type  
- **Pie chart:** Trades by currency  
- **Line chart:** Average price trend by delivery start date  
- **Histogram:** Distribution of notional values (Volume × Price)  
- **Heatmap:** Commodity vs TradeType counts  

---

## Deliverables
- **Jupyter Notebook (.ipynb)** containing:  
  - Code for loading all file formats  
  - Data transformation steps  
  - Visualizations with insights  
  - A **summary of key insights**  

---

## Requirements
- Python 3.x  
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn` 

Install dependencies using:

```bash
pip install pandas numpy matplotlib seaborn 
