import datetime
import time
r"""
This script creates an empty file.
"""

newList = []
for i in range(5):
    newList.append(datetime.datetime.now())
    time.sleep(1)

print('NewList -->', newList)

filename = datetime.datetime.now()
now = datetime.datetime.now()


after = now + datetime.timedelta(seconds=100003)

print('After -->', after)


def create_file():
    """this function creates an empty file."""

    with open(str(filename.strftime('%Y-%m-%B-%S')+".txt"), "w") as file:
        file.write("")


newDate = str(datetime.datetime(2018, 5, 14, 11, 19, 39, 583348))
print('newDate --> ', newDate)

# superNew = datetime.str("%Y-%n-%d-%H-%M-%S-%f")
# print('superNew --> ', superNew)


create_file()


# date = datetime.datetime.now()
# print(date)
