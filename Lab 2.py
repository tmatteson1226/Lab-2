def sum(num1,num2):
    return int(num1) + int(num2)
print sum(58,9)

def subtract(num1,num2):
    return num1 - num2
print subtract(85,6)

def subtractSmaller(num1,num2):
    if num1 > num2:
        ans = num1 - num2
        return ans
    else:
         pass
    if num1 < num2:
        ans = num2 - num1
        return ans
    else:
        pass
print subtractSmaller(3,10)