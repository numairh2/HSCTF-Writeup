# HSCTF – Aptenodytes-Forsteri

* **Category:** crypto
* **Points:** 183
* **Solved:** During CTF

## Challenge

> Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.

## Solution
By looking at the python script the *flag.txt* was encrypted by adding 18 character values to each character in the text file and gives us the output and puts it in a text file called *output.txt*

In order to get the flag, we need to create a simple python script that takes the output and substracts each character by 18 character values to gives us the flag.


```python3
output = open('outputforAp.txt', 'r').read()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decode = ""

for character in output[0:-1]:
decode += letters[(letters.index(character) - 18) % 26]

print("flag{" + decode + "}")
```

`Flag = flag{QWERTYUIOP}`
