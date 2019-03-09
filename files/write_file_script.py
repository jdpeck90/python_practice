file = open("example.txt", "w")
file.write("Line 4")


print(file)


file = open("example_two.txt", "w")
file.write("Line 1 !")
file.write("Line 2 !")


linelist = ["Line 1", "Line 2", "Line 3"]
for item in linelist:
    file.write(item + "\n")
file.close()
