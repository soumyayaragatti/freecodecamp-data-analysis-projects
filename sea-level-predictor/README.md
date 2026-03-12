# Sea Level Predictor

This project analyzes historical sea level data and predicts future sea level rise using **Python, Pandas, Matplotlib, and SciPy**.

The dataset contains global average sea level measurements from **1880 to 2014**. Using this data, we create a visualization and predict sea level rise through the year **2050**.

---

## Dataset

The dataset used is **epa-sea-level.csv**.

Columns in the dataset:

- **Year** — Year of measurement  
- **CSIRO Adjusted Sea Level** — Sea level measurement in inches  

The data comes from the **US Environmental Protection Agency (EPA)** using data from **CSIRO and NOAA**.

---

## Project Description

This project performs the following tasks:

1. **Scatter Plot**
   - Displays historical sea level data points from 1880 to 2014.

2. **First Line of Best Fit**
   - Uses all available data to predict sea level rise through 2050.

3. **Second Line of Best Fit**
   - Uses only data from the year **2000 onwards** to predict sea level rise through 2050.

The visualization helps compare long-term trends with more recent trends in sea level rise.

---

## Graph Details

- **Title:** Rise in Sea Level  
- **X-axis:** Year  
- **Y-axis:** Sea Level (inches)

The graph includes:
- Scatter points for real data
- Regression line for all data
- Regression line for recent data

---

## How to Run

1. Install required libraries:

```bash
pip install pandas matplotlib scipy