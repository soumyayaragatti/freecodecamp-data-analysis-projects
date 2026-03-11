# Page View Time Series Visualizer

This project visualizes daily page view data from the freeCodeCamp forum using Python, Pandas, Matplotlib, and Seaborn.

The goal is to show patterns in visits over time with a **line chart**, a **bar chart**, and **box plots**.

---

## Dataset

The dataset used is `fcc-forum-pageviews.csv`, which contains daily page view counts from **May 9, 2016** to **December 3, 2019**.

You can download it from the freeCodeCamp boilerplate repository.

---

## Project Description

This project includes three visualizations:

1. **Line Plot**  
   - Shows the daily page views over time.
   - Title: `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`
   - X‑axis: Date  
   - Y‑axis: Page Views

2. **Bar Plot**  
   - Shows the **average daily page views** for each month grouped by year.
   - X‑axis: Years  
   - Y‑axis: Average Page Views  
   - Legend: Months

3. **Box Plots**  
   - One plot shows year‑wise distribution (trend).
   - Another shows month‑wise distribution (seasonality).
   - Titles:  
     - `Year-wise Box Plot (Trend)`  
     - `Month-wise Box Plot (Seasonality)`

---

## How to Run

1. Make sure you have Python 3.x installed.

2. Install required libraries:

```bash
pip install pandas matplotlib seaborn