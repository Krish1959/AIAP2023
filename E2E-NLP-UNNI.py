#AIAP Project by UNNI KRISHNAN AMBADY (Sxxxx664B)
#This is an end-to-end Machine Learning Pipeline (MLP)
# STILL UNDER CONSTRUCTION

'''
The Steps in this File are:
1. Input data from the datbase and clean the data
2. Data Splitting: Split the data into training and testing sets (80%-20%). 
3. Feature Selection/Engineering (Optional):
4. Model Selection: Models to be considered are any 3 from below:
    Linear Regression, (Simple)
    Decision Trees,
    Random Forests, (Ideal in this case)
    Gradient Boosting (not tried) 
5. Model Training:
6. Evaluate the model's performance using metrics
    (Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE))
7. Hyperparameter Tuning (if time permits):
8. Model Evaluation:
9. Model Interpretation (if time permits):
    For selected models to consider techniques like feature importance analysis or
    SHAP (SHapley Additive exPlanations) values to interpret how different features affect the predictions.
10. Documentation & Submision (on Github):
'''
print(" hello")
#Import Libraries
import numpy as np
'''
import sys
sys.path.append("C:\\UNNI\\AISG-2023")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
#-------------------------
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
#-----------------------------------
print(" Imported Lib")
"""