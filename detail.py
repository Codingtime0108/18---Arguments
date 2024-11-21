experience = int(input("How many years of experience do you have?"))

def expertise(experience):
    if experience <= 5:
       s = 50000 
    elif experience > 5 and experience < 10 :
        s = 100000
    else:
        s = 200000
    return(s)
b = expertise(experience)
print(f"This will be your salary: ${b}")