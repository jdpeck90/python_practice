

def age_foo(age):
    new_age = age + 50
    return new_age


age = int(input("enter your age: "))

conditional = 'this age is not possible' if age > 150 else age_foo(age)

print(conditional)
