#sorting data 
# df.sort_values[by="column name",true,false, inplace = true]
import pandas as pd 
data  = { 
    "Name": ["Alice","Rahul", "Bob", "Charlie","tekam", "David"],
    "Age": [25, 30, 35, 40, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "ghorahi","dang"]
}
df = pd.DataFrame(data)
#single column sort 
# sortData = df.sort_values(by="Name" , ascending= True, inplace= True)
# print (df)

grouped =df.sort_values(by=["Age","City"], ascending= [True,False], inplace=True)
print(df)