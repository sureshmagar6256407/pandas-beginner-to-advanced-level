import pandas as pd
data  = { 
    "Name" : ["suresh" , "ram" ,"shaym", "hari","kiran","rahul"],
    "Age":[30,40,19,40,39,20],
    "Salary":[50000,40000,31000,49000,40000,5900],
    "PerformanceScore": [85,90,78,92,88,95]
}
df   = pd.DataFrame(data)
print(df)

# df.drop(columns =[column_name] ,inplace =True)
#single columns
df.drop(columns=["PerformanceScore"] ,inplace= True)
print(df)