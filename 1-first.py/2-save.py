import pandas as pd 
data  = { 
    "name" :["ram","shaym","ghanshyam"],
    "age":[20,31,23],
    "City":["ktm","ghorahi","pokhara"]
}
df  = pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)