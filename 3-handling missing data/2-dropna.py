#dropna()
# df.dropna(axis=0 ,inplace =True)


import pandas as pd
data  = { 
    "Name" : ["suresh" , None ,"shaym", "hari","kiran","rahul"],
    "Age":[30,40,19,40,None,20],
    "Salary":[50000,40000,31000,None,40000,5900],
    "PerformanceScore": [85,90,78,92,88,None]
}
df   = pd.DataFrame(data)
print(df)

df.dropna(inplace= True)
print(df)