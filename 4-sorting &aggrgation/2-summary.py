#df["column name"].mea()
#df["column name"].sum() like that other
import pandas as pd
data  = { 
    "Name": ["Alice","Rahul", "Bob", "Charlie","tekam", "David"],
    "Age": [25, 30, 35, 40, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "ghorahi","dang"]
}
df = pd.DataFrame(data)
avgsalary= df["Age"].mean()
print(avgsalary)