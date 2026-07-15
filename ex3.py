
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

# dt= dict([("name","ritu"),("id",10),("subject","python")])

# for k in dt.keys():
#     if k=="id":
#         continue
#     print(k)
# d3=dict(Name="Dipika", Age=6)
# print(d3) 


# d={}
# name=input("Enter name:")
# course=input("Enter course:")
# fee=int(input("Enter fee:"))
# d["name"]=name
# d["course"]=course
# d["fee"]=fee
# print(d)



def check(li,di):
    sum=0
    if type(li)==list:
        for l in li:
            sum=sum+l
        print(sum)
    if type(di)==dict:
        print(di)


di={"abc":1,"cde":2}
li=[1,2,3,4,5]
check(li,di)
