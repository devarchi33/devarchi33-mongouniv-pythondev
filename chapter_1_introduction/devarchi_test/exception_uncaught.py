import sys

# handle exception
try:
    print(5 / 0)
except Exception as e:
    print("exception: ", type(e), e)
print("but life goes on..")

# unhandle exception
print(5 / 0)
print("maybe not print this line..")
