
other_file = open('example.txt', 'r')

print("Content type --> ", type(other_file))

print("Printing 1st instance of variable --> ", other_file)

file_content = other_file.readlines()
# file_content = other_file.read()

print('****----------------  Final Jawn ----------------****')

file_content = [i.rstrip('\n') for i in file_content]

print(file_content)
other_file.close()

# file_content.seek(0)  <-- Moves in app text cusor from the end of a file to the beggining.
