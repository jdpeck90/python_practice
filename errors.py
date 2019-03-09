b = "2"
a = 1
c = 3

print('first', int(2.5))
print('2nd', a + int(b))
print('3rd', c)


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return print('Zero division is meaningless')
    except:
        return print('Not a Zero division error')


print(divide(1, '1'))
print('End of Program')
