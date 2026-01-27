"linear ,polynomial ,time"

# import pandas as pd
# data  = { 
#     "Name" : ["suresh" , "sita" ,"shaym", "hari","kiran","rahul"],
#     "Age":[30,40,19,40,None,20],
#     "Salary":[50000,40000,31000,None,40000,5900],
#     "PerformanceScore": [85,90,78,92,88,None]
# }
# df   = pd.DataFrame(data)
# print(df)

# df.interpolate(method="linear" ,axis=0,inplace= True)


#linear example  
import pandas as pd 
data  = { 
    'time' :[1,2,3,4,5],
    'value' :[10,None,30,None,50]
} 

df  = pd.DataFrame(data)
print (df)

df['value'] = df['value'].interpolate(method='linear')
print('after interpolation')
print(df)

