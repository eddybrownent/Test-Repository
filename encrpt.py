string = input("Enter a string to hide in uppercase :")
new_string = ""
code = ""
name = ""
for char in string:
    char = str(ord(char))
    
    new_string = new_string + (char)

print("THE SECRET IS ""{}".format(new_string), end="")

print()

print("decripting the string...")

for character in range(0, len(new_string)- 1, 2):
    code = new_string[character] + new_string [character+1]
    name = name + chr(int(code))

print("The name is ""{}".format(name))
