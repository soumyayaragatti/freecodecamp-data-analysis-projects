# Demographic Data Analyzer

This project analyzes demographic data from the **1994 Census dataset** using **Python and Pandas**.  

You will answer questions about age, education, race, occupation, work hours, and income distribution.  

---

## Dataset

The dataset used is `adult.data.csv` from the **UCI Machine Learning Repository**:

- Source: [https://archive.ics.uci.edu/ml/datasets/adult](https://archive.ics.uci.edu/ml/datasets/adult)  
- Format: CSV, 15 columns including age, education, occupation, hours-per-week, salary, etc.

---

## Project Description

This project performs the following analysis:

1. Count the number of people of each race.  
2. Calculate the average age of men.  
3. Calculate the percentage of people with a Bachelor's degree.  
4. Calculate the percentage of people with advanced education (`Bachelors`, `Masters`, `Doctorate`) earning more than 50K.  
5. Calculate the percentage of people without advanced education earning more than 50K.  
6. Find the minimum number of hours worked per week.  
7. Calculate the percentage of people working the minimum hours earning more than 50K.  
8. Identify the country with the highest percentage of people earning more than 50K.  
9. Find the most popular occupation for those earning more than 50K in India.

---

## How to Run

1. Make sure Python 3.x and Pandas are installed.  
2. Ensure the dataset `adult.data.csv` is in the project folder.  
3. Run the main file:

```bash
python main.py