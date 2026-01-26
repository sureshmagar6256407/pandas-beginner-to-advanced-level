import pandas as pd  
df   =pd.read_csv ("output.csv",encoding='latin1')
print("displaying the info of data set")
print(df.info())