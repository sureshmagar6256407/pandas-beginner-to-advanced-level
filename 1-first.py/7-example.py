import pandas as pd
data  = { 
    "Name" : ["suresh" , "ram" ,"shaym", "hari","kiran","rahul"],
    "Age":[30,40,19,40,39,20],
    "Salary":[50000,40000,31000,49000,40000,5900],
    "PerformanceScore": [85,90,78,92,88,95]
}
df   = pd.DataFrame(data)

print("samle Data Frame")
print(df)

#single columns
# print("names : (single columns retrun series)")
# print(df["Name"])

#multiplecolumns  
# print("names and age : ")
# print(df[["Name","Age"]])

#filtering the row one condition
# highSalary  = df[df["Salary"] > 40000]
# print(f"employe with salary {highSalary}")

#filtering the row multi condition 
# print("employe with :\n")
# filtered  = df[(df["Salary"] >30000) & (df["Salary"] <42000)]
# print(filtered)

#using or condition 
filteredOR = df[(df["Salary"]>40000) | (df["PerformanceScore"] > 90)]
print(filteredOR)


