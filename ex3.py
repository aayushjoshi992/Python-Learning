
# d={"name":"Rakesh","salary":500000,"age":35}
# print(d)
# print(len(d))
# name=d["name"]
# print(name)

# for k,v in d.items():
#     print(f'key is {k} ... value is: {v}')
# sal=d["salary"]
# dis=sal-(sal*0.1)
# print(f'The salary after 10% deduction is{dis}')

# for k in d.keys():
#     if k=="salary":
#         dis=d[k]-(d[k]*0.1)
#         print(f'The salary after 10% deduction is{dis}')

# d["company"]="google"
# print(d)

# del d["company"]
# print(d)

dt= dict([("name","ritu"),("id",10),("subject","python")])

for k in dt.keys():
    if k=="id":
        continue
    print(k)
d3=dict(Name="Dipika", Age=6)
print(d3) 

