flag = open('flag.txt','r').read() #open the flag
assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)


output = open('output.txt', 'r').read()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decode = ""
for character in output:
	decode += letters[(letters.index(character)-18)%26]
print(decode)

