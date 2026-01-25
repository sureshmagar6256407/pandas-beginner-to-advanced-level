# head() tail()
# head() give dfault 5 
# head(n) first n row 
#tail () give default 5  
# tail(n) last n row

import pandas as pd 
df   =pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(f"display 10 rows of first")
print(df.head(10))

print(f"display 10 rows of last ")
print(df.tail(10))
# print(df)