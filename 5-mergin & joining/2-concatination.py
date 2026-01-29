"""
Docstring for 5-mergin & joining.2-concatination
vertically (row-wise)
horizontally(column-wise)
pd.concate(df1,df2,axis=0, ignore_index= true)
"""
import pandas   as pd 
df_region1 = pd.DataFrame({
    "Name": ["Alice","Rahul", "Bob", "Charlie","bijaya", "David"],
    "Age": [25, 30, 35, 40, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "ghorahi","dang"]
})
df_region2 = pd.DataFrame({
    "Name": ["Eve","Frank", "Grace", "Henry","Ivy", "Jack"],
    "Age": [27, 31, 36, 41, 29, 33],
    "City": ["Miami", "Seattle", "Boston", "Denver", "Portland","Austin"]
})
concate= pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(concate)