import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Basic info
df.head()
df.info()

# Data cleaning
df = df.dropna()
df = df.drop_duplicates()

# Select useful columns
cols = ['Age','Attrition','BusinessTravel','Department','DistanceFromHome','Education','Gender',
        'JobLevel','JobRole','MaritalStatus','MonthlyIncome','OverTime','PercentSalaryHike',
        'PerformanceRating','TotalWorkingYears','YearsAtCompany','YearsInCurrentRole']
df = df[cols]

# Save cleaned file
df.to_csv("cleaned_hr_data.csv", index=False)

df.describe()