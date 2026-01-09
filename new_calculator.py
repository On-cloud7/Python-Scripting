import sys
num1 = 10
num = 20

def addition():
    add = num1+ num
    print(add)

def sub():
    sub = num1-num
    print(sub)
    
def mul():
    mul = num1* num
    print(mul)
    
def div():
    div = num1/ num
    print(div)
    
addition()
sub()
mul()
div()

num1 = sys.argv[1]
operation = sys.argv[2]
num = sys.argv[3]



