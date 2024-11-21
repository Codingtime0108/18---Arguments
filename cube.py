num = int(input("What is your number?"))
def cube(num):
    return num*num*num
def by_three(num):
    if num %3 == 0:
        return cube(num)
    else:
        return False
print(by_three(num))