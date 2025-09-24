def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("enter a value:"))
b=int(input("enter b value:"))
e=input("enter symbol e:")
if(e == '+'):
   e=add(a,b)
elif(e =='-'):
   e=sub(a,b)
elif(e =='*'):
   e=multiply(a,b)
elif(e =='/'):
   e=divide(a,b)
elif(e =='%'):
   e=modulus(a,b)
print(f"Result={e}")










