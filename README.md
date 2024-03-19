# machine_learning_Assignment
1. An introduction to the script.
The dataset can be found https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data
It is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict based on diagnostic measurements whether a patient has diabetes.

The data include 9 features, the Outcome is what we are going to predict based on the 8 features such as glucose, blood pressure, insulin and etc

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skin fold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: Diabetes pedigree function
Age: Age (years)
Outcome: Class variable (0 or 1)


2. Instructions on how to set up the environment to run the script (e.g., required packages, data files)
   
Install Python: Make sure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/
Install pip: pip is the package installer for Python. It allows you to install and manage Python packages easily.
Create a Virtual Environment (Optional but Recommended): It's a good practice to create a virtual environment to isolate your project's dependencies.
Install Required Packages: You can install the required packages using pip. For this model, you'll need pandas, scikit-learn, and you would import the LinearRegression model, sklearn.model_selection module, argparse module and etc.
Download the Diabetes Dataset from https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data

3. A description of the script's functionality.
   
The clean.py script is responsible for preprocessing and cleaning the dataset. It takes a raw dataset as input, applies necessary data cleaning operations such as handling missing values, removing outliers, and performing feature engineering, and produces a cleaned dataset ready for training.
The train.py script is responsible for training a machine learning model using the cleaned dataset. It takes the cleaned dataset as input, splits it into training and testing sets, trains the model using the training data, and return the score and mean absolute error
The main.py script serves as the main entry point for orchestrating the data cleaning and training processes. It imports functionalities from clean.py and train.py, executes them sequentially, and manages the overall workflow.
