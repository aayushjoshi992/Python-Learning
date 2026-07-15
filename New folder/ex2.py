# def check(age):
#     try:
#         if age<18:
#             print("lesser age")
#             raise ValueError("Invalid age value")
#         else:
#             print("valid age for voting")
#     except Exception as e:
#         print(e)

# age=int(input("Enter your age"))
# check(age)

# custom/user-defined Exception
# class BalanceException(Exception):
#     pass

# def checkBalance():
#     earn=10000
#     exp=9000
#     bal=earn-exp
#     if bal<2000:
#         raise BalanceException("not sufficient amount left")
#     else: 
#         print("sufficient amount",bal)

# try:
#     checkBalance()
# except BalanceException as b:
#     print(b)

num="Python"
try:
    print(float(num))
except ValueError:
    print("Invalid numeric value.")
