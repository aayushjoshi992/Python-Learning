# x=10    
# y=0
# try:
#     z=x/y
#     print(z)
# except Exception as e:
#     print(e)
# print("last line")

# x=10    
# y=0
# try:
#     z=x/y
#     print(z)
# except Exception as e:
#     print(e)
# else:
#     print("runs when no error in try block")
# finally:
#     print("always runs")
# print("last line")


def divide(a,b):
    try:
        z=a/b
        print(z)
    except Exception as e:
        print("cannot run")

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
divide(num1,num2)