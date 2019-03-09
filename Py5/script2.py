def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars


r = float(input("enter rate: "))
e = float(input("enter Euros: "))


print(currency_converter(r, e))
