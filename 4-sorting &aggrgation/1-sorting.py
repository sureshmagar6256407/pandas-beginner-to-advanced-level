#sorting data 
# df.sort_values[by="column name",inplace = true]
import pandas as pd 
data  = { 
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
sortData = df.sort_values(by="Name" , inplace= True)
print (df)