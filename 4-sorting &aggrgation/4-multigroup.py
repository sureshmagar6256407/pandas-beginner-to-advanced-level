import pandas as pd
data  = { 
    "Name": ["Alice","Rahul", "Bob", "Charlie","tekam", "David"],
    "Age": [25, 30, 35, 40, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "ghorahi","dang"],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000]
}

df = pd.DataFrame(data)
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)