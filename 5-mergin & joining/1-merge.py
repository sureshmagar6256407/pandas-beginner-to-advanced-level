# pd.merge(df,df2,on="column name", how=)

import pandas as pd 
data1 = {
    "Name": ["Alice","Rahul", "Bob", "Charlie","bijaya", "David"],
    "Age": [25, 30, 35, 40, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "ghorahi","dang"]
}
data2 = { 
    "Name": ["Alice","Rahul", "Bob", "Charlie","tekam", "Suresh"],
    "Age": [25, 30, 35, 40, 28, 32],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merge =pd.merge(df1,df2, on= "Name", how="outer")
print(merge)