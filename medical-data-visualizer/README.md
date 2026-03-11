# Medical Data Visualizer

This project visualizes and analyzes **medical examination data** using **Python, Pandas, Matplotlib, and Seaborn**.  

The goal is to explore the relationship between **cardiovascular disease**, body measurements, blood markers, and lifestyle choices.

---

## Dataset

The dataset used is `medical_examination.csv`, containing patient medical data collected during routine examinations.  

Columns include:

- `age` — age in days  
- `height` — height in cm  
- `weight` — weight in kg  
- `gender` — categorical code  
- `ap_hi` — systolic blood pressure  
- `ap_lo` — diastolic blood pressure  
- `cholesterol` — 1: normal, 2: above normal, 3: well above normal  
- `gluc` — 1: normal, 2: above normal, 3: well above normal  
- `smoke` — smoking habit (binary)  
- `alco` — alcohol intake (binary)  
- `active` — physical activity (binary)  
- `overweight` — calculated from BMI (binary, 0 = not overweight, 1 = overweight)  
- `cardio` — presence or absence of cardiovascular disease (binary)  

---

## Project Description

This project performs the following analysis:

1. **Categorical Plot**  
   - Shows counts of features (`cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`) split by `cardio` status.  
   - Visualizes counts for patients with `cardio=0` and `cardio=1`.

2. **Heat Map**  
   - Cleans data by filtering out incorrect values:
     - Diastolic pressure higher than systolic  
     - Height and weight outside 2.5th–97.5th percentiles  
   - Shows correlation between numeric features.

---

## How to Run

1. Make sure Python 3.x and the required libraries are installed:

```bash
pip install pandas matplotlib seaborn