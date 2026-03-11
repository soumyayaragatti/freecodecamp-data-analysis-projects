# Mean Variance Standard Deviation Calculator

This project is part of the **freeCodeCamp Data Analysis with Python Certification**.

## Project Description

The goal of this project is to create a function that calculates statistical values from a list of numbers.

The function converts a list of **9 numbers** into a **3×3 matrix** using NumPy and calculates:

* Mean
* Variance
* Standard Deviation
* Maximum
* Minimum
* Sum

These calculations are performed across:

* Columns
* Rows
* The entire matrix

## Technologies Used

* Python
* NumPy

## Project Files

* `mean_var_std.py` → Contains the main `calculate()` function
* `main.py` → Used to test the function
* `test_module.py` → Contains unit tests

## Example

Input:

```
calculate([0,1,2,3,4,5,6,7,8])
```

Output:

```
{
 'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
 'standard deviation': [[2.44..., 2.44..., 2.44...], [0.81..., 0.81..., 0.81...], 2.58...],
 'max': [[6,7,8],[2,5,8],8],
 'min': [[0,1,2],[0,3,6],0],
 'sum': [[9,12,15],[3,12,21],36]
}
```

## Author

Soumya
