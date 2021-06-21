output = open('outputt.txt', 'r').read()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(output)
decode = ""
for character in output[0:-1]:
	decode += letters[(letters.index(character)-18)%26]
print(decode)
